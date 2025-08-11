import matplotlib.pyplot as plt
from .utils import load_df, smart_date_ticks, save_fig

def ma_cli(subparsers):
    sp = subparsers.add_parser("ma", help="Overlay moving averages on a column.")
    sp.add_argument("--csv", required=True)
    sp.add_argument("--date-col", required=True)
    sp.add_argument("--col", required=True)
    sp.add_argument("--windows", nargs="+", type=int, required=True, help="MA windows, e.g., 20 50")
    sp.add_argument("--start", default=None)
    sp.add_argument("--end", default=None)
    sp.add_argument("--out", default=None)
    return sp

def ma_entry(args):
    df = load_df(args.csv, args.date_col)
    if args.start:
        df = df.loc[args.start:]
    if args.end:
        df = df.loc[:args.end]
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    df[args.col].plot(ax=ax, label=args.col)
    for w in args.windows:
        df[args.col].rolling(window=w, min_periods=1).mean().plot(ax=ax, label=f"MA{w}")
    ax.set_title(f"{args.col} with Moving Averages")
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.grid(True)
    smart_date_ticks(ax, df.index)
    ax.legend(loc="best")
    path = save_fig(fig, args.out, "ma.png")
    print(f"Wrote: {path}")
