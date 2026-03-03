from collections import namedtuple
from typing import Dict, Tuple


FILES_PATH = namedtuple('FILES_PATH', ['customers', 'orders', 'products'])(
    customers='raw_data/customers.csv',
    orders='raw_data/orders.csv',
    products='raw_data/products.csv'
)

CLEANED_FILE_PATH = namedtuple('CLEANED_FILE_PATH', ['customers', 'orders', 'products'])(
    customers='cleaned_data/customers_clean.csv',
    orders='cleaned_data/orders_clean.csv',
    products='raw_data/products.csv'
)

ORDER_STATUS_MAPPING: Dict = {
    "completed": "completed",
    "complete": "completed",
    "pending": "pending",
    "pending approval": "pending",
    "cancelled": "cancelled",
    "cancel": "cancelled",
    "refunded": "refunded",
    "refund": "refunded",
    "refnded": "refunded"
}

DATE_FORMATS: Tuple = ("%Y-%m-%d", "%d-%m-%Y", "%m/%d/%Y", "%B %d, %Y", "%Y/%m/%d")
