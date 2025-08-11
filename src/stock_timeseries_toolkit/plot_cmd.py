import matplotlib.pyplot as plt
from .utils import load_df, smart_date_ticks, save_fig

def plot_cli(subparsers):
    sp = subparsers.add_parser("plot", help="Plot one or more columns over time.")
    sp.add_argument("--csv", required=True)
    sp.add_argument("--date-col", required=True)
    sp.add_argument("--cols", nargs="+", required=True, help="Columns to plot (space-separated).")
    sp.add_argument("--start", default=None, help="Start date YYYY-MM-DD")
    sp.add_argument("--end", default=None, help="End date YYYY-MM-DD")
    sp.add_argument("--out", default=None)
    return sp

def plot_entry(args):
    df = load_df(args.csv, args.date_col)
    if args.start:
        df = df.loc[args.start:]
    if args.end:
        df = df.loc[:args.end]
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    df[args.cols].plot(ax=ax)
    ax.set_title("Time Series Plot")
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.grid(True)
    smart_date_ticks(ax, df.index)
    path = save_fig(fig, args.out, "plot.png")
    print(f"Wrote: {path}")
