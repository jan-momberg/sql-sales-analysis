import pandas as pd
from db import get_engine

engine = get_engine()

def get_order_details():
    query = """
    SELECT
        o.order_id,
        o.order_date,
        c.customer_name,
        c.country,
        p.product_name,
        p.category,
        o.quantity,
        o.revenue
    FROM portfolio.orders o
    JOIN portfolio.customers c
        ON o.customer_id = c.customer_id
    JOIN portfolio.products p
        ON o.product_id = p.product_id
    ORDER BY o.order_id;
    """
    return pd.read_sql(query, engine)

def get_total_revenue():
    query = """
    SELECT SUM(revenue) AS total_revenue
    FROM portfolio.orders;
    """
    return pd.read_sql(query, engine)

def get_total_orders():
    query = """
    SELECT COUNT(*) AS total_orders
    FROM portfolio.orders;
    """
    return pd.read_sql(query, engine)

def get_average_order_value():
    query = """
    SELECT AVG(revenue) AS avg_order_value
    FROM portfolio.orders;
    """
    return pd.read_sql(query, engine)

def get_revenue_by_country():
    query = """
    SELECT
        c.country,
        SUM(o.revenue) AS total_revenue
    FROM portfolio.orders o
    JOIN portfolio.customers c
        ON o.customer_id = c.customer_id
    GROUP BY c.country
    ORDER BY total_revenue DESC;
    """
    return pd.read_sql(query, engine)

def get_revenue_by_category():
    query = """
    SELECT
        p.category,
        SUM(o.revenue) AS total_revenue
    FROM portfolio.orders o
    JOIN portfolio.products p
        ON o.product_id = p.product_id
    GROUP BY p.category
    ORDER BY total_revenue DESC;
    """
    return pd.read_sql(query, engine)

def get_top_customers():
    query = """
    SELECT
        c.customer_name,
        c.country,
        SUM(o.revenue) AS total_revenue
    FROM portfolio.orders o
    JOIN portfolio.customers c
        ON o.customer_id = c.customer_id
    GROUP BY c.customer_name, c.country
    ORDER BY total_revenue DESC;
    """
    return pd.read_sql(query, engine)

def get_top_products():
    query = """
    SELECT
        p.product_name,
        p.category,
        SUM(o.revenue) AS total_revenue,
        SUM(o.quantity) AS total_quantity
    FROM portfolio.orders o
    JOIN portfolio.products p
        ON o.product_id = p.product_id
    GROUP BY p.product_name, p.category
    ORDER BY total_revenue DESC;
    """
    return pd.read_sql(query, engine)
