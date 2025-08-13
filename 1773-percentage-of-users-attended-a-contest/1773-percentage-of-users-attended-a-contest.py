import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    result = register.groupby("contest_id").agg(
        cnt = ("user_id", "nunique")
    ).reset_index()

    result["percentage"] = (result.cnt / len(users.user_id) * 100).round(2)
    result = result[["contest_id", "percentage"]].sort_values(by=["percentage", "contest_id"], ascending=[False, True])
    return result