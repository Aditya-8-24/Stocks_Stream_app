import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Title of the app
st.title('Nifty Stocks Price Visualizer')

# Load data
df = pd.read_csv('../Nifty_Stocks.csv')
df['Date'] = pd.to_datetime(df['Date'])

# Show category options
categories = df['Category'].unique()
selected_category = st.selectbox('Select Category:', categories)

# Filter based on selected category
filtered_by_category = df[df['Category'] == selected_category]

# Show symbol options
symbols = filtered_by_category['Symbol'].unique()
selected_symbol = st.selectbox('Select Symbol:', symbols)

# Filter based on selected symbol
filtered_by_symbol = filtered_by_category[filtered_by_category['Symbol'] == selected_symbol]

# Plotting
st.subheader(f'Closing Price of {selected_symbol}')
plt.figure(figsize=(15, 8))
sb.lineplot(x=filtered_by_symbol['Date'], y=filtered_by_symbol['Close'])
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title(f'{selected_symbol} Closing Price Over Time')
st.pyplot(plt)
