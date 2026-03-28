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

SELECT
    c.country,
    SUM(o.revenue) AS total_revenue
FROM portfolio.orders o
JOIN portfolio.customers c
    ON o.customer_id = c.customer_id
GROUP BY c.country
ORDER BY total_revenue DESC;

SELECT
    p.category,
    SUM(o.revenue) AS total_revenue
FROM portfolio.orders o
JOIN portfolio.products p
    ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;
