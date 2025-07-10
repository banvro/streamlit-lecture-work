import streamlit as st
import pandas as pd
st.title("File Uploader")

st.sidebar.subheader("Load Dataset")

file = st.file_uploader("Upload Your file to View info..", type = "csv")

# cap = st.camera_input("Be on camera")

if file is not None:

    df = pd.read_csv(file, encoding='latin1')

    st.write(f"this data hold {df.shape[0]} records and {df.shape[1]} columns.")

    st.dataframe(df)