import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    right = examinations.groupby(["student_id", "subject_name"]).agg(
        attended_exams = ("student_id", "count")
    ).reset_index()

    left = pd.merge(students, subjects, how = "cross")

    result = pd.merge(left, right, on = ["student_id", "subject_name"], how = "left").fillna(0)
    result = result.sort_values(["student_id", "subject_name"])
    result.loc[result["student_name"] == 0, "student_name"] = None
    return result