import streamlit as st
import yfinance as yf   # for getting stock details

st.title("Mariya's Stock Wizard!")

# Get the stock symbol input from the User
stock_symbol = st.text_input("Stock Symbol", placeholder="Enter a stock symbol")

# Fetch stock data from yfinance for the given stock symbol
stock_data = yf.Ticker(stock_symbol)


# Date Input columns
dc1, dc2 = st.columns(2)

with dc1:
    start_date = st.date_input("Start Date")
with dc2:
    end_date = st.date_input("End Date")

# Fetch the stock history details for the given stock symbol
stock_df = stock_data.history(period="1mo", start=start_date, end=end_date)

# Display the stock history                              
st.write(stock_df)

# Display the history in the Charts
chart1, chart2 = st.columns(2)

with chart1:
    st.subheader("Close Trend of {}".format(stock_symbol))
    st.line_chart(stock_df, y="Close")

with chart2:
    st.subheader("Volume Trend of {}".format(stock_symbol))
    st.line_chart(stock_df, y="Volume")
                              