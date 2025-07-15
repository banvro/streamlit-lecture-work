import streamlit as st 
from auth_db import csr, conn
import pandas as pd

st.header("My Todo app")

if "authanticated" not in  st.session_state:
    st.session_state.authanticated = False

if "username" not in st.session_state:
    st.session_state.username = ""

if st.session_state.authanticated:
    st.subheader(f"Add Todo ({st.session_state.username})")

    todo_title = st.text_input("Enter todo Title", key = "title")

    desc = st.text_area("Breif about todo..", key = "desc")

    addin = st.button("Add Todo")

    if addin:
        if todo_title == "" or desc == "":
            st.warning("please fill all fields..")
        
        else:
            csr.execute(f"insert into mytodos(todo_added, todo_title, todo_desc) values ('{st.session_state.username}', '{todo_title}', '{desc}')")

            conn.commit()

            st.success("Todo Added Sucessfully..!")
            st.balloons()

    st.header("My All Todos...")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("Todo Done")

    with col2:
        st.write("Todo Title")
    
    with col3:
        st.write("Description")

    with col4:
        st.write("Delete Todo")


    csr.execute(f"select * from mytodos where todo_added = '{st.session_state.username}';")

    all_todo = csr.fetchall()

    for id, added, title, dec, done in all_todo:

        todo_id, til, desc, dlt = st.columns(4)

        with todo_id:
            checked = st.checkbox("Done", key = {id}, value = bool(done))

            if checked != bool(done):
                csr.execute(f"update mytodos set todo_done = {checked} where todo_id = {id}")
                conn.commit()


        with til:
            st.write(f"{title}")
        
        with desc:
            st.write(f"{dec}")
        
        with dlt:
            x = st.button("⛔ Delete", key = f"{id}")

            if x:
                csr.execute(f"delete from mytodos where todo_id = {id}")
                conn.commit()
                st.snow()
                st.rerun()

        st.write("-----------------------------------------------")


    
    
else:
    st.warning("Please Login first.!")

    st.markdown("[Go to login Page](./login)")