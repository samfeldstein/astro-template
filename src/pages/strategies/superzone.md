---
layout: "@layouts/Strategy.astro"
title: Superzone Strategy
description: The Superzone trading strategy takes trades that fall within overlapping support and resistance areas across multiple timeframes.
---

Turn on [LuxAlgo Smart Money Concepts](https://www.luxalgo.com/library/indicator/smart-money-concepts-smc/) to find order blocks. Use [LuxAlgo Fair Value Gaps](https://www.luxalgo.com/library/indicator/fair-value-gap/) to find FVGs. (LuxAlgo SMC has an FVG detector, but it seems less accurate.) 

Open the daily chart draw a horizontal line on the top border of the nearest support zone and/or the bottom border of the nearest resistance zone.

Repeat for the 4h, 1h, and 5m charts. The area between the lines is your entry zone.

In an uptrend, the ideal entry is the bottom of the zone. In a downtrend, the ideal entry is the top of the zone. Two or more lines close together indicate overlap between timeframes and also might be a good entry.

*You must have at least a 5m line and one line from a higher timeframe. If you have just a 5m line, you don't have higher timeframes backing you. If you just have a higher timeframe, your entry will not be precise.*
