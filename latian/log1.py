import pickle 
from pathlib import Path

import pandas as pd 
import plotly.express as px
import streamlit as st
import streamlit_authenticator as stauth


st.set_page_config(page_title="Sales Dashboarnd", page_icon=":bar_chart:", layout="wide")

#names = ["Peter Parker", "Rebecca Miller"]
#usernames = ["pparker","rmiller"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
	hashed_passwords = pickle.load(file)

#authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
#	"sales_dashboard","abcdef",cookie_expiry_days=30)

#with open('../hashed_pw.pkl') as file:
 #   config = pickle.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    hashed_passwords['names'],
    hashed_passwords['cookie']['usernames'],
    hashed_passwords['cookie']['key'],
    hashed_passwords['cookie']['expiry_days'],
    hashed_passwords['preauthorized']
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
	st.error("Username/password is incorrect")

if authentication_status == None:
	st.warning("Please enter your username and password")

if authentication_status:

	@st.cache

	def load_data(BreastCancerWiscosin):
		df = pd.read_csv(BreastCancerWiscosin)
		return df

	def run_eda_app_BC():
		authenticator.logout("Logout","sidebar")
		st.sidebar.title(f"Welcome {name}")
		st.subheader("Exploratory Data Analysis")
		df = load_data("BreastCancerWiscosin/Breast_Cancer_Wisconsin_Clean.csv")
		#freq_df = load_data("ILPD/freq_age.csv")

		#submenu = st.sidebar.selectbox("Submenu",["Descriptive","Plots"])
		#if submenu == "Descriptive":
		with st.expander("Breast Cancer Dataset"):
			st.dataframe(df)

		with st.expander("Descriptive Summary"):
			st.dataframe(df.describe())

		with st.expander("Class Distribution"):
			st.dataframe(df['Class'].value_counts())


	#elif submenu == "Plots":
	#	st.subheader("Plots")



		#layouts
		col1,col2 = st.columns([2,1])

		with col1:
#			#For Class Distribution
			with st.expander("Dist Plot of Class"):
				fig = plt.figure()
				sns.countplot(df['Class'])
				st.pyplot(fig)

				st.write("0 for Balign; 1 for Malignant")

		with col2: 
			with st.expander("Class Distribution"):
				st.dataframe(df['Class'].value_counts())

#		# Correlation 
		with st.expander("Correlation Plot"):
			corr_matrix = df.corr()
			fig = plt.figure(figsize=(20,10))
			sns.heatmap(corr_matrix,annot=True)
			st.pyplot(fig)
