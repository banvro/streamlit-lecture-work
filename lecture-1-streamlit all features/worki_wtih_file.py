import streamlit as st 

st.title("Working with Files")

st.sidebar.write("File System")

st.subheader("Working With Image")

st.image("images/myimg.jpg")

st.image("images/nature.jpg")

col1, col2 = st.columns(2)

with col1:
    st.image("images/myimg.jpg")

with col2:
    st.image("images/nature.jpg")

# st.video()