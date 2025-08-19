import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(project, employee, on = "employee_id", how = "left")
    result = df.groupby("project_id").agg(
        average_years = ("experience_years", "mean")
    ).reset_index().round(2)
    return result