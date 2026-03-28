# SQL Sales Analysis Project

## Overview
This project demonstrates core SQL skills using PostgreSQL.  
The project starts with a simple flat sales table and then evolves into a relational data model with customers, products, and orders.

## Tools Used
- PostgreSQL
- psql
- SQL
- Git/GitHub
- macOS Terminal

## Project Structure
- `01_create_schema.sql` → creates the schema
- `02_create_tables.sql` → creates the initial flat sales table
- `03_insert_data.sql` → imports CSV sales data
- `04_analysis.sql` → basic aggregation analysis
- `05_create_relational_model.sql` → creates relational tables
- `06_insert_relational_data.sql` → inserts sample relational data
- `07_join_analysis.sql` → analysis with joins

## Database Schema
The relational model contains three main tables:
- `customers`
- `products`
- `orders`

Relationships:
- each order belongs to one customer
- each order contains one product
- customers and products are linked through orders

## SQL Skills Demonstrated
- `CREATE SCHEMA`
- `CREATE TABLE`
- `INSERT`
- `COPY / \copy`
- `SELECT`
- `GROUP BY`
- `ORDER BY`
- `SUM`
- `AVG`
- `JOIN`
- Primary Keys
- Foreign Keys

## Example Business Questions
- What is total revenue?
- Which country generated the highest revenue?
- Which product category performed best?
- Which customer generated the most revenue?

## Key Learnings
This project helped me practice:
- setting up PostgreSQL locally on macOS
- importing CSV data
- building a relational data model
- writing analytical SQL queries
- using joins to answer business questions

## Sample Result
Example insights from the dataset:
- Germany generated the highest revenue
- Electronics was the top-performing category
- Laptop was the highest-revenue product

## Author
Jan Momberg
