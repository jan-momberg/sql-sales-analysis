import streamlit as st
from queries import get_top_customers

st.set_page_config(page_title="Customers", layout="wide")

st.title("Customer Analysis")

customers_df = get_top_customers()

selected_country = st.selectbox(
    "Filter Customers by Country",
    ["All"] + sorted(customers_df["country"].unique().tolist())
)

if selected_country != "All":
    customers_df = customers_df[customers_df["country"] == selected_country]

st.subheader("Top Customers by Revenue")
st.dataframe(customers_df, width="stretch")

chart_df = customers_df[["customer_name", "total_revenue"]].copy()

if not chart_df.empty:
    st.bar_chart(chart_df.set_index("customer_name"))
else:
    st.info("No customer data available.")
