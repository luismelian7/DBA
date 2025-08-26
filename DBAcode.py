import streamlit as st
import pandas as pd
import plotly.express as px

# Streamlit app title
st.title("DBA Sales Insights Dashboard")

# File uploader for CSV
uploaded_file = st.file_uploader("Upload your sales CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    try:
        df = pd.read_csv(uploaded_file)
        
        # Display raw data
        st.subheader("Raw Sales Data")
        st.write(df.head())

        # Basic validation: check for required columns
        required_columns = ["Date", "Product", "Sales"]
        if not all(col in df.columns for col in required_columns):
            st.error("CSV must contain 'Date', 'Product', and 'Sales' columns.")
        else:
            # Convert Date column to datetime
            df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
            
            # Sales summary
            st.subheader("Sales Summary")
            total_sales = df["Sales"].sum()
            avg_sales = df["Sales"].mean()
            num_products = df["Product"].nunique()
            
            st.write(f"**Total Sales:** ${total_sales:,.2f}")
            st.write(f"**Average Sale Amount:** ${avg_sales:,.2f}")
            st.write(f"**Unique Products Sold:** {num_products}")

            # Sales trend chart
            st.subheader("Sales Trend Over Time")
            df_grouped = df.groupby(df["Date"].dt.date)["Sales"].sum().reset_index()
            fig = px.line(df_grouped, x="Date", y="Sales", title="Daily Sales Trend")
            st.plotly_chart(fig)

            # Sales by product
            st.subheader("Sales by Product")
            product_sales = df.groupby("Product")["Sales"].sum().reset_index()
            fig_product = px.bar(product_sales, x="Product", y="Sales", title="Sales by Product")
            st.plotly_chart(fig_product)

            # DBA-specific insight
            st.subheader("DBA Insight")
            top_product = product_sales.loc[product_sales["Sales"].idxmax(), "Product"]
            st.write(f"**Recommendation:** Focus marketing efforts on **{top_product}**, as it has the highest sales volume.")
            
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
else:
    st.info("Please upload a CSV file to see the sales summary and charts.")
