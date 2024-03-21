import streamlit as st
from PIL import Image

def bmi_calc(w,h):
    bmi = w/(h**2)
    bmi =  round(bmi,1)

    if bmi >= 35:
        return f"Your BMI is {bmi}, you are at risk of obesity class 2."
    elif 30 <= bmi < 35:
        return f"Your BMI is {bmi}, you are at risk of obesity class 1."
    elif 25 <= bmi < 30:
        return f"Your BMI is {bmi}, you are at risk of pre- obesity."
    elif 18.5 <= bmi < 25:
        return f"Your BMI is {bmi}, you are within the healthy range."
    else:
        return f"Your BMI is {bmi}, you are at risk of underweight."

st.title("BMI Calculator")
st.subheader("health is wealth,Calculate your BMI today")

img = Image.open("imageb.jpg")
st.image(img)
         
weight = st.number_input("Enter your weight in kg", step=0.1)
height = st.number_input("Enter your height in metres", step=1)       