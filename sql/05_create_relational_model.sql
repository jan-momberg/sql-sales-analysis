DROP TABLE IF EXISTS portfolio.orders;
DROP TABLE IF EXISTS portfolio.customers;
DROP TABLE IF EXISTS portfolio.products;

CREATE TABLE portfolio.customers (
    customer_id INT PRIMARY KEY,
    customer_name TEXT NOT NULL,
    country TEXT NOT NULL
);

CREATE TABLE portfolio.products (
    product_id INT PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    unit_price NUMERIC(10,2) NOT NULL
);

CREATE TABLE portfolio.orders (
    order_id INT PRIMARY KEY,
    order_date DATE NOT NULL,
    customer_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    revenue NUMERIC(10,2) NOT NULL,
    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id) REFERENCES portfolio.customers(customer_id),
    CONSTRAINT fk_product
        FOREIGN KEY (product_id) REFERENCES portfolio.products(product_id)
);
