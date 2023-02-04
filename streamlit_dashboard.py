import streamlit as st
from backend import get_visa_countries

data = get_visa_countries("Venezuela", "Argentina")

st.title("Visa requirements in different countries")

st.table(data.to_pandas())
