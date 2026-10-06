# Charts in email

Every chart is HTML tables and background colors. No images, no SVG, no
canvas — none of them render reliably across mail clients.

## The one thing that will break your chart

**An HTML table resolves ONE width per column across all rows.** Putting a
different `width="N"` on the bar cell of each row does nothing: every bar
collapses to the widest declaration and the chart shows nothing.

**The fix:** give each row its own nested table for the bar, and size the
fill cell with a PERCENTAGE, which resolves per row:

```html
<tr>
  <td width="120" style="width:120px;">Setting Spray</td>
  <td>
    <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%"><tr>
      <td width="38%" style="width:38%;"><div style="height:16px;background-color:#17533F;border-radius:4px;line-height:16px;font-size:0;">&nbsp;</div></td>
      <td style="padding-left:10px;white-space:nowrap;">12.6%</td>
    </tr></table>
  </td>
</tr>
```

## Rules

- **Zero-based and proportional.** Compute one px-or-percent-per-unit
  factor for the whole chart and apply it to every row. Never eyeball.
- **Label column wide enough for its longest label.** Labels are
  `white-space:nowrap`; measure the longest string and add ~16px.
- **Every chart has a caption** that states the takeaway in a sentence.
- **Only plot rows that have a value on that axis.** A line that did not
  add spend has no position on a marginal-return axis — leave it off the
  chart and say why in the caption, then cover it in the line panel
  instead.
- **Color carries meaning:** `#17533F` best/primary, `#778867` middle,
  `#C4A574` current-period, `#C65345` the problem, `#B7AA98` inert/below
  break-even.
- Bar height 14-22px, radius 4px, and always set `line-height` equal to
  height plus `font-size:0`, or Outlook adds space inside the bar.

## Marginal-return axis specifically

This chart only plots lines where spend increased week over week — a line
that cut spend has no incremental dollar to measure a return on. Mark a
break-even reference line at $1.00 (a thin dashed rule, not a bar) so a
below-break-even bar reads instantly. State in the caption which lines are
excluded and why ("Five lines cut spend and grew retail; they have no
position on this axis by definition — see the line panels below").

## Two-part share bars (revenue mix, brand vs. non-brand)

Percentage cells with a 4px spacer cell between, rounded outer corners
only, same pattern as a single bar but split in two.

## Trend / day-over-day bars

One row per day, Sunday first. Use `#C4A574` (sand) for the current
period's bars and `#17533F` for the prior period's, or `#778867` for a
mid-tier day if you need a third shade for an outlier. Always state the
actual weekday next to the date — verify it, never assume.
