import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    return followers.groupby("user_id").agg(
        followers_count = ("follower_id", lambda x: len(set(x)))
    ).reset_index().sort_values("user_id")