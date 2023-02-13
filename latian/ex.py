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
	#st.title("Main App")
	stc.html(html_temp)

	
	query_params = st.experimental_get_query_params()
	tabs = ["Home","Disease","About"]

	if "tab"== query_params:
		active_tab = query_params["tabs"][0]
		##st.write(desc_temp)
		#st.markdown(desc_temp,unsafe_allow_html=True)
	    active_tab = query_params["tabs"][0]
	else:
    	active_tab = "Home"

	if active_tab not in tabs:
    	st.experimental_set_query_params(tab="Home")
    	active_tab = "Home"

	li_items = "".join(
    	f"""
    	<li class="nav-item">
        	<a class="nav-link{' active' if t==active_tab else ''}" href="/?tab={t}">{t}</a>
    	</li>
    	"""
	    for t in tabs
	)
	tabs_html = f"""
    	<ul class="nav nav-tabs">
    	{li_items}
    	</ul>
	"""

	st.markdown(tabs_html, unsafe_allow_html=True)
	st.markdown("<br>", unsafe_allow_html=True)

	if active_tab == "Home":
    	st.write("Welcome to my lovely page!")
    	st.write("Feel free to play with this ephemeral slider!")
    	st.slider(
     	   "Does this get preserved? You bet it doesn't!",
        	min_value=0,
        	max_value=100,
        	value=50,
    	)
	elif active_tab == "About":
    	st.write("This page was created as a hacky demo of tabs")
	elif active_tab == "Contact":
    	st.write("If you'd like to contact me, then please don't.")
	else:
    	st.error("Something has gone terribly wrong.")

if __name__ == '__main__':
	main()














