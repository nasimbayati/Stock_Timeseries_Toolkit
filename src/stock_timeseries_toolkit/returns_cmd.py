import matplotlib.pyplot as plt
from .utils import load_df, smart_date_ticks, save_fig

def returns_cli(subparsers):
    sp = subparsers.add_parser("returns", help="Compute and plot daily percent returns of a column.")
    sp.add_argument("--csv", required=True)
    sp.add_argument("--date-col", required=True)
    sp.add_argument("--col", required=True)
    sp.add_argument("--start", default=None)
    sp.add_argument("--end", default=None)
    sp.add_argument("--out", default=None)
    return sp

def returns_entry(args):
    df = load_df(args.csv, args.date_col)
    if args.start:
        df = df.loc[args.start:]
    if args.end:
        df = df.loc[:args.end]
    r = df[args.col].pct_change() * 100.0
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    r.plot(ax=ax)
    ax.set_title(f"Daily Returns of {args.col} (%)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Percent")
    ax.grid(True)
    smart_date_ticks(ax, r.index)
    path = save_fig(fig, args.out, "returns.png")
    print(f"Wrote: {path}")
