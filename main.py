import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime

st.set_page_config(layout="wide")
st.title("📈 Global Stock Price App")
st.markdown("Compare stock performance across Brazil 🇧🇷, USA 🇺🇸, and Europe 🇪🇺")

# === Load tickers from each region ===
@st.cache_data
def load_tickers_brazil():
    df = pd.read_csv("IBOV.csv", sep=";")
    return {"🇧🇷 " + code.strip() + ".SA": code.strip() + ".SA" for code in df["Código"].dropna()}

@st.cache_data
def load_tickers_usa():
    df = pd.read_csv("NASDAQ.csv")
    return {"🇺🇸 " + symbol: symbol for symbol in df["Symbol"].dropna()}

@st.cache_data
def load_tickers_europe():
    df = pd.read_csv("EURONEXT.csv", sep=";")
    df = df[df["Symbol"].notnull()]
    return {"🇪🇺 " + symbol.strip(): symbol.strip() for symbol in df["Symbol"].dropna()}

@st.cache_data
def fetch_data(tickers):
    tickers_str = " ".join(tickers)
    data = yf.Tickers(tickers_str).history(start="2010-01-01")
    return data["Close"]

# === Sidebar: Region Filters ===
st.sidebar.header("Select Regions")
use_brazil = st.sidebar.checkbox("🇧🇷 Brazil", value=True)
use_usa = st.sidebar.checkbox("🇺🇸 USA", value=True)
use_europe = st.sidebar.checkbox("🇪🇺 Europe", value=True)

# === Load tickers ===
ticker_label_to_code = {}
if use_brazil:
    ticker_label_to_code.update(load_tickers_brazil())
if use_usa:
    ticker_label_to_code.update(load_tickers_usa())
if use_europe:
    ticker_label_to_code.update(load_tickers_europe())

if not ticker_label_to_code:
    st.sidebar.warning("Please select at least one region.")
    st.stop()

# === Stock selection ===
selected_labels = st.sidebar.multiselect("📊 Select stocks to compare", options=list(ticker_label_to_code.keys()))
selected_tickers = [ticker_label_to_code[label] for label in selected_labels]

# === Fixed date range ===
global_start = datetime(2010, 1, 1)
global_end = datetime(2025, 1, 1)

# Store once in session_state
if "date_range" not in st.session_state:
    st.session_state.date_range = (global_start, global_end)

# Render slider and update session state only on change
date_range = st.sidebar.slider(
    "📆 Select date range",
    min_value=global_start,
    max_value=global_end,
    value=st.session_state.date_range,
    key="date_slider"
)

# Update session state only if user changed the slider
if date_range != st.session_state.date_range:
    st.session_state.date_range = date_range

# === Portfolio input ===
portfolio_value = st.sidebar.number_input("💰 Enter portfolio value", min_value=0.0, step=100.0)

# === Load data once using session state ===
if "stock_data_cache" not in st.session_state:
    st.session_state["stock_data_cache"] = {}

# Create key to cache by selected tickers
tickers_key = "-".join(sorted(selected_tickers))

if tickers_key not in st.session_state["stock_data_cache"] and selected_tickers:
    st.session_state["stock_data_cache"][tickers_key] = fetch_data(selected_tickers)

stock_data = st.session_state["stock_data_cache"].get(tickers_key, pd.DataFrame())

# === Main content ===
if not selected_tickers or stock_data.empty:
    st.info("👈 Please select at least one valid stock.")
    st.stop()

# Filter by date - mantém a seleção do usuário mesmo com dados faltantes
filtered_data = stock_data[selected_tickers].copy()

# Verifica se há dados para o período selecionado
has_data_in_range = False
try:
    temp_data = stock_data[selected_tickers].loc[date_range[0]:date_range[1]]
    if not temp_data.empty:
        has_data_in_range = True
except:
    pass

if has_data_in_range:
    filtered_data = stock_data[selected_tickers].loc[date_range[0]:date_range[1]]
else:
    st.warning(f"Showing all available data (no data found for {date_range[0].date()} to {date_range[1].date()})")
    # Mantém a seleção do usuário mas mostra todos os dados disponíveis
    filtered_data = stock_data[selected_tickers].dropna(how='all')

# Remove linhas onde todas as ações estão com NaN
filtered_data = filtered_data.dropna(how='all')

if filtered_data.empty:
    st.error("No price data available for the selected stocks.")
    st.stop()

# === Chart ===
st.subheader("📈 Price Evolution")
st.line_chart(filtered_data)

# === Performance Calculation ===
st.subheader("📌 Asset Performance")
performance_summary = ""
portfolio_returns = []

for ticker in selected_tickers:
    # Filtra dados específicos para cada ação
    series = filtered_data[ticker].dropna()
    
    if len(series) < 2:
        performance_summary += f"\n{ticker}: Insufficient data"
        portfolio_returns.append(0)
        continue

    initial = series.iloc[0]
    final = series.iloc[-1]
    if initial == 0 or pd.isna(initial) or pd.isna(final):
        performance_summary += f"\n{ticker}: Invalid price data"
        portfolio_returns.append(0)
        continue

    perf = (final / initial) - 1
    portfolio_returns.append(1 + perf)

    label = [k for k, v in ticker_label_to_code.items() if v == ticker][0]
    color = "green" if perf > 0 else "red" if perf < 0 else ""
    performance_summary += f"\n{label}: <span style='color:{color}'>{perf:.1%}</span>"

# === Portfolio Summary ===
if portfolio_returns:
    avg_perf = (sum(portfolio_returns) / len(portfolio_returns)) - 1
    final_value = portfolio_value * (1 + avg_perf) if portfolio_value else None

    color = "green" if avg_perf > 0 else "red" if avg_perf < 0 else "black"
    performance_summary += f"\n\n**Portfolio performance (equal-weighted)**: <span style='color:{color}'>{avg_perf:.1%}</span>"
    if portfolio_value:
        performance_summary += f"\n**Final portfolio value**: {final_value:,.2f}"

st.markdown(performance_summary, unsafe_allow_html=True)