import plotly.express as px
import numpy as np

# func to plot the charts
def interactive_plot(df):
    fig = px.line()
    for i in df.columns[1:]:
        fig.add_scatter(x=df['Date'], y=df[i], name=i)
    fig.update_layout(
        width=450, 
        margin=dict(l=20, r=20, t=50, b=20), 
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
    )
    return fig

# func to normalize the prices 
def normalize(df_2):
    df = df_2.copy()
    for i in df.columns[1:]:
        df[i] = df[i] / df[i].iloc[0] 
    return df

# func to calculate daily returns
def daily_return(df_2):
    df = df_2.copy()
    for i in df.columns[1:]:
        df[i] = df[i].pct_change() * 100  
    df.fillna(0, inplace=True)  
    return df

# func to calculate beta
def calculate_beta(stock_daily_return, stock):
    rm = stock_daily_return['sp500'].mean() * 252  # 
    b, a = np.polyfit(stock_daily_return['sp500'], stock_daily_return[stock], 1)
    return b, a




