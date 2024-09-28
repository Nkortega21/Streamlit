import plotly.express as px
import streamlit as st
import pandas as pd
df = pd.read_csv('Resources/municipal_demographics.csv')
# Group by city and calculate the average income
df_avg_income = df.groupby('City', as_index=False)['Income'].mean()
# Create the Plotly bar chart
fig = px.bar(df_avg_income, x='City', y='Income', title="Average Income per City")
# Display the chart in Streamlit
st.plotly_chart(fig)