# stock-timeseries-toolkit

A clean, portfolio-friendly toolkit for exploring stock-like time series using **Pandas** and **Matplotlib**. 
No course text or proprietary files. Runs standalone with included synthetic sample data.

## Features
- **plot**: plot one or more columns over time (open/high/low/close/volume).
- **compare**: overlay two columns on the same axes (e.g., Close vs. Adj Close).
- **returns**: compute and plot simple daily % returns for a column.
- **ma**: overlay moving averages (e.g., 20 and 50) on the chosen column.
- Smart monthly date ticks with rotation to avoid label overlap.
- Saves figures to `out/`.

## Quick start
```bash
pip install -r requirements.txt
python -m stock_timeseries_toolkit --help
```

### Examples (using included sample CSV)
```bash
# 1) Plot Close
python -m stock_timeseries_toolkit plot   --csv examples/sample_stock.csv --date-col date --cols Close --out out/close.png

# 2) Compare Close and AdjClose
python -m stock_timeseries_toolkit compare   --csv examples/sample_stock.csv --date-col date --col-a Close --col-b AdjClose   --out out/compare.png

# 3) Daily returns of Close
python -m stock_timeseries_toolkit returns   --csv examples/sample_stock.csv --date-col date --col Close --out out/returns.png

# 4) Moving averages on Close
python -m stock_timeseries_toolkit ma   --csv examples/sample_stock.csv --date-col date --col Close --windows 20 50   --out out/ma.png
```

## CSV format
A date column and one or more numeric columns. See `examples/sample_stock.csv`.

## Notes
- Pure Matplotlib (no seaborn). One figure per command.
- No certification banners or course HTML included.
- MIT licensed.
