import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Santanu Das")
    content = """
    Hi, I am Santanu! I am a python programmer.
    """
    st.info(content)

text1 = """
Below you can find some of the apps I have built in python
"""
st.text(text1)