
import streamlit as st
from core.signal_synthesizer import synthesize_signals
from scripts.backtester import run_backtest
from scripts.scheduler import schedule_tasks

st.title("🔮 AstroQuant Dashboard")

menu = st.sidebar.radio("Navigation", ["📊 Dashboard", "🧪 Backtest", "⏰ Scheduler", "⚙️ Run Signal Synth"])

if menu == "📊 Dashboard":
    st.write("Welcome to AstroQuant! Here you’ll see a live feed of trade signals, astrology & numerology insights.")
    st.success("Dashboard live update placeholder")

elif menu == "🧪 Backtest":
    if st.button("Run Backtest"):
        run_backtest()
        st.success("Backtest completed")

elif menu == "⏰ Scheduler":
    if st.button("Start Scheduler"):
        schedule_tasks()
        st.info("Task scheduler initialized")

elif menu == "⚙️ Run Signal Synth":
    if st.button("Run Synthesizer"):
        synthesize_signals()
        st.success("Signal synthesis complete")
