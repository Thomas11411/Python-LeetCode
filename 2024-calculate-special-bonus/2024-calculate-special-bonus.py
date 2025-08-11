import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    result = employees.copy()
    result.loc[(result.employee_id % 2 == 0) | (list(map(lambda n: n[0] == "M", result.name))), "salary"] = 0
    result = result[["employee_id", "salary"]].rename(columns = {"salary": "bonus"}).sort_values("employee_id")
    return result