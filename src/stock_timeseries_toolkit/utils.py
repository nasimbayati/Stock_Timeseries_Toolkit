from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def load_df(csv_path: str, date_col: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df[date_col] = pd.to_datetime(df[date_col])
    return df.sort_values(date_col).set_index(date_col)

def smart_date_ticks(ax, index):
    if len(index) == 0:
        return
    start = pd.to_datetime(index[0])
    end = pd.to_datetime(index[-1])
    span_days = (end - start).days
    if span_days <= 120:
        locator = mdates.MonthLocator(interval=1)
    elif span_days <= 365:
        locator = mdates.MonthLocator(interval=2)
    else:
        locator = mdates.MonthLocator(interval=3)
    formatter = mdates.DateFormatter('%b %Y')
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    for label in ax.get_xticklabels():
        label.set_rotation(45)
        label.set_ha('right')

def ensure_out():
    Path("out").mkdir(exist_ok=True, parents=True)

def save_fig(fig, out: str | None, default_name: str) -> str:
    ensure_out()
    out_path = out or f"out/{default_name}"
    fig.tight_layout()
    fig.savefig(out_path, bbox_inches="tight")
    return out_path
