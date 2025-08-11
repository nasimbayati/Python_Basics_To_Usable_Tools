from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def hist_cli(subparsers):
    sp = subparsers.add_parser("hist", help="Create a histogram from a CSV column.")
    sp.add_argument("--csv", required=True)
    sp.add_argument("--col", required=True)
    sp.add_argument("--bins", type=int, default=10)
    sp.add_argument("--out", default="out/hist.png")
    return sp

def hist_entry(args):
    df = pd.read_csv(args.csv)
    s = pd.to_numeric(df[args.col], errors="coerce").dropna()
    fig, ax = plt.subplots(1,1, figsize=(7,5))
    ax.hist(s.values, bins=args.bins)
    ax.set_title(f"Histogram of {args.col}")
    ax.set_xlabel(args.col)
    ax.set_ylabel("Frequency")
    ax.grid(True)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(args.out, bbox_inches="tight")
    print(f"Wrote: {args.out}")
