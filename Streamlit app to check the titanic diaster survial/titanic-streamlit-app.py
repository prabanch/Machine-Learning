# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 09:03:14 2020

@author: praba
"""

import streamlit as st
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

st.write("""
# Titanic Survival Prediction App

This app predicts the **Titaic Survival**!
""")
st.write('---')
st.header('Specify Input Parameters')

# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Specify Input Parameters')

def user_input_features():
    

    name = st.sidebar.text_input("Enter Name","")
    age = st.sidebar.text_input("Enter Age","10")
    
    gender = st.sidebar.selectbox("Select Gender",['Male', 'Female'])
    
    pclass = st.sidebar.selectbox("Select Class",['1', '2','3'])  
    TravelAlone  = st.sidebar.selectbox("Select No of Travellors",['0','1', '2','3'])  
    Fare   = st.sidebar.slider("Select Fare",10,100,50)  
    Embarked = st.sidebar.selectbox("Select Port of Embarked",['S', 'Q','C'])  

    Selected_features = ['Age', 'TravelAlone', 'Pclass_1', 'Pclass_2', 'Embarked_C', 
                         'Embarked_Q', 'Sex_female', 'IsMinor']    

    
    print(type(TravelAlone))
    
    if TravelAlone == '0':
        TravelAlone = 1
    else:
        TravelAlone = 0
    
    if pclass == '1':
        Pclass_1 = 1
        Pclass_2 = 0
    elif pclass == '2':
        Pclass_1 = 0
        Pclass_2 = 1
    else: 
        Pclass_1 = 0
        Pclass_2 = 0
         
    Embarked_C = 0
    Embarked_Q = 0     
   
    if gender == 'Male':
        Sex_female = 0
    else:
        Sex_female = 1
        
    if int(age) < 16:
        IsMinor = 1
    else:
        IsMinor = 0    
        
    data = {
            'Age': int(age),
            'TravelAlone': TravelAlone,
            'Pclass_1':  Pclass_1,
            'Pclass_2' : Pclass_2,
            'Embarked_C': Embarked_C, 
            'Embarked_Q':  Embarked_Q,
            'Sex_female': Sex_female,
            'IsMinor': IsMinor}
    features = pd.DataFrame(data, index=[0])
    print(features)
    return features

df = user_input_features()

# Main Panel

import joblib

if st.sidebar.button('Predict Survival'):
    # Print specified input parameters
    st.header('Specified Input parameters')
    st.write(df)
    st.write('---')
    
    
    
    filename = 'rf_model.h5'
    loaded_model = joblib.load(filename)
    
    prediction = loaded_model.predict(df)
    
    
    if prediction[0] == 0:
        prediction = 'Not Survive'
    else:
        prediction = 'Survive'
    st.header('Prediction is that the passenger will ' + "'" + prediction + "'")
    # st.write(prediction)