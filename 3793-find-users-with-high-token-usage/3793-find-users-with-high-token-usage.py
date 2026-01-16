import pandas as pd

def find_users_with_high_tokens(prompts: pd.DataFrame) -> pd.DataFrame:
    df = prompts.groupby("user_id")["tokens"].agg(
        prompt_count = 'count',
        avg_tokens = "mean",
        max_tokens = "max"
    ).reset_index()

    df["avg_tokens"] = df["avg_tokens"].round(2)

    df = df.loc[(df["prompt_count"] >= 3) & (df["max_tokens"] > df["avg_tokens"]), ["user_id", "prompt_count", "avg_tokens"]]
    df = df.sort_values(["avg_tokens", "user_id"], ascending = [False, True])
    return df