import pandas as pd

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    round2 = lambda x: round(x + 0.0001, 2)

    UserActivity = user_activity
    UserActivity["activity_date"] = pd.to_datetime(UserActivity["activity_date"])

    sum_data = UserActivity.groupby(['user_id', 'activity_type']).agg(
            avg_duration=("activity_duration", 'mean'),
        ).reset_index()

    free = sum_data.loc[sum_data.activity_type == "free_trial", ["user_id", "avg_duration"]].rename(columns = {"avg_duration": 'trial_avg_duration'})
    paid = sum_data.loc[sum_data.activity_type == "paid", ["user_id", "avg_duration"]].rename(columns = {"avg_duration": 'paid_avg_duration'})

    result = pd.merge(free, paid, on = "user_id", how = "inner").apply(round2).sort_values(by = ["user_id"], ascending=[True])
    return result