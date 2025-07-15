import streamlit as st 
from auth_db import csr, conn

st.title("Sign up Here")

col1, col2 = st.columns(2)

with col1:
    username = st.text_input("Enter unique username...")

with col2:
    full_name = st.text_input("Enter your full name")

phon = st.number_input("Enter your phone number", min_value = 1000000000)

email = st.text_input("ENter your email address ")

password = st.text_input("Enter your password", type = "password")

conform_pass = st.text_input("confirm password..", type = "password")

btn = st.button("Sign-up")

if btn:
    if username == "" or full_name == "" or phon == "" or email == "" or password == "" or conform_pass == "":
        st.error("Please fill up all fields")
        st.snow()
    
    else:
        if password != conform_pass:
            st.warning("conform password do not matchh..")
            st.snow()
        
        else:
            try:
                csr.execute(f"insert into signup_user(username, full_name, phone_number, email, passwordd) values('{username}', '{full_name}', '{phon}', '{email}', '{password}')")

                conn.commit()
                st.success("Signup sucessfulllyyy..!")
                st.balloons()

                st.markdown("[Go to login page](./login)")
            
            except Exception as e:
                st.error("Please check username must be unique..!")