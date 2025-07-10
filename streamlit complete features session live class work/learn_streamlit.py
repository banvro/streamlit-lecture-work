import streamlit as st

st.title("This is My first webside")

st.header("This is my headering")

st.subheader("this is my subhrad")

st.write("Python is a powerful programming lanaguge...")

# streamlit run filename.py

# python -m streamlit run filename.py

st.markdown("""
### Programming Langauges
## Backend Langauges
- Python
- PHP
- JavaScript
- Pascal
            
## Frontend Langauges
1. HTML
2. CSS          
""")

st.code("""
def hlo():
   print("helloww worlddd) 
        
hlo()
""")

# AI ----

# equestions

st.write("x^2 + y^1 + z = 0")

st.latex("x^2 + y^1 + z = 0")