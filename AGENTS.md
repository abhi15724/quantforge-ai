# AGENTS.md — QuantForge AI

Instructions for AI coding/agent tools (OpenAI Codex, Cursor, GitHub Copilot agent, Gemini CLI, Aider, and others that read AGENTS.md).

## What this repo is
A quantitative trading research and engineering playbook: strategy pipeline, validation gates, overfitting checks, risk limits, and market-specific rules (India NSE/BSE/MCX, US, FX, commodities, crypto).

## How to use it
When a task involves designing, backtesting, validating, or risk-reviewing a trading strategy or trading agent, FIRST read `skills/quantforge-ai/SKILL.md`, then load only the reference files it points to:
- `skills/quantforge-ai/references/agents.md` — agent roster and agent-creation card
- `skills/quantforge-ai/references/strategy-spec-and-report.md` — spec, backtest declaration, report template, scoring
- `skills/quantforge-ai/references/validation-gates.md` — stage gates, overfitting checklist, robustness tests
- `skills/quantforge-ai/references/india-markets-and-costs.md` — Indian market and cost rules
- `skills/quantforge-ai/references/execution-and-risk.md` — modes, hard limits, pre-trade checks, latency tiers

To compute metrics from a CSV: `python skills/quantforge-ai/scripts/metrics.py --returns file.csv` (column `ret`) or `--trades file.csv` (column `pnl`). Needs `pip install -r requirements.txt`.

Adversarial reviewer prompts: `agents/overfitting-detector.md`, `agents/risk-manager.md`. Task prompts: `commands/*.md` (treat them as reusable prompt templates).

## Hard rules (never override)
1. Never fabricate prices, candles, option chains, OI, volume, backtest results, fills or P&L. Missing data → say `DATA REQUIRED`.
2. Never guarantee profit, win rate or returns. Use probabilistic language.
3. Label every claim by stage: hypothesis, backtest, out-of-sample, walk-forward, paper, simulated execution, live.
4. Risk outranks return. `NO TRADE` is a valid answer.
5. Never place or enable live orders without the pre-trade checklist and explicit user approval. Default to dry-run/paper.
6. Verify exchange-specific numbers (lot sizes, STT/charges, expiry days, margins, regulations) from current sources; never rely on memory.

## Dev
Run tests: `pip install -r requirements.txt pytest && pytest -q`.
