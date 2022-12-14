# utilize streamlit and AZURE VM for visualization
# # import packages
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


#########VISUALIZATIONS########

# Creating a barchart
st.subheader('Display of gender of patients to understand any correlation between gender and no-show')
patient_gender= df1['patient_gender'].value_counts()
st.bar_chart(patient_gender)
st.caption('Visual provides correlation between gender on no-show')

# Creating a line chart
st.subheader('Any correlation between appointment type and no-show')
appointment_type = df1['appointment_type'].value_counts()
st.line_chart(appointment_type)
st.caption('Visual provides insight on the impact of type of appointment on no-show')

# Creating a barchart
st.subheader('Display of patient age to understand any correlation between age and no-show')
patient_age = df1['patient_age'].value_counts()
st.bar_chart(patient_age)
st.caption('Visual provides correlation between age on no-show')

# Creating a line chart
st.subheader('Any correlation between appointment within 5 days holiday and no-show')
appintmentwithin5dayholiday = df1['appintmentwithin5dayholiday'].value_counts()
st.line_chart(appintmentwithin5dayholiday)
st.caption('Visual provides insight on the impact of holidays on no-show')

# Creating a line chart
st.subheader('Any correlation between appointment within 7 days holiday and no-show')
appintmentwithin7dayholiday = df1['appintmentwithin7dayholiday'].value_counts()
st.line_chart(appintmentwithin7dayholiday)
st.caption('Visual provides insight on the impact of holidays on no-show')


# Creating a line chart
st.subheader('Any correlation between appointment starting hour and no-show')
appointment_start_time_hour = df1['appointment_start_time_hour'].value_counts()
st.line_chart(appointment_start_time_hour)
st.caption('Visual provides insight on appointment starting hour on no-show')