import pandas as pd

def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    def check(ip):
        tmp = ip.split(".")
        if((len(tmp) != 4) | any(map(lambda x: (x[0] == "0") | (int(x) > 255), tmp))): return True
        return False

    df = logs.groupby("ip").agg(
        invalid_count=('ip', 'count')
    ).reset_index()
    df = df.loc[df["ip"].apply(check)]
    df = df.sort_values(by=['invalid_count', 'ip'], ascending=False)
    return df