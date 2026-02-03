import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the App
st.title("🥖 Bakery Demand Forecasting App")

# Simple "Hello World" to prove it works
st.write("Welcome to the Bakery AI System!")
st.write("This app will eventually forecast demand for Croissants and Baguettes.")

# A placeholder chart
data = pd.DataFrame({
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Sales': [120, 135, 110, 145, 180]
})

fig = px.bar(data, x='Day', y='Sales', title="Sample Sales Data")
st.plotly_chart(fig)