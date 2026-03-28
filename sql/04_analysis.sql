-- Gesamtumsatz
SELECT SUM(revenue) AS total_revenue
FROM portfolio.sales;

-- Umsatz nach Land
SELECT country, SUM(revenue) AS revenue
FROM portfolio.sales
GROUP BY country
ORDER BY revenue DESC;

-- Umsatz nach Kategorie
SELECT category, SUM(revenue) AS revenue
FROM portfolio.sales
GROUP BY category
ORDER BY revenue DESC;

-- Durchschnittlicher Umsatz pro Bestellung
SELECT AVG(revenue) AS avg_revenue
FROM portfolio.sales;

-- Top Produkte nach Umsatz
SELECT product_name, SUM(revenue) AS revenue
FROM portfolio.sales
GROUP BY product_name
ORDER BY revenue DESC;
