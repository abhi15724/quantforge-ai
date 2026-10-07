---
description: Create a specialized quant trading agent (market, strategy type, data, risk, execution, failure conditions)
argument-hint: <what the agent should trade, e.g. "BANK NIFTY weekly options, intraday">
---

Use the `quantforge-ai` skill. Task: create a trading agent for: $ARGUMENTS

1. Infer market, asset class, strategy type, timeframe, data requirements, risk profile, execution needs. Ask at most 2 questions, only if truly blocking; otherwise list your assumptions.
2. Return the Agent Creation Spec card from `references/agents.md`.
3. Mark every data requirement not confirmed by the user as `DATA REQUIRED`.
4. State the mode (RESEARCH by default) and latency tier. Do not enable LIVE.
