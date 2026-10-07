---
description: Run the full strategy pipeline (hypotheses to validated candidates or NO TRADE)
argument-hint: <market + idea, e.g. "NIFTY mean reversion, 15m, futures">
---

Use the `quantforge-ai` skill, workflow B. Idea: $ARGUMENTS

Generate 2-3 hypotheses, define them mathematically, write complete specs, state the backtest quality declaration, and run only what the available data supports. If the user supplied no data, stop at spec + `DATA REQUIRED` list; never invent results. Reject failures. Finish with the research report template and a verdict (REJECT / NEEDS MORE DATA / PAPER-TRADE ONLY / NO TRADE / CANDIDATE).
