import pandas as pd

def find_consistently_improving_employees(employees: pd.DataFrame, performance_reviews: pd.DataFrame) -> pd.DataFrame:
    performance_reviews["rank"] = performance_reviews.groupby(["employee_id"])["review_date"].rank(ascending=False)
    df = performance_reviews[performance_reviews["rank"] <= 3]
    df = df.pivot(index = "employee_id", columns = "rank", values = "rating").reset_index()
    df = df.dropna().loc[(df[1] > df[2]) & (df[2] > df[3])]
    df['improvement_score'] = df[1] - df[3]
    df = df.drop([1,2,3], axis=1)
    result = pd.merge(employees, df, on = "employee_id", how = "inner").sort_values(by = ["improvement_score", "name"], ascending=[False, True])
    return result