from numpy.core.records import array
import streamlit as st
from joblib import load
import numpy as np
import sys
sys.path.insert(0, '../scripts')


def app():

    # Load Saved Results Data
    #model = load(filename='./models/satisfaction_scorer_model.joblib')

    st.title("Sales Prediction App")

    st.header("Insert Store id")
    st.subheader("What is your store ID: ")
    session_count = st.number_input('Enter sessions',key='a')
    
    st.subheader("How far is the nearest competitor?: ")
    total_time = st.number_input('Enter distance in meters', key='b')

    st.subheader("What is yoyr store type : ")
    average_delay = st.number_input('Enter store type',key='c')

    st.subheader("How is your store assorted?: ")
    total_throughput = st.number_input('Enter store assortment',key='d')
    from io import StringIO 


    if st.button('Predict Sales'):
        try:
            #array = ['Store Id','Store Type ,Assortment ,DistaceToCompetitor ]
           # val = model.predict([array])
            satisfaction = [i[0] for i in val][0]
            st.write('The predicted satisfaction score of the user is: {:.3f}'.format(satisfaction))
        except:
            print('Need more inputs')