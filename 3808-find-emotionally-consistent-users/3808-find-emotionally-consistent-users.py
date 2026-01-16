import pandas as pd

def find_emotionally_consistent_users(reactions: pd.DataFrame) -> pd.DataFrame:
    round2 = lambda x: round(x + 0.0001, 2)

    df = reactions.groupby(["user_id", "reaction"]).agg(
        cnt = ("reaction", "count")
    ).reset_index()

    top_reaction = (
        df.loc[df.groupby("user_id")["cnt"].idxmax()]
    ).reset_index()[["user_id", "reaction"]]

    res = df.groupby(["user_id"]).agg(
        total = ("cnt", "sum"),
        max_cnt = ("cnt", "max"),
    ).reset_index()

    res["reaction_ratio"] = (res["max_cnt"] / res["total"]).apply(round2)

    res = pd.merge(res, top_reaction, on = "user_id", how = "left")
    res = res.loc[(res.reaction_ratio > 0.6) & (res.total >= 5)]
    res = res.sort_values(by = ["reaction_ratio", "user_id"], ascending = [False, True])[["user_id", "reaction", "reaction_ratio"]]
    res.rename(columns = {"reaction": "dominant_reaction"}, inplace=True)
    return res