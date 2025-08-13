import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    df = stocks.groupby(["stock_name", "operation"]).agg(
        price = ("price", "sum")
    ).reset_index()

    df = df.pivot(columns = "operation", index = "stock_name", values = "price").reset_index().fillna(0)
    df["capital_gain_loss"] = df.Sell - df.Buy
    df = df[["stock_name", "capital_gain_loss"]]
    return df