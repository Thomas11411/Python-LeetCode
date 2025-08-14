import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders.order_date = pd.to_datetime(orders.order_date)

    orders = orders[(orders.order_date.dt.year == 2020) & (orders.order_date.dt.month == 2)]
    df = orders.groupby("product_id").agg(
        unit = ("unit", "sum")
    ).reset_index()

    df = df[df.unit >= 100]
    result = pd.merge(products, df, on = "product_id", how = "right")[["product_name", "unit"]]
    return result