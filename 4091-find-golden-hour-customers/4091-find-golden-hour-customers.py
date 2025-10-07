import pandas as pd

def find_golden_hour_customers(restaurant_orders: pd.DataFrame) -> pd.DataFrame:
    # 建立 DataFrame（假設已存在 restaurant_orders）
    restaurant_orders['order_timestamp'] = pd.to_datetime(restaurant_orders['order_timestamp'])

    # 取時間部分（以 timedelta 表示）
    restaurant_orders['time'] = pd.to_timedelta(restaurant_orders['order_timestamp'].dt.strftime('%H:%M:%S'))

    # 定義時段邊界
    t11, t14, t18, t21 = (pd.to_timedelta('11:00:00'), pd.to_timedelta('14:00:00'),
                        pd.to_timedelta('18:00:00'), pd.to_timedelta('21:00:00'))

    # 判斷是否為用餐尖峰時間
    is_peak = lambda x: ((t11 <= x) & (x <= t14)) | ((t18 <= x) & (x <= t21))

    df = restaurant_orders.groupby(["customer_id"]).agg(
        total_orders = ("order_timestamp", "count"),
        total_peaks = ('time', lambda x: is_peak(x).sum()),
        na_cnt = ("order_rating", lambda x: x.isna().sum()),
        average_rating = ("order_rating", "mean")
    ).reset_index()

    df["peak_hour_percentage"] = (100 * df["total_peaks"] / df["total_orders"]).round(0)
    df["average_rating"] = df["average_rating"].round(2)
    df = df.loc[(df["peak_hour_percentage"] >= 60) & (df["total_orders"] >= 3) & (df["average_rating"] >= 4) & (df["total_orders"] >= 2 * df["na_cnt"]), ['customer_id', 'total_orders', 'peak_hour_percentage', 'average_rating']]
    return df.sort_values(["average_rating", "customer_id"], ascending = [False, False])
