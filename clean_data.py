import pandas as pd
from typing import List, Any

import constants
from utils.common_utils import parse_dates


def clean_customers()-> None:
    '''Function to parse and clean the customers file
    '''
    df: pd.DataFrame = pd.read_csv(constants.FILES_PATH.customers)
    # Drop the duplicate entries
    df = df.sort_values(by='signup_date', ascending=False)
    df = df.drop_duplicates(subset='customer_id', keep='first')

    # email validations
    df['email'] = df['email'].str.lower()
    email_pattern: str = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    df['is_valid_email'] = df['email'].str.match(email_pattern)

    df['region'] = df['region'].fillna('Unknown')

    # Strip values
    def strip_val_func(val: Any):
        if isinstance(val, str):
            return val.strip()
        else:
            raise ValueError

    strip_cols: List = ['name', 'region']
    for col in strip_cols:
        try:
            df[col] = df[col].apply(strip_val_func)
        except Exception as e:
            print(f'Aborting the file cleaning process due to error:', {e})
            return

    # Sort the date and keep the most recent signup
    df['signup_date'] = df['signup_date'].apply(parse_dates)
    df = df.sort_values(by='signup_date', ascending=False)
    df = df.drop_duplicates(subset='customer_id', keep='first')
    df = df.sort_values(by='customer_id')

    df.to_csv("cleaned_data/customers_clean.csv", index=False)

def clean_orders()-> None:
    '''Function to parse and clean the orders file
    '''
    df: pd.DataFrame = pd.read_csv(constants.FILES_PATH.orders)

    # Parse the date formats
    df['order_date'] = df['order_date'].apply(parse_dates)
    df['order_year_month'] = df['order_date'].dt.strftime('%Y-%m')
    
    # Drop the duplicate entries
    df = df.dropna(subset=['customer_id', 'order_id'], how='all')

    df['amount'] = df.groupby('product')['amount'].transform(lambda val: val.fillna(val.median()))
    df['status'] = df['status'].str.lower().map(constants.ORDER_STATUS_MAPPING)

    df.to_csv("cleaned_data/orders_clean.csv", index=False)


if __name__ == '__main__': 
    try:
        clean_customers()
        clean_orders()
    except Exception as e:
        print(f'Aborted due to error: {e}')
