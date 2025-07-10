import streamlit as st 
import pandas as pd

st.title("Working with Data Structure")

st.sidebar.header("Data Structure")

data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [20, 21, 19, 22, 20],
    'Grade': ['Sophomore', 'Junior', 'Freshman', 'Senior', 'Sophomore'],
    'GPA': [3.5, 3.7, 3.2, 3.8, 3.6]
})

st.dataframe(data)

jsonn = [
  {
    "Name": "Alice",
    "Age": 20,
    "Grade": "Sophomore",
    "GPA": 3.5
  },
  {
    "Name": "Bob",
    "Age": 21,
    "Grade": "Junior",
    "GPA": 3.7
  },
  {
    "Name": "Charlie",
    "Age": 19,
    "Grade": "Freshman",
    "GPA": 3.2
  },
  {
    "Name": "David",
    "Age": 22,
    "Grade": "Senior",
    "GPA": 3.8
  },
  {
    "Name": "Eva",
    "Age": 20,
    "Grade": "Sophomore",
    "GPA": 3.6
  }
]


st.json(jsonn)

