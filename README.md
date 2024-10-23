# **CAPM - Capital Asset Pricing Model Web App**

This is a **Streamlit** web application for analyzing stock returns using the **Capital Asset Pricing Model (CAPM)**. The app allows users to select multiple stocks and compare their returns against the S&P 500 market returns. It calculates key financial metrics, including **beta** and **expected return**, for selected stocks.

## **Features**

- Select multiple stocks dynamically from a list or input your own custom stock symbols.
- Calculate daily returns of stocks and the S&P 500 index.
- Visualize stock prices and normalized stock prices.
- Calculate beta and alpha values for each stock using the CAPM formula.
- Compute expected returns for selected stocks based on the CAPM model.
- Interactive data plots using **Plotly** for better visualization.
  
## **Technologies Used**

- **Python**: Backend logic for stock analysis and CAPM calculations.
- **Streamlit**: Frontend framework for building the web interface.
- **Pandas**: Data manipulation and analysis.
- **Plotly**: For interactive and dynamic plotting.
- **Yahoo Finance API**: For fetching real-time stock data.
- **FRED API (Federal Reserve Economic Data)**: For fetching S&P 500 market data.

## **Installation**

### 1. **Clone the Repository**

```bash
git clone https://github.com/your-username/capm-web-app.git
cd capm-web-app
```

### 2. **Set up a Python virtual environment**

```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

### 3. **Install the required dependencies**

```bash
pip install -r requirements.txt
```

### 4. **Run the Streamlit App**

```bash
streamlit run CAPM_Return.py
```

## **Usage**

1. **Input Stocks**: Select up to four stocks from the dropdown or enter custom stock symbols manually.
2. **Select Time Range**: Choose how many years of historical data to analyze.
3. **View Results**: The app will automatically calculate and display:
   - Stock prices and normalized prices.
   - Beta and alpha for each stock.
   - CAPM-expected return for each stock.
4. **Interact**: Use interactive plots to compare the performance of multiple stocks against the S&P 500.

## **File Structure**

```
.
├── CAPM_Return.py           # Main Streamlit app file
├── CAPM_functions.py        # Helper functions for CAPM calculations and plotting
├── requirements.txt         # List of dependencies
└── README.md                # Project documentation
```

## **Dependencies**

The following libraries are required to run the project:

- **streamlit**: `pip install streamlit`
- **pandas**: `pip install pandas`
- **yfinance**: `pip install yfinance`
- **pandas_datareader**: `pip install pandas-datareader`
- **plotly**: `pip install plotly`

Alternatively, install all dependencies at once using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## **Contributing**

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for improvements, bug fixes, or feature requests.
