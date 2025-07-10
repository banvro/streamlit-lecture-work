import streamlit as st 

st.title("Login System")

st.sidebar.header("Login Page")

st.sidebar.selectbox("Choose Page", ["Signup", "Login", "Forget Password"])

username = st.text_input("Enter Your Username : ")

password = st.text_input("Enter your password : ", type = "password")

btn = st.button("Login Here")

if btn:
    if username == "" or password == "":
        st.warning("Enter all fields..!")
        st.snow()
    else:
        if username == "python":
            if password == "python@123":
                st.success("Login Sucessfully....!")
                st.balloons()
            else:
                st.error("Enter Valid Password")
        else:
            st.error("Enter a valid username..")