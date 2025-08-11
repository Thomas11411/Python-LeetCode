import pandas as pd

def find_polarized_books(books: pd.DataFrame, reading_sessions: pd.DataFrame) -> pd.DataFrame:
    round2 = lambda x: round(x + 0.0001, 2)
    result = reading_sessions.groupby("book_id").agg(
        cnt = ("book_id", "count"),
        rating_spread = ("session_rating", lambda x: max(x) - min(x)),
        polarization_cnt =  ("session_rating", lambda x: sum((x <= 2) | (x >= 4))),
        high_polarization = ("session_rating", lambda x: sum((x >= 4))),
        low_polarization = ("session_rating", lambda x: sum((x <= 2)))
    ).reset_index()


    result["polarization_score"] = (result.polarization_cnt / result.cnt).apply(round2)
    result = result.loc[(result.cnt >= 5) & (result.polarization_score >= 0.6) & (result.low_polarization > 0) & (result.high_polarization > 0), ["book_id", "rating_spread", "polarization_score"]]
    result = pd.merge(books, result, on = "book_id", how = "right")
    result = result.sort_values(by = ["polarization_score", "title"], ascending=False)
    return result