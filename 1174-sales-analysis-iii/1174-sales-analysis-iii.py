import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    sales["sale_date"] = pd.to_datetime(sales["sale_date"])
    df = sales.groupby(['product_id']).agg(min=('sale_date', 'min'), max=('sale_date', 'max')).reset_index()
    df = df[(df["min"] >= pd.to_datetime("2019-01-01")) & (df["max"] <= pd.to_datetime("2019-03-31"))]["product_id"]
    return pd.merge(product, df, how = "right")[["product_id", "product_name"]]