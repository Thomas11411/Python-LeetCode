import pandas as pd

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    scores["exam_date"] = pd.to_datetime(scores["exam_date"])
    scores = scores.sort_values(["student_id", "subject", "exam_date"])
    df = scores.groupby(["student_id", "subject"]).agg(first_score = ("score", "first"), latest_score = ("score", "last")).reset_index()
    df = df[df["latest_score"] - df["first_score"] > 0]
    return df