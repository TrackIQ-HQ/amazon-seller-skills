#!/usr/bin/env python
"""Rebuild trackiq-skills.zip — every skill in registry.json in one archive.

    python scripts/build_bundle.py [--force] [--out dist]

Reads each skill's latest release tag. If the set of skills and tags matches
the manifest already published beside the bundle, there is nothing to do and
the script exits without writing. Otherwise it downloads each skill's own
release zip, checks it unpacks to <skill-name>/SKILL.md, and writes:

    dist/trackiq-skills.zip             unzip -d ~/.claude/skills
    dist/trackiq-skills.manifest.json   {skill-name: release tag}

and prints changed=true for the workflow. GITHUB_TOKEN, if set, is used for
API calls (unauthenticated calls are capped at 60 an hour).
"""
import argparse, io, json, os, sys, urllib.error, urllib.request, zipfile

ORG = "TrackIQ-HQ"
REPO = "amazon-seller-skills"
BUNDLE = "trackiq-skills.zip"
MANIFEST = "trackiq-skills.manifest.json"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def fetch(url, api=False):
    req = urllib.request.Request(url, headers={"User-Agent": "trackiq-bundle"})
    if api:
        req.add_header("Accept", "application/vnd.github+json")
        if os.environ.get("GITHUB_TOKEN"):
            req.add_header("Authorization", "Bearer " + os.environ["GITHUB_TOKEN"])
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def published_manifest():
    """The manifest beside the current bundle, or {} before the first build."""
    try:
        return json.loads(fetch(f"https://github.com/{ORG}/{REPO}/releases/latest/download/{MANIFEST}"))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return {}
        raise


def build(skills, out):
    bundle = zipfile.ZipFile(os.path.join(out, BUNDLE), "w", zipfile.ZIP_DEFLATED)
    for s in skills:
        z = zipfile.ZipFile(io.BytesIO(fetch(s["install"]["zip"])))
        names = z.namelist()
        # Each skill zip must unpack to exactly one folder named for the skill,
        # or unzipping the bundle into ~/.claude/skills scatters files.
        stray = [n for n in names if not n.startswith(s["name"] + "/")]
        if stray or s["name"] + "/SKILL.md" not in names:
            sys.exit(f"{s['name']}: zip is not <name>/SKILL.md-shaped (stray: {stray[:3]})")
        for n in names:
            bundle.writestr(n, z.read(n))
    bundle.close()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="rebuild even if nothing changed")
    ap.add_argument("--out", default=os.path.join(ROOT, "dist"))
    a = ap.parse_args()

    skills = json.load(open(os.path.join(ROOT, "registry.json"), encoding="utf-8"))["skills"]
    tags = {s["name"]: json.loads(fetch(f"https://api.github.com/repos/{ORG}/{s['name']}/releases/latest", api=True))["tag_name"]
            for s in skills}
    before = published_manifest()
    changed = a.force or tags != before
    if changed:
        os.makedirs(a.out, exist_ok=True)
        build(skills, a.out)
        with open(os.path.join(a.out, MANIFEST), "w", encoding="utf-8") as fh:
            json.dump(tags, fh, indent=2, sort_keys=True)
        diff = sorted(k for k in tags.keys() | before.keys() if tags.get(k) != before.get(k))
        print(f"rebuilt {len(skills)} skills; changed: {', '.join(diff) or 'forced'}")
    else:
        print(f"{len(skills)} skills unchanged")
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
            fh.write(f"changed={'true' if changed else 'false'}\n")


if __name__ == "__main__":
    main()
