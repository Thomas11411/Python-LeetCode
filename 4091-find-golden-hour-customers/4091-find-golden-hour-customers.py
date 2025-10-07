import pandas as pd

def find_golden_hour_customers(restaurant_orders: pd.DataFrame) -> pd.DataFrame:

                            # We prepare for determining peak hour orders
    is_peak = lambda x: (((t11 <= x) & (x<= t14)) | ((t18 <= x) & (x<= t21)))
    t11, t14, t18, t21 = (pd.to_timedelta('11:00:00'), pd.to_timedelta('14:00:00'),
                          pd.to_timedelta('18:00:00'), pd.to_timedelta('21:00:00'))
    restaurant_orders['time'] = pd.to_timedelta(
                           restaurant_orders.order_timestamp.str.split(' ').str[1])

                            # We prepare for determining order rating averages
    restaurant_orders.order_rating = pd.to_numeric(
                              restaurant_orders['order_rating'], errors = 'coerce')

                            # We group required data for applying criteria
    df = restaurant_orders.groupby('customer_id').agg(
        total_orders   = ('order_amount', 'count'),
        peak_orders    = ('time', lambda x: is_peak(x).sum()),
        nan_count      = ('order_rating', lambda x: x.isna().sum()), 
        average_rating = ('order_rating', 'mean')).reset_index()

                            # We round these two columns as required
    df['peak_hour_percentage'] = (100 * df.peak_orders/ df.total_orders).round(0)
    df['average_rating']       = df.average_rating.round(2)

                            # We filter according to the four criteria
    df = (df[df.total_orders >= 3]                  # 1) 3 orders
            [df.peak_hour_percentage >= 60]         # 2) 60% during peak
            [df.average_rating >= 4.0]              # 3) 40% rating average
            [df.total_orders >= 2 * df.nan_count])  # 4) 50% orders rated (it's algebra)

    
                            # We tidy up and return the dataframe
    return df.sort_values(['average_rating','customer_id'],
                                              ascending = [0, 0]).iloc[:,[0,1,5,4]]
