import pandas as pd

def find_improved_efficiency_drivers(drivers: pd.DataFrame, trips: pd.DataFrame) -> pd.DataFrame:
    trips["trip_date"] = pd.to_datetime(trips["trip_date"])
    trips["month"] = trips["trip_date"].dt.month
    trips["half"] = list(map(lambda m: "first" if m <= 6 else "second", trips["month"]))
    trips["fuel_efficiency"] = (trips["distance_km"] / trips["fuel_consumed"])

    sumdata = trips.groupby(['driver_id', 'half']).agg(
            average_efficiency=("fuel_efficiency", 'mean'),
        ).reset_index()
    sumdata.average_efficiency = sumdata.average_efficiency

    first_data = sumdata.loc[sumdata.half == "first", ['driver_id','average_efficiency']].rename(columns = {'average_efficiency': 'first_half_avg'})
    second_data = sumdata.loc[sumdata.half == "second", ['driver_id','average_efficiency']].rename(columns = {'average_efficiency': 'second_half_avg'})

    result = pd.merge(drivers, first_data, on = 'driver_id', how = "left")
    result = pd.merge(result, second_data, on = 'driver_id', how = "left")
    result = result.dropna()
    result["efficiency_improvement"] = (result.second_half_avg - result.first_half_avg)
    result = result.loc[result.efficiency_improvement > 0]
    result = result.sort_values(by=["efficiency_improvement", 'driver_name'], ascending=[False, True]).round(2)
    return result