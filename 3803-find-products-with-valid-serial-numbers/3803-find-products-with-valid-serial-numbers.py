import pandas as pd

def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:

    def check(line):
        for w in line.split():
            if all((len(w) == 11, w[0:2] == "SN",  w[2:6].isdigit(), w[6:7] == "-", w[7:11])): return True
        return False

    return products[products['description'].apply(check)].sort_values('product_id')