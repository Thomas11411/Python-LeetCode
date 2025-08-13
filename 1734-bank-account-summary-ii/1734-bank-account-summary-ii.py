import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = transactions.groupby("account").agg(
        balance = ("amount", "sum")
    ).reset_index()
    df = df.loc[df.balance > 10000]
    result = pd.merge(users, df, on = "account", how = "right")[["name", "balance"]]
    return result