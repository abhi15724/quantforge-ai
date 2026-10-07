---
description: Compute performance, tail risk, bootstrap CI and IS/OOS split from a returns or trades CSV
argument-hint: <path to CSV with column ret or pnl> [periods-per-year] [cost-bps]
---

Run `scripts/metrics.py` from the `quantforge-ai` skill on the attached/pointed CSV: $ARGUMENTS
Use `--returns` if the file has a `ret` column, `--trades` if it has `pnl`. Default 252 periods per year and 0 cost unless given. Report the output faithfully, then interpret: is OOS consistent with IS, does the bootstrap CI exclude zero, does edge survive 2x costs. Never fabricate data if the file is missing.
