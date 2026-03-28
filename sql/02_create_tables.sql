CREATE TABLE IF NOT EXISTS portfolio.sales (
    order_id INT PRIMARY KEY,
    order_date DATE,
    customer_id INT,
    product_name TEXT,
    category TEXT,
    quantity INT,
    unit_price NUMERIC(10,2),
    revenue NUMERIC(10,2),
    country TEXT
);