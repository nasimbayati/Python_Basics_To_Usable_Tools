from pathlib import Path
import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, poisson

def dist_cli(subparsers):
    sp = subparsers.add_parser("dist", help="Plot probability distributions.")
    ssub = sp.add_subparsers(dest="dist_cmd", required=True)

    # normal
    spn = ssub.add_parser("normal", help="Normal distribution")
    spn.add_argument("--mu", type=float, required=True)
    spn.add_argument("--sigma", type=float, required=True)
    spn.add_argument("--x-min", type=float, required=True)
    spn.add_argument("--x-max", type=float, required=True)
    spn.add_argument("--out", default="out/normal.png")

    # binomial
    spb = ssub.add_parser("binomial", help="Binomial distribution")
    spb.add_argument("--n", type=int, required=True)
    spb.add_argument("--p", type=float, required=True)
    spb.add_argument("--out", default="out/binomial.png")

    # poisson
    spp = ssub.add_parser("poisson", help="Poisson distribution")
    spp.add_argument("--lam", type=float, required=True)
    spp.add_argument("--k-max", type=int, required=True)
    spp.add_argument("--out", default="out/poisson.png")

    return sp

def dist_entry(args):
    if args.dist_cmd == "normal":
        xs = np.linspace(args.x_min, args.x_max, 400)
        ys = norm.pdf(xs, loc=args.mu, scale=args.sigma)
        fig, ax = plt.subplots(1,1, figsize=(7,5))
        ax.plot(xs, ys)
        ax.set_title(f"Normal(mu={args.mu}, sigma={args.sigma})")
        ax.set_xlabel("x")
        ax.set_ylabel("PDF")
        ax.grid(True)
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        fig.tight_layout()
        fig.savefig(args.out, bbox_inches="tight")
        print(f"Wrote: {args.out}")
    elif args.dist_cmd == "binomial":
        k = np.arange(0, args.n+1)
        pmf = binom.pmf(k, args.n, args.p)
        fig, ax = plt.subplots(1,1, figsize=(7,5))
        ax.stem(k, pmf, use_line_collection=True)
        ax.set_title(f"Binomial(n={args.n}, p={args.p})")
        ax.set_xlabel("k")
        ax.set_ylabel("PMF")
        ax.grid(True)
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        fig.tight_layout()
        fig.savefig(args.out, bbox_inches="tight")
        print(f"Wrote: {args.out}")
    elif args.dist_cmd == "poisson":
        k = np.arange(0, args.k_max+1)
        pmf = poisson.pmf(k, args.lam)
        fig, ax = plt.subplots(1,1, figsize=(7,5))
        ax.stem(k, pmf, use_line_collection=True)
        ax.set_title(f"Poisson(lambda={args.lam})")
        ax.set_xlabel("k")
        ax.set_ylabel("PMF")
        ax.grid(True)
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        fig.tight_layout()
        fig.savefig(args.out, bbox_inches="tight")
        print(f"Wrote: {args.out}")
