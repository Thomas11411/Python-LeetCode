import pandas as pd

def find_loyal_customers(customer_transactions: pd.DataFrame) -> pd.DataFrame:
    customer_transactions["transaction_date"] = pd.to_datetime(customer_transactions["transaction_date"])

    df = customer_transactions.groupby("customer_id").agg(
        transactions_count = ("customer_id", "count"),
        purchase_count = ("transaction_type", lambda x: sum(x == "purchase")),
        refund_count = ("transaction_type", lambda x: sum(x == "refund")),
        date_max = ("transaction_date", "max"),
        date_min = ("transaction_date", "min")
    ).reset_index()

    return df.loc[(df["purchase_count"] >= 3) & ((df["date_max"] - df["date_min"]).dt.days >= 30) & ((df["refund_count"] / df["transactions_count"]) < 0.2), ["customer_id"]].sort_values("customer_id")