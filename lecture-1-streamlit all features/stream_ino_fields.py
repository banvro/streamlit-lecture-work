import streamlit as st 

st.title("My Contact Us Form")

full_name = st.text_input("Enter your full name : ")

user_age = st.number_input("Enter your age : ", max_value = 100, min_value = 18)

gender = st.selectbox("Choose Your Gender", ["Male", "Female"])

# Get dateof birth
st.date_input("Enter your Date of birth")

phone_number = st.number_input("Enter your Phone number : ")

msg = st.text_area("Enter your Message:")

btn = st.button("Send Message")

if btn:
    st.header("Button Clicked!")
    st.title(f"{full_name}, {gender}")