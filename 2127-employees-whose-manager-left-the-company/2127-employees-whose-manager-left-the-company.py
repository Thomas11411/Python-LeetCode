import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees[(employees.salary < 30000) & (~pd.isna(employees.manager_id))]
    result = pd.merge(employees, df, left_on = "employee_id", right_on = "manager_id", how = "right").reset_index()
    result = pd.DataFrame(result.loc[pd.isna(result.employee_id_x), "employee_id_y"]).rename(columns = {"employee_id_y": "employee_id"}).sort_values("employee_id")
    return result