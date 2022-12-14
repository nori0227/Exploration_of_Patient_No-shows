

# import packages
import pandas as pd
import streamlit as st
import numpy as np

st.title('Descriptive Analysis of a Patient No-show Database')

st.caption('The dataset was provided by Dr. Hants for the final competition assignment to analyze and better understand the key non-clinical factos that effect patient no-show')

#### Dataframe 1
df1 = pd.read_csv('data/US_Accidents_Dec21_updated.csv')
df1 = df1.head(25)
df1

#### Dataframe 2
df2 = pd.read_csv('data/master1_merged_on_accidentdate&zipcode.csv')
df2 = df1.head(15)

#### Toggle ####

# Displaying the dataframe 1
if st.checkbox('Show first 100 records of baseline patient no-show database'):
    st.dataframe(df1)

# Displaying the dataframe 2
if st.checkbox('Show the enriched data table'):
    st.dataframe(df2)

# Creating a barchart
st.subheader('Display of gender of patients to understand any correlation between gender and no-show')
patient_gender= df2['patient_gender'].value_counts()
st.bar_chart(patient_gender)
st.caption('Visual provides correlation between gender on no-show')