import streamlit as st 
from auth_db import csr, conn

def logout_this():
    st.session_state.authanticated = False
    st.session_state.username = ""
    st.rerun()

if "authanticated" not in  st.session_state:
    st.session_state.authanticated = False

if "username" not in st.session_state:
    st.session_state.username = ""

if st.session_state.authanticated:
    st.success(f"Already Login as : {st.session_state.username}")
    st.write("Click On Logout to end the session....!")
    if st.button("Logout"):
        logout_this()

else:
    st.title("Login Page")

    username = st.text_input("Enter your username")

    password = st.text_input("Enter your password",type = "password" )

    btn = st.button("Login")

    if btn:
        if username == "" or password == "":
            st.error("Please fill all fields...")
            st.snow()
        
        else:
            csr.execute(f"select * from signup_user where username = '{username}';")
            
            check_usernmae = csr.fetchone()

            if check_usernmae is None:
                st.warning("Username not found..!")
            
            else:

                if password != check_usernmae[4]:
                    st.warning("Please enter valid password")

                else:
                    st.session_state.authanticated = True
                    st.session_state.username = check_usernmae[0]
                    st.session_state.full_name = check_usernmae[1]
                    st.write(check_usernmae)
                    st.write(f"you suvessfuly login as {check_usernmae[1]}")
                    st.success("Login Sucessfully done..!")
                    st.balloons()
                    st.rerun()