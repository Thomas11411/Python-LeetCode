import pandas as pd

def find_product_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    from collections import Counter

    product_info = product_info[["product_id", "category"]]
    df = pd.merge(product_purchases, product_purchases, on = 'user_id')
    rows = Counter(zip(df.product_id_x, df.product_id_y)).items()
    data = [(p1,p2, cnt) for (p1, p2), cnt in rows if p1 < p2 and cnt >= 3]

    result = pd.DataFrame(data, columns = ["product1_id", "product2_id",  "customer_count"])
    result = pd.merge(result, product_info, left_on = "product1_id", right_on = "product_id", how = "left")
    result = pd.merge(result, product_info, left_on = "product2_id", right_on = "product_id", how = "left")
    result = result[["product1_id", "product2_id", "category_x", "category_y", "customer_count"]]
    result = result.rename(columns = {'category_x': 'product1_category', 'category_y': 'product2_category'}).sort_values(by = ["customer_count", "product1_id", "product2_id"], ascending=[False, True, True])
    return result