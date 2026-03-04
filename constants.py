from collections import namedtuple
from typing import Dict, Tuple


EMAIL_PATTERN: str = r'^[\w\.-]+@[\w\.-]+\.\w+$'
DATE_FORMATS: Tuple = ("%Y-%m-%d", "%d-%m-%Y", "%m/%d/%Y", "%B %d, %Y", "%Y/%m/%d")

FILES_PATH: namedtuple = namedtuple('FILES_PATH', ['customers', 'orders', 'products'])(
    customers='raw_data/customers.csv',
    orders='raw_data/orders.csv',
    products='raw_data/products.csv'
)

CLEANED_FILE_PATH: namedtuple = namedtuple('CLEANED_FILE_PATH', ['customers', 'orders', 'products'])(
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


ANALYSIS_OUTPUT_FILE_PATH: namedtuple = namedtuple('ANALYSIS_OUTPUT_FILE_PATH', [
    'order_year_month', 'top_customers', 'category_performance', 'regional_analysis', 'churn_indicator'
])(
    order_year_month='analysis_data/order_year_month.csv',
    top_customers='analysis_data/top_customers.csv',
    category_performance='analysis_data/category_performance.csv',
    regional_analysis='analysis_data/regional_analysis.csv',
    churn_indicator='analysis_data/churn_indicator.csv'
)
