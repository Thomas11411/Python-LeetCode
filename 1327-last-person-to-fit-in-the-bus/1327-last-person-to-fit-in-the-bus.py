import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    import numpy as np

    queue = queue.sort_values("turn")
    return queue.loc[np.cumsum(queue.weight) <= 1000, ["person_name"]].tail(1)