import pandas as pd

def find_emotionally_consistent_users(reactions: pd.DataFrame) -> pd.DataFrame:
    round2 = lambda x: round(x + 0.0001, 2)

    df = reactions.groupby(["user_id", "reaction"]).agg(
        cnt = ("reaction", "count")
    ).reset_index()

    res = (
        df.groupby("user_id", as_index=False)
        .apply(lambda g: pd.Series({
            "total": g["cnt"].sum(),
            "max_cnt": g["cnt"].max(),
            "dominant_reaction": g.loc[g["cnt"].idxmax(), "reaction"]
        }))
    )

    res["reaction_ratio"] = (res["max_cnt"] / res["total"]).apply(round2)

    res = res.loc[(res.reaction_ratio > 0.6) & (res.total >= 5)]
    res = res.sort_values(by = ["reaction_ratio", "user_id"], ascending = [False, True])[["user_id", "dominant_reaction", "reaction_ratio"]]
    return res