---
description: Try to break a strategy or backtest (overfitting, bias, cost sensitivity, regime dependence)
argument-hint: <paste strategy/backtest or attach a CSV>
---

Use the `quantforge-ai` skill, workflow C, on: $ARGUMENTS

Fill the backtest quality declaration (unknown means INCOMPLETE). Answer the 10-point overfitting checklist PASS/FAIL/UNKNOWN. If a returns or trades CSV is provided, run `scripts/metrics.py` and report IS vs OOS, bootstrap CI, and 2x cost stress. Delegate adversarial review to the `overfitting-detector` and `risk-manager` agents when available. Give a verdict, leading with the biggest weakness.
