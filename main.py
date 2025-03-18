import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of the forecasted days.")
print("days: " + str(days))
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

x = [0 for i in range(days*8)]
data = get_data(place="Tokyo", forecast_days=days, kind=option)

figure = px.line(x, y=data, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)