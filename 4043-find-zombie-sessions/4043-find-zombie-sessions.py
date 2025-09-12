import pandas as pd

def find_zombie_sessions(app_events: pd.DataFrame) -> pd.DataFrame:
    app_events["event_timestamp"] = pd.to_datetime(app_events["event_timestamp"])
    df = app_events.groupby(['session_id', "user_id"]).agg(
        purchase_count = ("event_type", lambda x: sum(x == "purchase")),
        scroll_count = ("event_type", lambda x: sum(x == "scroll")),
        click_count = ("event_type", lambda x: sum(x == "click")),
        min_time = ("event_timestamp", "min"),
        max_time = ("event_timestamp", "max")
    ).reset_index()

    df["session_duration_minutes"] = (df.max_time - df.min_time).dt.seconds / 60

    df = df.loc[(df.session_duration_minutes > 30) & (df.purchase_count == 0) & (5 * df.click_count < df.scroll_count) & (df.scroll_count >= 5), ["session_id",  "user_id", "session_duration_minutes", "scroll_count"]].sort_values(['scroll_count','session_id'], ascending = [False, True])
    return df