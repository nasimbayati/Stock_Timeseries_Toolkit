import matplotlib.pyplot as plt
from .utils import load_df, smart_date_ticks, save_fig

def compare_cli(subparsers):
    sp = subparsers.add_parser("compare", help="Overlay two columns on the same axes.")
    sp.add_argument("--csv", required=True)
    sp.add_argument("--date-col", required=True)
    sp.add_argument("--col-a", required=True)
    sp.add_argument("--col-b", required=True)
    sp.add_argument("--start", default=None)
    sp.add_argument("--end", default=None)
    sp.add_argument("--out", default=None)
    return sp

def compare_entry(args):
    df = load_df(args.csv, args.date_col)
    if args.start:
        df = df.loc[args.start:]
    if args.end:
        df = df.loc[:args.end]
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    df[[args.col_a, args.col_b]].plot(ax=ax)
    ax.set_title(f"Compare {args.col_a} vs {args.col_b}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.grid(True)
    smart_date_ticks(ax, df.index)
    ax.legend(loc="best")
    path = save_fig(fig, args.out, "compare.png")
    print(f"Wrote: {path}")
