# 📈 Global Stock Price App – Streamlit Dashboard

This repository contains an interactive and region-aware **financial data visualization dashboard** built using Python and [Streamlit](https://streamlit.io). The app allows users to compare the historical performance of stocks across **Brazil 🇧🇷, the United States 🇺🇸, and Europe 🇪🇺**, using real-time data pulled from **Yahoo Finance**.

The project highlights a complete **data-driven web application**, from UI logic to performance computation, ideal for both business users and data analysts.

---

## 🌍 Overview

### Key Features:
- ✅ Compare multiple stocks across three global markets  
- 📅 Interactive date range slider with persistent selection  
- 📉 Visualize price evolution dynamically  
- 💰 Simulate portfolio value and returns  
- ⚠️ Intelligent handling of missing data with graceful fallback  
- 🧠 Efficient caching using Streamlit session state

---

## 🖼️ App Preview

Here are examples of the interactive dashboards powered by the app:

### 📊 1. Cross-Market Comparison (Brazil + USA)

![Global Stock App TSLA vs PETR4](https://raw.githubusercontent.com/AndreLuiz-Cardoso/Data-Science/main/Global_Stock_Price_App/img/0%20stocksus.png) 
Users can select companies from multiple regions (e.g., Tesla in the USA and Petrobras in Brazil) and compare their historical performance side by side. The app shows percentage return and final portfolio value based on a simulated investment.

---

### 🇧🇷 2. Brazil-Only Portfolio Analysis

![Global Stock App BR stocks](https://raw.githubusercontent.com/AndreLuiz-Cardoso/Data-Science/main/Global_Stock_Price_App/img/1%20stocksbrazil.png) 
You can analyze multiple Brazilian assets such as PETR4, ABEV3, and B3SA3 simultaneously. The app calculates both individual and portfolio-level performance, displaying the growth (or loss) over time.

---

### 🇺🇸 3. USA Big Tech Portfolio Simulation

![Global Stock App Tech Portfolio](https://raw.githubusercontent.com/AndreLuiz-Cardoso/Data-Science/main/Global_Stock_Price_App/img/3%20diferentStocks.png)
Users can simulate a portfolio with companies like META, AAPL, AMZN, and more. The dashboard visualizes their price evolution and computes the total return of the equally-weighted portfolio over the selected period.

---

Each chart is fully interactive, and updates based on user-selected stock tickers, regions, and timeframes. The portfolio simulator dynamically adjusts results according to the initial capital input, helping users understand long-term performance.
---

## 🛠️ Technologies Used

- 🐍 **Python 3.9+**
- 📊 **Pandas** – for time series manipulation and performance calculations  
- 💸 **yFinance** – for pulling real-time financial data  
- 🖥️ **Streamlit** – to build and deploy the interactive web dashboard  

---

## 🗂️ Project Structure

```text
├── main.py               # Streamlit app source code
├── IBOV.csv              # Tickers from Brazilian stock market
├── NASDAQ.csv            # Tickers from the U.S. NASDAQ exchange
├── EURONEXT.csv          # Tickers from European markets
├── requirements.txt      # List of dependencies
└── README.md             # You're here :)
```

## 🚀 Try it Live

Experience the app running in production:

> 🌐 **Live Demo**: [click here](https://andre-cardoso-global-stock-price-app.streamlit.app/)  
> *(Replace this with the actual URL after deployment on Streamlit Cloud)*

No installation needed — just open the link and start exploring stock performance across the globe.

---

## 🎯 Project Objectives

- ✅ Deliver a professional-grade Streamlit app with real-time financial data  
- ✅ Showcase financial data visualization using interactive UI components  
- ✅ Allow users to simulate and track multi-asset portfolio performance  
- ✅ Provide a smooth UX with clear messages when data is unavailable  
- ✅ Handle large volumes of historical data efficiently using caching strategies  

---

## 🧠 What This Project Demonstrates

This project reflects key capabilities that are valuable in a modern data/tech role:

- **Full-stack data product thinking** – from raw data to user-facing insights  
- **Strong Python programming** with libraries like `pandas` and `yfinance`  
- **Streamlit expertise** – layout control, session state, widget handling  
- **Business logic awareness** – KPIs, returns, portfolio simulation  
- **Resilience and usability** – intelligent fallback for incomplete datasets  

---

## 💡 How to Run Locally

To explore the project on your own machine:

```bash
# Clone the repository
git clone https://github.com/AndreLuiz-Cardoso/global-stock-app.git
cd global-stock-app

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run main.py
