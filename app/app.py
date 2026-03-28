import streamlit as st
from queries import (
    get_total_revenue,
    get_revenue_by_country,
    get_revenue_by_category,
    get_order_details
)

st.set_page_config(page_title="SQL Sales Dashboard", layout="wide")

st.title("SQL Sales Analysis Dashboard")
st.write("Interactive dashboard based on a PostgreSQL sales analysis project.")

total_revenue_df = get_total_revenue()
country_df = get_revenue_by_country()
category_df = get_revenue_by_category()
orders_df = get_order_details()

total_revenue = total_revenue_df.loc[0, "total_revenue"]

st.metric("Total Revenue", f"{total_revenue:,.2f}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Revenue by Country")
    st.bar_chart(country_df.set_index("country"))

with col2:
    st.subheader("Revenue by Category")
    st.bar_chart(category_df.set_index("category"))

st.subheader("Order Details")
st.dataframe(orders_df, use_container_width=True)
