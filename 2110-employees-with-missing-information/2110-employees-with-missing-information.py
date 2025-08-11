import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(employees, salaries, how = "outer")
    result = result.loc[result.name.isna() | result.salary.isna(), ["employee_id"]].sort_values('employee_id')
    return result