import yfinance as yf
import streamlit as st
import pandas as pd

st.write(""" 

#Simple stock price app

shown are the stock closing price of google!

""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = '1d' , start = '2015-10-10' , end = '2020-10-10')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
