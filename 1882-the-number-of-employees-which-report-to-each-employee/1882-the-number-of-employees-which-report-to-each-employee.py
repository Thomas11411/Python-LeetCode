import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    round0 = lambda x: round(x + 0.0001, 0)
    df = employees.groupby("reports_to").agg(
        reports_count = ("reports_to", "count"),
        average_age = ("age", lambda x: round0(np.mean(x)))
    ).reset_index()

    result = pd.merge(employees, df, left_on = "employee_id", right_on = "reports_to")[["employee_id", "name", "reports_count", "average_age"]]
    result = result.sort_values("employee_id")
    return result