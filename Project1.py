import streamlit as st
st.title("New Machine Learning Project")
st.info("I am going to make a new project")
with st.expander("Used to expand and shrink below data"):
    st.write("My name is Rohan")
with st.sidebar:
    gender=st.selectbox("Your Gender",['Male','Female'])
    age=st.slider("Your Age",0,100)
