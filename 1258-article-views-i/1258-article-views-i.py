import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views[views.author_id == views.viewer_id].groupby("author_id").agg(
    cnt = ("author_id", "count")
).reset_index()[["author_id"]].rename(columns = {"author_id": "id"}).sort_values("id")