INSERT INTO portfolio.customers (customer_id, customer_name, country)
VALUES
(101, 'Anna Schmidt', 'Germany'),
(102, 'Lukas Weber', 'Germany'),
(103, 'Claire Martin', 'France'),
(104, 'Carlos Ruiz', 'Spain'),
(105, 'Mia Fischer', 'Germany');

INSERT INTO portfolio.products (product_id, product_name, category, unit_price)
VALUES
(1, 'Laptop', 'Electronics', 1200.00),
(2, 'Mouse', 'Electronics', 25.00),
(3, 'Desk Chair', 'Furniture', 180.00),
(4, 'Monitor', 'Electronics', 300.00),
(5, 'Notebook', 'Office Supplies', 4.00);

INSERT INTO portfolio.orders (order_id, order_date, customer_id, product_id, quantity, revenue)
VALUES
(1, '2024-01-05', 101, 1, 1, 1200.00),
(2, '2024-01-06', 102, 2, 2, 50.00),
(3, '2024-01-07', 103, 3, 1, 180.00),
(4, '2024-01-08', 104, 4, 2, 600.00),
(5, '2024-01-09', 105, 5, 5, 20.00);
