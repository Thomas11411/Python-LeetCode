import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery = delivery.sort_values("order_date")

    df = delivery.groupby(["customer_id"]).first().reset_index()
    result = pd.DataFrame({
        "immediate_percentage": [round(100 * sum(df.order_date == df.customer_pref_delivery_date) / df.shape[0], 2)]
    })
    return result