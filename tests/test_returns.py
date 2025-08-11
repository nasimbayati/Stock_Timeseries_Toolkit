import pandas as pd
from stock_timeseries_toolkit.utils import load_df

def test_load_df_index_sorted(tmp_path):
    p = tmp_path / "x.csv"
    p.write_text("date,Close\n2024-01-02,2\n2024-01-01,1\n")
    df = load_df(str(p), "date")
    assert list(df.index.astype(str)) == ["2024-01-01", "2024-01-02"]
