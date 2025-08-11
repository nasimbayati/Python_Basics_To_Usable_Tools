from pathlib import Path
import json
import pandas as pd

def stats_cli(subparsers):
    sp = subparsers.add_parser("stats", help="Compute basic statistics for a CSV column.")
    sp.add_argument("--csv", required=True)
    sp.add_argument("--col", required=True)
    sp.add_argument("--out", default="out/stats.json")
    return sp

def stats_entry(args):
    df = pd.read_csv(args.csv)
    s = pd.to_numeric(df[args.col], errors="coerce").dropna()
    result = {
        "count": int(s.count()),
        "mean": float(s.mean()),
        "median": float(s.median()),
        "mode": [float(x) for x in s.mode().tolist()],
        "std": float(s.std(ddof=1)),
        "min": float(s.min()),
        "max": float(s.max())
    }
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w") as f:
        json.dump(result, f, indent=2)
    print(f"Wrote: {args.out}")
