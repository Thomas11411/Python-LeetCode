import pandas as pd

def find_inventory_imbalance(stores: pd.DataFrame, inventory: pd.DataFrame) -> pd.DataFrame:
    # 最貴商品
    max_price = inventory.loc[
        inventory.groupby('store_id')['price'].idxmax(),
        ['store_id', 'product_name', 'quantity']
    ].rename(columns={'product_name': 'most_exp_product', 'quantity': 'most_exp_qty'})

    # 最便宜商品
    min_price = inventory.loc[
        inventory.groupby('store_id')['price'].idxmin(),
        ['store_id', 'product_name', 'quantity']
    ].rename(columns={'product_name': 'cheapest_product', 'quantity': 'cheapest_qty'})

    # 合併 max/min
    merged = pd.merge(max_price, min_price, on='store_id')

    # 計算 imbalance_ratio（只有最貴商品數量 < 最便宜商品數量 才保留）
    merged = merged[merged['most_exp_qty'] < merged['cheapest_qty']]
    merged['imbalance_ratio'] = (merged['cheapest_qty'] / merged['most_exp_qty']).round(2)

    # 計算每個 store 有幾種產品
    product_cnt = inventory.groupby('store_id')['product_name'].nunique().reset_index(name='product_count')
    merged = pd.merge(merged, product_cnt, on='store_id')
    merged = merged[merged['product_count'] >= 3]

    # 合併商店資訊
    result = pd.merge(stores, merged, on='store_id')

    # 排序與選取欄位
    result = result.sort_values(by=['imbalance_ratio', 'store_name'], ascending=[False, True])
    return result[['store_id', 'store_name', 'location', 'most_exp_product', 'cheapest_product', 'imbalance_ratio']]