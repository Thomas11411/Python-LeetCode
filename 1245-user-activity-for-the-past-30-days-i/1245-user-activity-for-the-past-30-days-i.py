import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    activity["activity_date"] = pd.to_datetime(activity["activity_date"])

    df = activity[activity["activity_date"].between("2019-06-28", "2019-07-27")]
    df = df.groupby(["activity_date"])['user_id'].nunique().reset_index().rename(columns = {"activity_date": "day", "user_id": "active_users"})
    return df