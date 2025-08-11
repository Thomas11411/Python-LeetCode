import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    logins["time_stamp"] = pd.to_datetime(logins["time_stamp"])
    result = logins[logins.time_stamp.dt.year == 2020]
    result = result.groupby(["user_id"]).max().reset_index().rename(columns = {'time_stamp':'last_stamp'})
    return result