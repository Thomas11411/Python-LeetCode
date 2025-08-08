import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    result = users.copy()
    result = result.loc[list(map(lambda e: "@" in e and e[-4:] == ".com", result.email))]
    result = result.loc[map(lambda e: e[:e.find("@")].isalnum() and e[(e.find("@")+1):e.find(".com")].isalpha(), result.email)]
    return result