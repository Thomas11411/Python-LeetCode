import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.groupby(["emp_id", "event_day"]).apply(
        lambda g: pd.Series({
            'total_time': sum((g["out_time"] - g["in_time"]))
        })
    ).reset_index()[["event_day", "emp_id", 'total_time']].rename(columns = {"event_day": "day"})