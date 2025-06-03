import streamlit as st
import pandas as pd

st.set_page_config(page_title="Traffic Dashboard", layout="wide")

st.title("🚦 Real-Time Traffic Monitoring Dashboard")

df = pd.read_csv("traffic_log.csv")

st.metric("🚗 Total Vehicles", int(df['vehicle_count'].sum()))
st.metric("📸 Total Frames Logged", len(df))

st.subheader("Recent Activity")
st.dataframe(df.tail(10), use_container_width=True)

vehicle_chart = df['vehicle_count'].rolling(10).mean()
st.line_chart(vehicle_chart)
