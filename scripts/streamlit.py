# utilize streamlit and AZURE VM for visualization
# # import packages
import pandas as pd
import streamlit as st
import numpy as np

st.title('Descriptive Analysis of a Patient No-show Database (sub-database containing 25000 rows of the original databse')

st.caption('The dataset was provided by Dr. Hants for the final competition assignment to analyze and better understand the key non-clinical factos that effect patient no-show')

#### Dataframe master_3 (25000 rows)
df1 = pd.read_csv('data/dataset_streamlit.cvs') 
df_head = df1.head(100)


#### Toggle ####

# Displaying the dataframe 1
if st.checkbox('Show first 30 records of baseline patient no-show database'):
    st.dataframe(df_head)

#########VISUALIZATIONS########

# Creating a barchart
st.subheader('Display of gender of patients to understand any correlation between gender and no-show')
patient_gender= df1['patient_gender'].value_counts()
st.bar_chart(patient_gender)
st.caption('Visual provides correlation between gender on number of no-show patients. Gender is the independent variable, plotted on the x-axis and number of no-shows is the continuous variable')

# Creating a line chart
st.subheader('Any correlation between appointment type and no-show')
appointment_type = df1['appointment_type'].value_counts()
st.line_chart(appointment_type)
st.caption('Visual provides insight on the impact of type of appointment on number of no-shows. Types of appointment is the independent variable, plotted on the x-axis and the number of no-shows is the continuous dependent variable, plotted on the y-axis. For this sub-dataset, circumcisions and rapid-COVID are the types of appointment where there were the highest no-shows.')

# Creating a barchart
st.subheader('Display of patient age to understand any correlation between age and no-show')
patient_age = df1['patient_age'].value_counts()
st.bar_chart(patient_age)
st.caption('Visual provides correlation between age on no-show. Age is the independent variable and no-shows is the continous dependent variable. Children below the age of 4 had the highest no-shows.')

# Creating a bar chart
st.subheader('Any correlation between appointment starting hour and no-show')
appointment_start_time_hour = df1['appointment_start_time_hour'].value_counts()
st.bar_chart(appointment_start_time_hour)
st.caption('Visual provides insight on appointment starting hour on no-shows. Most no-shows are in the 9th and 10th hour of the day.')