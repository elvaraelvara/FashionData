import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
file_path = 'all_data.csv'
data = pd.read_csv(file_path)

# Sidebar
st.sidebar.title("Dashboard Options")
visualization_option = st.sidebar.selectbox("Select Visualization", ["Age Distribution", "Gender Distribution", "Product Type Distribution", "Purchase Quantity Distribution", "Product Price Distribution", "Correlation Heatmap"])

# Main content
st.title("Data Visualization Dashboard")

# Visualization 1: Age Distribution
if visualization_option == "Age Distribution":
    st.subheader("Age Distribution of Customers")
    fig_age = plt.figure(figsize=(10, 6))
    sns.histplot(data['age'], bins=20, kde=True)
    st.pyplot(fig_age)

# Visualization 2: Gender Distribution
elif visualization_option == "Gender Distribution":
    st.subheader("Gender Distribution of Customers")
    fig_gender = plt.figure(figsize=(8, 5))
    sns.countplot(x='gender', data=data)
    st.pyplot(fig_gender)

# Visualization 3: Product Type Distribution
elif visualization_option == "Product Type Distribution":
    st.subheader("Product Type Distribution")
    fig_product_type = plt.figure(figsize=(12, 8))
    sns.countplot(x='product_type', data=data, order=data['product_type'].value_counts().index)
    plt.xticks(rotation=45)
    st.pyplot(fig_product_type)

# Visualization 4: Purchase Quantity Distribution
elif visualization_option == "Purchase Quantity Distribution":
    st.subheader("Purchase Quantity Distribution")
    fig_quantity = plt.figure(figsize=(10, 6))
    sns.boxplot(x='quantity_x', data=data)
    st.pyplot(fig_quantity)

# Visualization 5: Product Price Distribution
elif visualization_option == "Product Price Distribution":
    st.subheader("Product Price Distribution")
    fig_price = plt.figure(figsize=(10, 6))
    sns.histplot(data['price'], bins=20, kde=True)
    st.pyplot(fig_price)

# Visualization 6: Correlation Heatmap
elif visualization_option == "Correlation Heatmap":
    st.subheader("Correlation Heatmap")
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    correlation_matrix = data[numeric_columns].corr()
    fig_heatmap = plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
    st.pyplot(fig_heatmap)

# Visualization 7: Top Purchased Product Prices
elif visualization_option == "Top Purchased Product Prices":
    st.subheader("Top 10 Most Purchased Product Prices")
    price_counts = data['price'].value_counts()
    top_prices = price_counts.head(10)
    fig_top_prices = plt.figure(figsize=(12, 8))
    sns.barplot(x=top_prices.index, y=top_prices.values)
    plt.xticks(rotation=45)
    plt.title('Top 10 Most Purchased Product Prices')
    plt.xlabel('Product Price')
    plt.ylabel('Purchase Frequency')
    st.pyplot(fig_top_prices)