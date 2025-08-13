import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    pivot_data = activity.pivot(index=["machine_id", "process_id"], columns='activity_type', values='timestamp').reset_index()
    pivot_data["diff_time"] = pivot_data["end"] - pivot_data["start"]
    result = pivot_data.groupby("machine_id").agg(
        processing_time = ("diff_time", "mean")
    ).reset_index().round(3)
    return result