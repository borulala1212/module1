# Core Pkgs
import streamlit as st 
import streamlit.components.v1 as stc

from PIL import Image
# Import mini apps
from eda_app_liver import run_eda_app_liver
from ml_app_liver import run_ml_app_liver

html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Early Stage Disease Risk Data App </h1>
		<h4 style="color:white;text-align:center;">Cronic Disease</h4>
		</div>
		"""
desc_temp = """
			### Early Stage Disease Predictor App
			This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
			#### Datasource
				- https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App
			"""
def main():
	#stc.html(html_temp)
	menu = ["Home","Disease Prediction","About"]
	choice = st.sidebar.selectbox('Menu',menu)
	if choice == "Home":
		st.subheader("Home")

	elif choice == "Disease Prediction":
		desc_temp_liver = """
			### Early Stage Liver Disease Predictor App
			This data set contains 416 liver patient records and 167 non liver patient records.The data set was collected from north east of Andhra Pradesh, India. Selector is a class label used to divide into groups(liver patient or not). This data set contains 441 male patient records and 142 female patient records. 
			#### Datasource
				- https://archive.ics.uci.edu/ml/datasets/ILPD+(Indian+Liver+Patient+Dataset)
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App
			"""
		## LIVER DISEASE
		DD = ["Explore Data Analysis","Liver Prediction"]
		choice11 = st.sidebar.radio('Features',DD)
		img2 = Image.open("LIVER.jpg")
		st.image(img2,use_column_width=True)

		if choice11 == "Explore Data Analysis":
			st.markdown(desc_temp_liver,unsafe_allow_html=True)
			run_eda_app_liver()
		elif choice11 == "Liver Prediction":
			run_ml_app_liver()
		else:	
			pass
if __name__ == '__main__':
	main()














