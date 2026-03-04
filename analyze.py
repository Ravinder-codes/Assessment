from datetime import datetime
import logging
import pandas as pd

import constants
from utils.common_utils import read_csv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def get_merged_data()-> pd.DataFrame:
    '''Function to join the data set and then get insights of orders with no customer or product
    '''
    try:
        customers_df, orders_df, products_df = read_csv()
    except Exception as e:
        logger.error(f'Cannot read the file due to error: {e}')
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
    full_data['order_date'] = pd.to_datetime(full_data['order_date'])
    logger.info(f'Order rows having no matching customer: {full_data["name"].isnull().sum()}')
    logger.info(f'Order rows having no matching product: {full_data["product_name"].isnull().sum()}')

    return full_data

def order_year_month_trend(merged_df: pd.date_range)-> None:
    '''Function to get the monthly revenue trend of the company
    '''
    df: pd.DataFrame = (
        merged_df[merged_df["status"]=='completed']
        .groupby('order_year_month')
        .agg(
            monthly_sales=('unit_price', 'sum')
        )
        .sort_values('order_year_month')
    )
    df.to_csv(constants.ANALYSIS_OUTPUT_FILE_PATH.order_year_month)


def top_customers_trend(merged_df: pd.DataFrame, save_file: bool = True)-> None:
    '''Function to get the top 10 customers according to their spendings
    '''
    df: pd.DataFrame = (
        merged_df[merged_df["status"]=='completed']
        .groupby('customer_id')
        .agg(
            total_spending=('unit_price', 'sum')
        )
        .sort_values('total_spending', ascending=False)
        .head(10)
    )

    if save_file: df.to_csv(constants.ANALYSIS_OUTPUT_FILE_PATH.top_customers)
    return df

def category_performance_trend(merged_df: pd.DataFrame)-> None:
    '''Function to compute the total revenue accoring to category, avg order value and number of orders
    '''
    df: pd.DataFrame = (
        merged_df[merged_df["status"]=='completed']
        .groupby('category')
        .agg(
            total_revenue=('unit_price', 'sum'),
            average_order_value=('unit_price', 'mean'),
            order_count=('unit_price', 'count')
        )
        .sort_values('category')
    )
    df.to_csv(constants.ANALYSIS_OUTPUT_FILE_PATH.category_performance)

def regional_analysis(merged_df: pd.DataFrame)-> None:
    '''Function to get the regional analysis of sales, get average customer spending in that region
    '''
    df: pd.DataFrame = (
        merged_df[merged_df["status"]=='completed']
        .groupby('region')
        .agg(
            total_revenue=('unit_price', 'sum'),
            customer_count=('customer_id', 'nunique'),
            order_count=('unit_price', 'count')
        )
        .sort_values('region')
    )
    df['avg_revenue_per_customer'] = df['total_revenue']/df['customer_count']

    df.to_csv(constants.ANALYSIS_OUTPUT_FILE_PATH.regional_analysis)

def churn_analysis(merged_df: pd.DataFrame)-> None:
    '''Function to flag the customers who have not completed orders in the past 90 days
    '''
    latest_date: datetime = merged_df['order_date'].max()
    cutoff: datetime = latest_date - pd.Timedelta(days=90)
    
    merged_df['churn'] = (merged_df['order_date'] < cutoff) & (merged_df['status'] == 'pending')
    customer_ids: set = set()

    # Take the customers who 
    for _, rows in merged_df.iterrows():
        if not rows['churn']: continue
        customer_ids.add(rows['customer_id'])

    top_customer_df: pd.DataFrame = top_customers_trend(merged_df=merged_df, save_file=False).reset_index()
    top_customer_df['churn'] = top_customer_df['customer_id'].isin(customer_ids)
    top_customer_df.to_csv(constants.ANALYSIS_OUTPUT_FILE_PATH.churn_indicator, index=False)

if __name__ == "__main__":
    try:
        merged_df: pd.DataFrame = get_merged_data()
        order_year_month_trend(merged_df=merged_df)
        top_customers_trend(merged_df=merged_df)
        category_performance_trend(merged_df=merged_df)
        regional_analysis(merged_df=merged_df)
        churn_analysis(merged_df=merged_df)
    except Exception as e:
        logger.error(f'Aborting the process due to error: {e}')
