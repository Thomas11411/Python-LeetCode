import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders.order_date = pd.to_datetime(orders.order_date)

    df = orders[orders.order_date.dt.year == 2019].groupby("buyer_id").agg(
        orders_in_2019 = ("buyer_id", "count")
    ).reset_index()

    result = pd.merge(users, df, left_on = "user_id", right_on = "buyer_id", how = "left")[["user_id", "join_date", "orders_in_2019"]].fillna(0)
    result = result.rename(columns = {"user_id": "buyer_id"})
    return result