import streamlit as st
from queries import (
    get_total_revenue,
    get_total_orders,
    get_average_order_value,
    get_revenue_by_country,
    get_revenue_by_category,
    get_order_details,
)

st.set_page_config(page_title="Overview", layout="wide")

st.title("Overview")

total_revenue = get_total_revenue().loc[0, "total_revenue"]
total_orders = get_total_orders().loc[0, "total_orders"]
avg_order_value = get_average_order_value().loc[0, "avg_order_value"]

country_df = get_revenue_by_country()
category_df = get_revenue_by_category()
orders_df = get_order_details()

selected_country = st.selectbox(
    "Filter by Country",
    ["All"] + sorted(orders_df["country"].unique().tolist())
)

if selected_country != "All":
    orders_df = orders_df[orders_df["country"] == selected_country]
    country_df = country_df[country_df["country"] == selected_country]
    total_revenue = orders_df["revenue"].sum()
    total_orders = len(orders_df)
    avg_order_value = orders_df["revenue"].mean()

    category_df = (
        orders_df.groupby("category", as_index=False)["revenue"]
        .sum()
        .rename(columns={"revenue": "total_revenue"})
        .sort_values("total_revenue", ascending=False)
    )

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Revenue", f"{total_revenue:,.2f}")

with col2:
    st.metric("Number of Orders", f"{total_orders}")

with col3:
    st.metric("Average Order Value", f"{avg_order_value:,.2f}")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Revenue by Country")
    if not country_df.empty:
        st.bar_chart(country_df.set_index("country"))
    else:
        st.info("No data available.")

with chart_col2:
    st.subheader("Revenue by Category")
    if not category_df.empty:
        st.bar_chart(category_df.set_index("category"))
    else:
        st.info("No data available.")

st.subheader("Order Details")
st.dataframe(orders_df, width="stretch")
