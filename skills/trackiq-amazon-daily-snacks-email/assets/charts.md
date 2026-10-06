# Charts in email

Every chart is HTML tables and background colors. No images, no SVG, no
canvas — they will not render.

## The one thing that will break your chart

**An HTML table resolves ONE width per column across all rows.** Putting a
different `width="N"` on the bar cell of each row does nothing: every bar
collapses to the widest declaration and the chart shows nothing. This bug
shipped twice in this format's history and is invisible unless you measure.

**The fix:** give each row its own nested table for the bar, and size the
fill cell with a PERCENTAGE, which resolves per row:

```html
<tr>
  <td width="112" style="width:112px;">Patio Lighting</td>
  <td>
    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%"><tr>
      <td width="30%" style="width:30%;"><div style="height:16px;background-color:#17533F;border-radius:4px;line-height:16px;font-size:0;">&nbsp;</div></td>
      <td style="padding-left:10px;white-space:nowrap;">13.4%</td>
    </tr></table>
  </td>
</tr>
```

## Rules

- **Zero-based and proportional.** Compute one px-or-percent-per-unit
  factor for the whole chart and apply it to every row. Never eyeball.
- **Label column wide enough for its longest label.** Labels are
  `white-space:nowrap`; if the text equals the cell width it touches the
  bar. Measure the longest string, add ~16px.
- **Every chart has a caption** that states the takeaway in a sentence.
  A chart with no caption is decoration.
- **Only plot lines that belong on the axis.** If a line has no value on
  the chart's axis, leave it out and explain the absence in the caption.
- **Color carries meaning:** `#17533F` best/primary, `#778867` middle,
  `#C4A574` current-or-latest, `#C65345` the problem, `#B7AA98` inert.
- Bar height 14–18px, radius 4px, and always set
  `line-height` equal to height plus `font-size:0` or Outlook adds space.

## Split bars

For a two-part share bar (revenue mix), use percentage cells with a 4px
spacer cell between, and round the outer corners only.
