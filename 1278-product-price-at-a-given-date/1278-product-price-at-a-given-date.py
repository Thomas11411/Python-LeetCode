import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    products["change_date"] = pd.to_datetime(products["change_date"])
    left_data = pd.DataFrame({
        "product_id": np.unique(products.product_id)
    })

    right_data = products.loc[products["change_date"] <= "2019-08-16"].sort_values("change_date")
    right_data = right_data.loc[right_data.groupby("product_id")["change_date"].idxmax(), ["product_id", "new_price"]].rename(columns = {"new_price": "price"})
    result = pd.merge(left_data, right_data, on = "product_id", how = "left").fillna(10).sort_values("price", ascending=False)
    return result