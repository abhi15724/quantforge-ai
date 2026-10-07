"""Smoke tests for scripts/metrics.py. Uses tiny synthetic inputs ONLY to test the code, never as market data."""
import json, subprocess, sys, pathlib
import numpy as np, pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "quantforge-ai" / "scripts" / "metrics.py"
sys.path.insert(0, str(SCRIPT.parent))
import metrics  # noqa: E402


def test_known_drawdown_and_total_return():
    p = metrics.perf([0.10, -0.50], 252)
    assert abs(p["max_drawdown"] - (-0.50)) < 1e-9
    assert abs(p["total_return"] - (1.1 * 0.5 - 1)) < 1e-9


def test_cli_end_to_end(tmp_path):
    rng = np.random.default_rng(0)
    f = tmp_path / "r.csv"
    pd.DataFrame({"ret": rng.normal(0.0003, 0.01, 300)}).to_csv(f, index=False)
    out = subprocess.run([sys.executable, str(SCRIPT), "--returns", str(f), "--cost-bps", "1"],
                         capture_output=True, text=True, check=True).stdout
    rep = json.loads(out)
    for k in ("full", "in_sample", "out_of_sample", "bootstrap", "cost_stress_2x_sharpe"):
        assert k in rep
    assert rep["in_sample"]["n"] + rep["out_of_sample"]["n"] == 300


def test_missing_column_says_data_required(tmp_path):
    f = tmp_path / "bad.csv"
    pd.DataFrame({"x": [1, 2, 3]}).to_csv(f, index=False)
    r = subprocess.run([sys.executable, str(SCRIPT), "--returns", str(f)], capture_output=True, text=True)
    assert r.returncode != 0 and "DATA REQUIRED" in (r.stderr + r.stdout)
