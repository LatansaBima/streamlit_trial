import streamlit as st

tab1, tab2 = st.tabs(["Tab1","Tab2"])

tab1.write ("Ini tab 1!")
tab2.write ("Ini tab 2!")

st.image("jarjit.png")