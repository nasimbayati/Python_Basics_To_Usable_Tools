import pandas as pd
from python_basics_tools.stats_cli import stats_entry

def test_stats_entry(tmp_path, capsys):
    p = tmp_path / "x.csv"
    p.write_text("value\n1\n2\n3\n")
    class Args: 
        csv=str(p); col="value"; out=str(tmp_path / "out.json")
    stats_entry(Args())
    out = (tmp_path / "out.json").read_text()
    assert '"mean": 2.0' in out
