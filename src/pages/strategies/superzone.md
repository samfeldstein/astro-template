---
layout: "@layouts/Strategy.astro"
title: Superzone Trading Strategy
description: The Superzone trading strategy takes trades that fall within overlapping orders blocks and supply and demand zones across multiple timeframes.
---

Turn on [BigBeluga Supply and Demand Zones](https://www.tradingview.com/script/I0o8N7VW-Supply-and-Demand-Zones-BigBeluga/), [LuxAlgo Order Blocks](https://www.luxalgo.com/library/indicator/order-block-detector/), and [LuxAlgo Fair Value Gaps](https://www.luxalgo.com/library/indicator/fair-value-gap/). Trace zones on 1hr, 15m, 5m, and 1m. (I'm looking to open and close trades in a few hours or less, so these ranges are the most relevant.)

A **superzone** is any area where two or more zones or gaps overlap on two or more timeframes.

Enter on 1m chart at the strongest superzone. _Price must be in a 1m zone, show a [WillyAlgo PrecSniper reversal](https://www.tradingview.com/script/IZj18oYZ-Precision-Sniper-WillyAlgoTrader/), or show a reversal pattern_.

Set SL past superzone. When prices hits next support/resistance, move stop to a point where you can make the most profit without triggering early.

Repeat until 1m shows reversal.
