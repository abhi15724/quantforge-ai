# QuantForge AI — Quant Trading Agents, Backtesting & Risk Skill for Claude, Codex and AI Coding Tools

**QuantForge AI** is an open-source plugin and skill pack that turns an AI assistant into a small quantitative research team. It creates algorithmic trading agents, designs and validates systematic strategies, detects backtest overfitting, and enforces risk limits for **Indian markets (NSE, BSE, NIFTY, BANK NIFTY, FINNIFTY, MCX)**, US and global equities, options and futures, forex, commodities and crypto.

Works with **Claude (chat website, desktop, mobile)**, **Claude Code**, **OpenAI Codex**, and any tool that reads `AGENTS.md` or custom instructions (Cursor, GitHub Copilot agent, Gemini CLI and others).

> **Disclaimer.** Research and engineering aid only. Not financial advice, not a trading system. It does not guarantee profit, does not supply market data, and does not place live orders. Backtests are not predictions; trading carries substantial risk of loss. You are responsible for your decisions and for compliance with your exchange, broker and local regulations.

## Why use it
- **No fabricated data.** Missing inputs return `DATA REQUIRED`, never made-up prices, option chains or backtest results.
- **Validation gates, not vibes.** Every claim is labelled: hypothesis, backtest, out-of-sample, walk-forward, paper, simulated execution or live, and each stage needs its own evidence.
- **Overfitting detection.** A 10-point checklist (look-ahead, survivorship, leakage, data snooping, multiple testing, cost sensitivity, regime dependence).
- **Risk before return.** Hard limits, kill switch, pre-trade checks, and `NO TRADE` as a valid answer.
- **Honest about latency.** Separates research, paper, retail live and institutional HFT; never promises nanosecond execution.
- **Built-in metrics.** Sharpe, Sortino, max drawdown, Calmar, profit factor, expectancy, VaR/CVaR, in-sample/out-of-sample split, bootstrap confidence interval, cost stress test.

## What's inside
| Path | Purpose |
|---|---|
| `skills/quantforge-ai/` | Core skill (`SKILL.md`), reference docs, `scripts/metrics.py` |
| `commands/` | `/create-agent`, `/strategy`, `/validate`, `/risk-check`, `/metrics` |
| `agents/` | `overfitting-detector` and `risk-manager` adversarial reviewers |
| `AGENTS.md` | Instructions for Codex and other agent tools |
| `tests/`, `.github/workflows/ci.yml` | Tests and CI |

## Install

| Tool | How |
|---|---|
| **Claude Code** | `/plugin marketplace add abhi15724/quantforge-ai` then `/plugin install quantforge-ai@quantforge-marketplace`. Gives you the skill, slash commands and reviewer agents. |
| **Claude chat (web / desktop / mobile)** | Run `./build_skill.sh` (or download `quantforge-ai.skill` from Releases), then upload it in Claude's Skills settings. Gives you the skill; slash commands and agents are Claude Code features. |
| **OpenAI Codex** | Clone the repo or copy it into your project. Codex reads `AGENTS.md`, which points to the skill and references. Prompt: "Use QuantForge to validate this backtest." |
| **Cursor, Copilot agent, Gemini CLI, others** | Clone into your project; tools that read `AGENTS.md` pick it up. Otherwise paste `skills/quantforge-ai/SKILL.md` into custom instructions and attach the reference files when needed. |

`metrics.py` needs Python 3.9+: `pip install -r requirements.txt`.

> Platform note: where each tool stores skills and which features it supports changes over time. If a step differs in your version, the portable fallback is always: give the tool `SKILL.md` and the `references/` files.

## Examples
```
/create-agent BANK NIFTY weekly options, intraday
/strategy NIFTY futures mean reversion, 15m
/validate <paste your backtest or attach returns.csv>
/risk-check <paste your bot's risk logic>
/metrics returns.csv 252 2
```
CSV format: `ret` column (periodic returns, 0.002 = 0.2%) or `pnl` column (per-trade P&L as a fraction of capital).

## Coverage
Quant research, statistical arbitrage and pairs trading, mean reversion, momentum, trend following, options and volatility strategies (Greeks, IV rank, skew, term structure, open interest, PCR), futures basis and carry, market microstructure and execution, crypto perpetuals (funding, basis, liquidations), forex carry, commodity curves, portfolio optimization (risk parity, volatility targeting, VaR/CVaR), walk-forward testing, Monte Carlo simulation, and low-latency architecture research.

## Indian-market note
Lot sizes, expiry days, STT and charges, margin rules and algo-trading regulations change. The plugin verifies current values instead of using memory. Check them yourself before acting.

## Contributing
Issues and PRs welcome. Keep the core rules: no fabricated data, no profit guarantees, risk before return. Run `pytest -q` before submitting.

## License
MIT. See `LICENSE`.
