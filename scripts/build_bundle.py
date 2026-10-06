#!/usr/bin/env python
"""Sync all skills into skills/<name>/ and rebuild dist/ bundles.

    python scripts/build_bundle.py [--force] [--out dist]

Reads each skill's latest release tag. If nothing moved since the last run,
exits. Otherwise, for each skill:

- vendors it into skills/<name>/                 (what repo-download users consume)
- adds it to dist/trackiq-skills.zip             (unzip -d ~/.claude/skills)
- writes dist/<name>.zip                         (per-skill, for claude.ai upload)

Also writes trackiq-skills.manifest.json at the repo root (what CI diffs
against to know whether anything moved) and dist/ (what ships with the
Release so trackiq.com/skills can read it).

Prints changed=true for the workflow. GITHUB_TOKEN, if set, is used for API
calls (unauthenticated calls are capped at 60 an hour).
"""
import argparse, io, json, os, shutil, sys, time, urllib.error, urllib.request, zipfile

ORG = "TrackIQ-HQ"
REPO = "amazon-seller-skills"
BUNDLE = "trackiq-skills.zip"
MANIFEST = "trackiq-skills.manifest.json"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT, "skills")


def fetch(url, api=False):
    req = urllib.request.Request(url, headers={"User-Agent": "trackiq-sync"})
    if api:
        req.add_header("Accept", "application/vnd.github+json")
        if os.environ.get("GITHUB_TOKEN"):
            req.add_header("Authorization", "Bearer " + os.environ["GITHUB_TOKEN"])
    # GitHub release downloads occasionally 5xx right after an asset is
    # replaced; retry rather than fail the hourly run.
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code < 500 or attempt == 3:
                raise
        except urllib.error.URLError:
            if attempt == 3:
                raise
        time.sleep(5 * (attempt + 1))


def current_manifest():
    """What we last vendored into skills/ — {} on first run."""
    p = os.path.join(ROOT, MANIFEST)
    if os.path.exists(p):
        return json.load(open(p, encoding="utf-8"))
    return {}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="sync even if nothing changed")
    ap.add_argument("--out", default=os.path.join(ROOT, "dist"))
    a = ap.parse_args()

    skills = json.load(open(os.path.join(ROOT, "registry.json"), encoding="utf-8"))["skills"]
    tags = {
        s["name"]: json.loads(fetch(
            f"https://api.github.com/repos/{ORG}/{s['name']}/releases/latest", api=True
        ))["tag_name"]
        for s in skills
    }
    before = current_manifest()
    changed = a.force or tags != before

    if not changed:
        print(f"{len(skills)} skills unchanged")
        if os.environ.get("GITHUB_OUTPUT"):
            with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
                fh.write("changed=false\n")
        return

    # Fetch every skill's release zip once, into memory.
    raws = {s["name"]: fetch(s["install"]["zip"]) for s in skills}

    # Validate shape before we touch skills/ — each must unpack to
    # <name>/SKILL.md, or the vendored tree ends up scrambled.
    for s in skills:
        z = zipfile.ZipFile(io.BytesIO(raws[s["name"]]))
        names = z.namelist()
        stray = [n for n in names if not n.startswith(s["name"] + "/")]
        if stray or s["name"] + "/SKILL.md" not in names:
            sys.exit(f"{s['name']}: zip is not <name>/SKILL.md-shaped (stray: {stray[:3]})")

    # Wipe and re-vendor skills/ so the tree always matches the manifest.
    if os.path.exists(SKILLS_DIR):
        shutil.rmtree(SKILLS_DIR)
    os.makedirs(SKILLS_DIR, exist_ok=True)
    for s in skills:
        zipfile.ZipFile(io.BytesIO(raws[s["name"]])).extractall(SKILLS_DIR)

    # Build dist/trackiq-skills.zip + per-skill zips for the Release.
    os.makedirs(a.out, exist_ok=True)
    bundle = zipfile.ZipFile(os.path.join(a.out, BUNDLE), "w", zipfile.ZIP_DEFLATED)
    for s in skills:
        z = zipfile.ZipFile(io.BytesIO(raws[s["name"]]))
        for n in z.namelist():
            bundle.writestr(n, z.read(n))
        with open(os.path.join(a.out, s["name"] + ".zip"), "wb") as fh:
            fh.write(raws[s["name"]])
    bundle.close()

    # Manifest in dist/ (shipped with Release) AND at repo root (committed —
    # the next run reads it to decide whether anything moved).
    for p in (os.path.join(a.out, MANIFEST), os.path.join(ROOT, MANIFEST)):
        with open(p, "w", encoding="utf-8") as fh:
            json.dump(tags, fh, indent=2, sort_keys=True)

    diff = sorted(k for k in tags.keys() | before.keys() if tags.get(k) != before.get(k))
    print(f"synced {len(skills)} skills; changed: {', '.join(diff) or 'forced'}")

    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
            fh.write("changed=true\n")


if __name__ == "__main__":
    main()
