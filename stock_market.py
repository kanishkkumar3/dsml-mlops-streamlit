import streamlit as st
import pandas as pd
import yfinance as yf
import datetime

st.title("Stock Market App")
st.write("Below is Stock data of Apple")

ticker_symbol = st.text_input("Enter Stock Code", "AAPL")

ticker_data=yf.Ticker(ticker_symbol)
start_date = st.date_input("Start_date", datetime.date(2022, 5, 30))
end_date = st.date_input("End_date", datetime.date(2022, 7, 30))
hist=ticker_data.history(start=start_date, end= end_date)
st.write(hist)

col1, col2 = st.columns(2)

with col1:
    st.write("This chart is stock volume")
    st.line_chart(hist.Volume)

with col2:
    st.write("This chart is stock price")
    st.line_chart(hist.Open)
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")