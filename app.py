import streamlit as st
st.title("MY FIRST CLOUD APP")
st.write("Streamlit cloud app")
st.write("Hello")
number1= st.slider("Pick any number",0,100)
number2= st.slider("Pick any number",0,100)
x= number1+number2
y= number1-number2
st.write("SUM")
st.write(x)
st.write("DIFFERENCE")
st.write(y)
