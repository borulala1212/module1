# Core Pkgs
import streamlit as st 
import streamlit.components.v1 as stc

# Import mini apps
from eda_app_diabetesNum import run_eda_app_diabetesNum
from ml_app_diabetesNum import run_ml_app_diabetesNum

from eda_app_liver import run_eda_app_liver
from ml_app_liver import run_ml_app_liver

from eda_app_BC import run_eda_app_BC
from ml_app_BC import run_ml_app_BC

from eda_app_HD import run_eda_app_HD
from ml_app_HD import run_ml_app_HD

from PIL import Image


html_temp = """
		<h2 style="color:black;text-align:justify;">AICare is a useful application for predicting chronic diseases based on the implementation of machine learning. </h2>
		"""
html_temp1 = """
			####<p1> AICare focus on chronic disease such as </p>
				- Breast Cancer Disease
				- Diabetes Disease
				- Heart Disease
				- Liver Disease


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
	#st.title("Main App")
	menu = ["AICare","Disease Prediction","About Us"]
	choice = st.sidebar.selectbox('Menu',menu)



	if choice == "AICare":
		img = Image.open("COVERUTAMA.jpg")
		st.image(img,use_column_width=True)
		stc.html(html_temp)
		#stc.html(html_temp1)

		##st.write(desc_temp)
		#st.markdown(desc_temp,unsafe_allow_html=True)


	elif choice == "Disease Prediction":
		menu1 = ["Breast Cancer Disease","Diabetes Disease","Heart Disease","Liver Disease"]
		choice1 = st.sidebar.selectbox('Our Facilities',menu1)

		## Breast Cancer
		desc_temp_BC = """
			### Early Stage Breast Cancer Disease Predictor App
			Original Wisconsin Breast Cancer Database
			#### Datasource
				https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Original%29
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App

			"""
		## Heart Disease
		desc_temp_HD = """
			### Early Stage Heart Disease Predictor App
				Heart Disease Dataset
			#### Datasource
				https://github.com/ammarmahmood1999/HeartHealthPrediction/blob/master/heart.csv
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App

			"""
		## DIABETES DISEASE

		desc_temp_diabetes = """
			### Early Stage Diabetes Disease Predictor App
			Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage.
			#### Datasource
				- https://www.kaggle.com/datasets/mathchi/diabetes-data-set
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App

			"""
		## penyakit hati 
		desc_temp_liver = """
			### Early Stage Liver Disease Predictor App
			This data set contains 416 liver patient records and 167 non liver patient records.The data set was collected from north east of Andhra Pradesh, India. Selector is a class label used to divide into groups(liver patient or not). This data set contains 441 male patient records and 142 female patient records. 
			#### Datasource
				- https://archive.ics.uci.edu/ml/datasets/ILPD+(Indian+Liver+Patient+Dataset)
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App

			"""





		if choice1 == "Diabetes Disease":
			
			DD = ["Explore Data Analysis","Diabetes Prediction"]
			choice11 = st.sidebar.radio('Features',DD)
			img1 = Image.open("DIABETES.jpg")
			st.image(img1,use_column_width=True)

			#if choice11 == "Home":
			#	st.subheader("Home")
			#	st.markdown(desc_temp_diabetes,unsafe_allow_html=True)

			if choice11 == "Explore Data Analysis":
				st.markdown(desc_temp_diabetes,unsafe_allow_html=True)
				run_eda_app_diabetesNum()
			elif choice11 == "Diabetes Prediction":
				run_ml_app_diabetesNum()
			else:
				pass



		## LIVER DISEASE
		elif choice1 == "Liver Disease":
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

		elif choice1 == "Breast Cancer Disease":

			DD = ["Explore Data Analysis","Breast Cancer Prediction"]
			choice11 = st.sidebar.radio('Features',DD)
			img3 = Image.open("BREASTCANCER.jpg")
			st.image(img3,use_column_width=True)
				
			if choice11 == "Explore Data Analysis":
				st.markdown(desc_temp_BC,unsafe_allow_html=True)
				run_eda_app_BC()
			elif choice11 == "Breast Cancer Prediction":
				run_ml_app_BC()
			else:
				pass


		elif choice1 == "Heart Disease":

			DD = ["Explore Data Analysis","Heart Prediction"]
			choice11 = st.sidebar.radio('Features',DD)
			img4 = Image.open("HEART.jpg")
			st.image(img4,use_column_width=True)

			if choice11 == "Explore Data Analysis":
				st.markdown(desc_temp_HD,unsafe_allow_html=True)
				run_eda_app_HD()
			elif choice11 == "Heart Prediction":
				run_ml_app_HD()
			else:
				pass
	else:
		st.subheader("About Us")
		st.write("hallo")


if __name__ == '__main__':
	main()














