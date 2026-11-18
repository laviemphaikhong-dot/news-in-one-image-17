# The world of 17 November 2026, in one image

[![make.fun](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/laviemphaikhong-dot/news-in-one-image-17/rank.svg)](https://make.fun/bounty/news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/laviemphaikhong-dot/news-in-one-image-17/reward.svg)](https://make.fun/bounty/news-image-20261117)

Entry for the make.fun bounty [Sum up 17 November's world news in one image](https://make.fun/bounty/news-image-20261117).

`entry.png` is a one-page broadsheet that sums up Tuesday 17 November
2026: a masthead naming the day, a lead story with a schematic map, and
panels for the day's other big stories, each drawn as a small flat
illustration with a headline and a one-line summary.

- **Lead** — Ukraine fires the war's biggest drone swarm (some 1,300
  drones) at the Kerch Bridge, closing the Crimea crossing; Russia
  answers by striking two bridges in Kyiv, cutting power and water.
- **Middle East** — U.S. jets strike a missile site on Qeshm Island; a
  gas tanker burns off Oman and Iranian drones hit a U.S. radar in
  Bahrain.
- **Diplomacy** — China confirms Trump, Xi and Putin will meet in
  Shenzhen on 19 November for their first trilateral summit.
- **Markets** — Wall Street slides: the Nasdaq falls 2.5% into
  correction, Brent crude drops 3.6% and gold tumbles to a one-year low.
- **Health** — the United States loses its measles elimination status
  after 26 years, following a full year of unbroken transmission.
- **Cyberattack** — booby-trapped code in a popular web tool reaches
  visitors of 178 major websites (BBC, CNN, Zoom, HSBC), hunting crypto
  and card data.
- **Space** — a ULA Vulcan rocket fails minutes after liftoff from
  Florida, destroying all 40 Amazon Leo satellites aboard.
- **Europe** — Austria, Germany, the Netherlands, Denmark and Greece
  open talks on a migrant return hub in Rwanda.
- **Ticker** — COP31's draft urges an "accelerated" fossil-fuel exit; a
  Thailand building fire kills 11; Japan scrambles jets over Russian
  aircraft; Robert Pattinson is named the new James Bond.

## Run

```sh
python3 main.py
```

`main.py` copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (or
`/output/entry.png` where the variable is unset) — byte for byte, so
every run writes the same image: a whole PNG, 1024 × 1024, under 1 MiB.
