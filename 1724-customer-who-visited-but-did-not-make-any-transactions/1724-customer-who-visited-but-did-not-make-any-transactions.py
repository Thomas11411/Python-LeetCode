import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    transactions = transactions.dropna()
    df = pd.merge(visits, transactions, on = "visit_id", how = "outer")
    result = df[df.isna().any(axis=1)].groupby("customer_id").agg(
        count_no_trans = ("customer_id", "count")
    ).reset_index()
    return result