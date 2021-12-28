import streamlit as st
st.title("MY FIRST CLOUD APP")
st.write("Streamlit cloud app")
st.write("Hello")
number1= st.slider("Pick any number",0,100)
number2= st.slider("Pick any",0,100)
x= number1+number2
st.write(x)
