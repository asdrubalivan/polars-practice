import streamlit as st
from backend import get_visa_countries, get_country_list

countries = get_country_list()


def swap() -> None:
    st.session_state.country1, st.session_state.country2 = (
        st.session_state.country2,
        st.session_state.country1,
    )


st.title("Visa requirements in different countries")
choice1 = st.selectbox(label="Country 1", options=countries.to_pandas(), key="country1")
choice2 = st.selectbox(label="Country 2", options=countries.to_pandas(), key="country2")
st.button(label="Swap", on_click=swap)


if st.session_state.country1 == st.session_state.country2:
    st.text("Countries are the same, please select different countries")
else:
    data = get_visa_countries(st.session_state.country1, st.session_state.country2)
    st.table(data.to_pandas())
