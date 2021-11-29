import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock **closing** and ***volume*** of Google!

""")

#Ticker Symbol
tickerSymbol = 'GOOGL'
#Data on this ticker 
tickerData = yf.Ticker(tickerSymbol)
#historical prices for this ticker
tickerDf = tickerData.history(period='Id', start='2010-1-1', end='2022-1-1')
#Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
