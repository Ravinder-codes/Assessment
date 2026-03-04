from datetime import datetime 
import pandas as pd
from typing import List

import constants


def parse_dates(date_val: str):
        for format in constants.DATE_FORMATS:
            try:
                return datetime.strptime(date_val, format)
            except ValueError: 
                continue
        # No match found
        return pd.NaT

def read_csv()-> List:
    '''Function to read the files 
    '''
    customers_df: pd.DataFrame = pd.read_csv(constants.CLEANED_FILE_PATH.customers, index_col=None)
    orders_df: pd.DataFrame = pd.read_csv(constants.CLEANED_FILE_PATH.orders, index_col=None)
    products_df: pd.DataFrame = pd.read_csv(constants.CLEANED_FILE_PATH.products, index_col=None)

    return [customers_df, orders_df, products_df]
