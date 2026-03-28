import streamlit as st
from queries import get_top_products

st.set_page_config(page_title="Products", layout="wide")

st.title("Product Analysis")

products_df = get_top_products()

selected_category = st.selectbox(
    "Filter Products by Category",
    ["All"] + sorted(products_df["category"].unique().tolist())
)

if selected_category != "All":
    products_df = products_df[products_df["category"] == selected_category]

metric_col1, metric_col2 = st.columns(2)

with metric_col1:
    st.metric("Total Product Revenue", f"{products_df['total_revenue'].sum():,.2f}")

with metric_col2:
    st.metric("Total Quantity Sold", f"{int(products_df['total_quantity'].sum())}")

st.subheader("Products Table")
st.dataframe(products_df, width="stretch")

chart_df = products_df[["product_name", "total_revenue"]].copy()

if not chart_df.empty:
    st.subheader("Revenue by Product")
    st.bar_chart(chart_df.set_index("product_name"))
else:
    st.info("No product data available.")
