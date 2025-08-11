import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    l_a = sum((accounts['income'] < 20000))
    a_a = sum((accounts['income'] >= 20000) & (accounts['income'] <= 50000))
    h_a = sum((accounts['income'] > 50000))

    result = pd.DataFrame(
        {"category": ["Low Salary", "Average Salary", "High Salary"],
        "accounts_count": [l_a, a_a, h_a]
        }
    )
    return result