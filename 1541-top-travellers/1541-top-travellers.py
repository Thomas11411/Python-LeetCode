import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    df = rides.groupby("user_id").agg(
        travelled_distance = ("distance", "sum")
    ).reset_index()

    result = pd.merge(users, df, left_on = "id", right_on = "user_id", how = "left").fillna(0)[["name", "travelled_distance"]]
    result = result.sort_values(by = ["travelled_distance", "name"], ascending = [False, True])
    return result