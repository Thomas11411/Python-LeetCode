import pandas as pd

def find_covid_recovery_patients(patients: pd.DataFrame, covid_tests: pd.DataFrame) -> pd.DataFrame:
    covid_tests["test_date"] = pd.to_datetime(covid_tests["test_date"])

    P_data = covid_tests[covid_tests["result"] == "Positive"].rename(columns = {'test_date': 'Pos_date'})
    N_data = covid_tests[covid_tests["result"] == "Negative"].rename(columns = {'test_date': 'Neg_date'})

    merged = pd.merge(P_data, N_data, on = 'patient_id')
    merged = merged.loc[merged["test_id_y"] > merged["test_id_x"]]
    merged["recovery_time"] = (merged["Neg_date"] - merged["Pos_date"]).dt.days
    merged = merged.loc[merged.groupby('test_id_x')["recovery_time"].idxmin()]
    merged = merged.loc[merged.groupby('test_id_y')["recovery_time"].idxmax()]
    merged = merged.loc[merged.groupby("patient_id")['test_id_x'].idxmin(),["patient_id", "recovery_time"]]
    result = pd.merge(patients, merged, on = 'patient_id', how = "inner")
    result = result.sort_values(by=['recovery_time', 'patient_name'], ascending=[True, True])
    return result