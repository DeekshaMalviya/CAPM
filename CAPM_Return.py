import streamlit as st
import pandas as pd
import yfinance as yf
import pandas_datareader.data as web
import datetime
import CAPM_functions 
import plotly.express as px 


st.set_page_config(page_title="CAPM",
                   page_icon="chart_with_upwards_trend",
                   layout='wide')

st.title("Capital Asset Pricing Model")

# Taking input from user
col1, col2 = st.columns([1, 1])
with col1:
    stock_list = st.multiselect("Choose 4 stocks", 
                                ('TSLA', 'AAPL', 'NFLX', 'MSFT', 'MGM', 'AMZN', 'NVDA', 'GOOGL'),
                                ['TSLA', 'AAPL', 'AMZN', 'GOOGL'])

with col2:
    year = st.number_input("Number of Years", 1, 10)

try:
    # Downloading market data for SP500
    end = datetime.date.today()
    start = datetime.date(end.year - year, end.month, end.day)

    SP500 = web.DataReader(['sp500'], 'fred', start, end)

    stock_df = pd.DataFrame()

   
    for stock in stock_list:
        data = yf.download(stock, period=f'{year}y')
        stock_df[f'{stock}'] = data['Close']

    stock_df.reset_index(inplace=True)
    SP500.reset_index(inplace=True)
    SP500.columns = ['Date', 'sp500']

    
    stock_df['Date'] = stock_df['Date'].apply(lambda x: str(x)[:10])
    stock_df['Date'] = pd.to_datetime(stock_df['Date'])
    stock_df = pd.merge(stock_df, SP500, on='Date', how='inner')

    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("### Dataframe head")
        st.dataframe(stock_df.head(), use_container_width=True)

    with col2:
        st.markdown("### Dataframe tail")
        st.dataframe(stock_df.tail(), use_container_width=True)

    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("### Price of all the Stocks")
        fig = CAPM_functions.interactive_plot(stock_df)
        if fig:
            st.plotly_chart(fig)
        else:
            st.error("Failed to load chart, please check the plotly function.")

    with col2:
        st.markdown("### Price of all the Stocks (After Normalizing)")
        normalized_df = CAPM_functions.normalize(stock_df)
        fig_norm = CAPM_functions.interactive_plot(normalized_df)
        if fig_norm:
            st.plotly_chart(fig_norm)
        else:
            st.error("Failed to load normalized chart, please check the normalization function.")

    
    stock_daily_return = CAPM_functions.daily_return(stock_df)

    beta = {}
    alpha = {}

    
    for i in stock_daily_return.columns:
        if i != 'Date' and i != 'sp500':
            b, a = CAPM_functions.calculate_beta(stock_daily_return, i)
            beta[i] = b
            alpha[i] = a

  
    beta_df = pd.DataFrame(columns=['Stock', 'Beta value'])
    beta_df['Stock'] = beta.keys()
    beta_df['Beta value'] = [str(round(i, 2)) for i in beta.values()]

    with col1:
        st.markdown("### Calculated Beta Value")
        st.dataframe(beta_df, use_container_width=True)

    # Calculating return using CAPM formula
    rf = 0
    rm = stock_daily_return['sp500'].mean() * 252  # 
    return_df = pd.DataFrame()
    return_value = []

    for stock, value in beta.items():
        return_value.append(str(round(rf + (value * (rm - rf)), 2)))

    return_df['Stock'] = stock_list
    return_df['Return Value'] = return_value

    with col2:
        st.markdown("### Calculated Return using CAPM")
        st.dataframe(return_df, use_container_width=True)

except Exception as e:
    st.error(f"An error occurred: {e}")



