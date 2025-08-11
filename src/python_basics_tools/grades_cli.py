from pathlib import Path
import pandas as pd

def parse_scheme(s: str):
    # "90:A,80:B,70:C,60:D" -> list of (threshold, letter)
    items = []
    for part in s.split(","):
        cut, letter = part.split(":")
        items.append((float(cut), letter))
    # sort descending thresholds
    items.sort(key=lambda x: -x[0])
    return items

def assign_letter(score: float, scheme):
    for cut, letter in scheme:
        if score >= cut:
            return letter
    return "F"

def grades_cli(subparsers):
    sp = subparsers.add_parser("grades", help="Summarize grades, apply curve & letter grades.")
    sp.add_argument("--csv", required=True)
    sp.add_argument("--student-col", required=True)
    sp.add_argument("--score-col", required=True)
    sp.add_argument("--curve", type=float, default=0.0, help="Additive curve in points.")
    sp.add_argument("--scheme", default="90:A,80:B,70:C,60:D", help="Thresholds for letters.")
    sp.add_argument("--out", default="out/grades_report.csv")
    return sp

def grades_entry(args):
    df = pd.read_csv(args.csv)
    scheme = parse_scheme(args.scheme)
    # numeric scores
    s = pd.to_numeric(df[args.score_col], errors="coerce").fillna(0.0)
    curved = (s + args.curve).clip(upper=100.0)
    letters = curved.apply(lambda x: assign_letter(x, scheme))
    report = pd.DataFrame({
        args.student_col: df[args.student_col].astype(str),
        "raw_score": s,
        "curved_score": curved,
        "letter": letters
    })
    # summary
    summary = pd.DataFrame({
        "metric": ["count", "mean_raw", "mean_curved", "min", "max"],
        "value": [int(s.count()), float(s.mean()), float(curved.mean()), float(curved.min()), float(curved.max())]
    })
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    report.to_csv(args.out, index=False)
    # Also write summary next to it
    summary_path = str(Path(args.out).with_name(Path(args.out).stem + "_summary.csv"))
    summary.to_csv(summary_path, index=False)
    print(f"Wrote: {args.out}")
    print(f"Wrote: {summary_path}")
