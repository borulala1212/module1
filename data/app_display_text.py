# Basics & Fundamentals

# Core Pkgs
import streamlit as st

# Load EDA Pkgs
import pandas as pd

#Display Data 
df = pd.read_csv("iris.csv")

# Method 1
#st.dataframe(df)

#Adding A color style from pandas
#st.dataframe(df.style.highlight_max(axis=0))


# Method 2 : Static Tabel
#st.table(df)

# Method 3 : Usinf superfxn st.write
#st.write(df.head())

# Display JSON
st.json({'data':'name'})

# Display code
mycode = """
def sayhello():
	print("Hello Streamlit lovers)

"""
st.code(mycode,language='python')











