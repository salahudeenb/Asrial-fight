import streamlit as st

# Read the HTML game code
with open("Asriel_Dreamer_Fight.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Display it in Streamlit
st.components.v1.html(html_code, height=600, scrolling=True)
