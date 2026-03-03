import pandas as pd
from typing import List

import constants


def read_csv()-> List:
    '''Function to read the files 
    '''
    customers_df: pd.DataFrame = pd.read_csv(constants.CLEANED_FILE_PATH.customers)
    orders_df: pd.DataFrame = pd.read_csv(constants.CLEANED_FILE_PATH.orders)
    products_df: pd.DataFrame = pd.read_csv(constants.CLEANED_FILE_PATH.products)

    return [customers_df, orders_df, products_df]

def get_merged_data()-> None:
    '''Function to join the data set and then get insights of orders with no customer or product
    '''
    try:
        customers_df, orders_df, products_df = read_csv()
    except Exception as e:
        print(f'Cannot read the file due to error: {e}')
        return 
    
    # Left join of orders with customers
    orders_with_customers: pd.DataFrame = pd.merge(
        orders_df, 
        customers_df, 
        on='customer_id', 
        how='left'
    ) 

    # Left join of orders & customer with products
    full_data: pd.DataFrame = pd.merge(
        orders_with_customers, 
        products_df, 
        left_on='product',
        right_on='product_name',
        how='left'
    )

    print(f'Order rows having no matching customer:', full_data['name'].isnull().sum())
    print(f'Order rows having no matching product:', full_data['product_name'].isnull().sum())

if __name__ == "__main__":
    get_merged_data()
