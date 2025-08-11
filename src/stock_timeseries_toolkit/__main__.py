import argparse
from .plot_cmd import plot_cli, plot_entry
from .compare_cmd import compare_cli, compare_entry
from .returns_cmd import returns_cli, returns_entry
from .ma_cmd import ma_cli, ma_entry

def main():
    parser = argparse.ArgumentParser(prog="stock_timeseries_toolkit", description="Explore stock-like time series from CSV.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    plot_cli(sub)
    compare_cli(sub)
    returns_cli(sub)
    ma_cli(sub)

    args = parser.parse_args()
    if args.cmd == "plot":
        plot_entry(args)
    elif args.cmd == "compare":
        compare_entry(args)
    elif args.cmd == "returns":
        returns_entry(args)
    elif args.cmd == "ma":
        ma_entry(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
