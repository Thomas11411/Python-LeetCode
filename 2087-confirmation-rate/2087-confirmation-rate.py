import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    signups = signups[['user_id']]
    confirmations = confirmations[['user_id', 'action']]
    df_total = confirmations.groupby("user_id")["action"].count().reset_index()
    df_confirm = confirmations[confirmations.action == 'confirmed'].groupby("user_id")["action"].count().reset_index()
    result = pd.merge(df_confirm, df_total, on = "user_id", how = "outer")
    result = pd.merge(result, signups, on = "user_id", how = "outer")
    result["confirmation_rate"] = (result.action_x / result.action_y).round(2)
    result = result[["user_id","confirmation_rate"]]
    result = result.fillna(0)
    return result