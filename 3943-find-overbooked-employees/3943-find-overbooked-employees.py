import pandas as pd

def find_overbooked_employees(employees: pd.DataFrame, meetings: pd.DataFrame) -> pd.DataFrame:
    from datetime import datetime

    meetings["week"] = meetings["meeting_date"].apply(lambda d: d.isocalendar()[1])
    sum_data = meetings.groupby(['employee_id', 'week'])['duration_hours'].sum().reset_index()
    sum_data = sum_data.loc[sum_data["duration_hours"] > 20]
    sum_data = sum_data.groupby(['employee_id'])['week'].count().reset_index(name = "meeting_heavy_weeks")
    sum_data = sum_data.loc[sum_data['meeting_heavy_weeks'] >= 2][["employee_id", "meeting_heavy_weeks"]]

    result = pd.merge(employees, sum_data, on = 'employee_id', how = "inner")
    result = result.sort_values(by=['meeting_heavy_weeks', 'employee_name'], ascending=[False, True])
    return result