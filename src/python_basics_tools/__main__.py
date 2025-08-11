import argparse
from .stats_cli import stats_cli, stats_entry
from .hist_cli import hist_cli, hist_entry
from .dist_cli import dist_cli, dist_entry
from .grades_cli import grades_cli, grades_entry

def main():
    parser = argparse.ArgumentParser(prog="python_basics_tools", description="Python basics turned into useful tools.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    stats_cli(sub)
    hist_cli(sub)
    dist_cli(sub)
    grades_cli(sub)

    args = parser.parse_args()
    if args.cmd == "stats":
        stats_entry(args)
    elif args.cmd == "hist":
        hist_entry(args)
    elif args.cmd == "dist":
        dist_entry(args)
    elif args.cmd == "grades":
        grades_entry(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
