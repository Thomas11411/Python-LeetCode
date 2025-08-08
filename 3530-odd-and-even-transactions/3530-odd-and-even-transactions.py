import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    even_data = transactions.loc[transactions.amount % 2 == 0].groupby(["transaction_date"]).agg(even_sum = ("amount", "sum")).reset_index()
    odd_data = transactions.loc[transactions.amount % 2 == 1].groupby(["transaction_date"]).agg(odd_sum = ("amount", "sum")).reset_index()

    result = pd.merge(odd_data, even_data, on = "transaction_date", how = "outer").fillna(0).sort_values(by = ["transaction_date"], ascending=[True])
    return result