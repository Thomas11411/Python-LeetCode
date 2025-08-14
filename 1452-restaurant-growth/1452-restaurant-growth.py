import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    customer.visited_on = pd.to_datetime(customer.visited_on)
    #customer = customer.set_index("visited_on")
    df = customer.sort_values("visited_on").groupby("visited_on")[["amount"]].sum().reset_index()
    rolling_sum = df.rolling("7D", on="visited_on")["amount"].sum()
    rolling_avg = (rolling_sum / 7).round(2)
    rolling_day = df.rolling("7D", on="visited_on")["amount"].count()

    df = df.assign(amount = rolling_sum, average_amount = rolling_avg)
    df = df[rolling_day == 7]
    df = df.sort_values("visited_on")
    return df