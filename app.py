import sys
sys.path.insert(0, './scripts')

import streamlit as st
from multiapp import MultiApp
from pages import data_upload, model_implementation
# import your app modules here

st.set_page_config(page_title="Rossman sales prediction", layout="wide")

app = MultiApp()


st.sidebar.markdown("""
# Rossman sales prediction
""")
#st.sidebar.image("../pharm_sales/images/pharm.png", use_column_width=True)

# Add all your application here
#app.add_app("Upload Data", data_upload)
app.add_app("Predict Sales ad customers", model_implementation.app)


# The main app
app.run()