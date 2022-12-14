#import packages
import pandas as pd
import datetime as dt
import numpy as np

#load dataset#1: main file
df1 = pd.read_csv('data/output_noshow1_balanced_2022-11-16.csv')
df1.dtypes

#load dataset 2: locations
df2 = pd.read_csv('data/practiceLocations.csv')
df2

#load dataset 3: car crash and temp (2016-2021)
df3 = pd.read_csv('data/US_Accidents_Dec21_updated.csv')
df3

# preview get random sample of 25 rows
df1.sample(25)

# list columns
list(df1)

############## COLUMN NAMES ##############
df1_column_names = list(df1)
df2_column_names = list(df2)
df3_column_names = list(df3)

# remove all special characters and whitespace ' ' from column names
df1.columns = df1.columns.str.replace('[^A-Za-z0-9]+', '_') ## regex 

df3.columns= df3.columns.str.replace('[^A-Za-z0-9]+', '_') ## regex 


# change all column names to lowercase
df1.columns = df1.columns.str.lower()
df2.columns = df2.columns.str.lower()
df3.columns = df3.columns.str.lower()

# convert accident start_time in df3 to datetime
df3['date'] = pd.to_datetime(df3['start_time'])
df3.dtypes
# remove time from Date and store it in a new column
df3['date'] = df3['date'].dt.date
# display the dataframe
print(df3)
df3.columns


# replace all whitespace in column names with an underscore
df1.columns = df1.columns.str.replace(' ', '_')
df2.columns = df2.columns.str.replace(' ', '_')
df3.columns = df3.columns.str.replace(' ', '_')

## want to see if strings are really strings, number are numbers, dates are dates, and boolean are booleans
df1.dtypes
df2.dtypes
df3.dtypes

#merge dataset 1 & 2
df_noshow = pd.merge(df1, df2, on='practice_id', how='inner')
df_noshow.columns

# get a specific column to preview for analysis: practice_zipcode column
column50 = df_noshow.iloc[:,49] #final column
column50.sample(100)

date_df3 = df3.iloc[:,2]

# get a specific column: patient_zipcode column
column20 = df_noshow.iloc[:,19] # patient zipcode column
column33 = df_noshow.iloc[:,32] # zipcode
column33.sample(100)

# dropping columns zipcode from df_nowhow dataset since NaN
df_noshow.drop(['zipcode'], axis=1, inplace=True, errors='ignore') #  CASE SENSITIVE
df_noshow.columns

# renaming column patient_zipcode_x to zipcode and appointment_date to date to merge with dataset3:df3 on date 
df_noshow = df_noshow.rename(columns={'patient_zipcode_x':'zipcode'}) # rename the column, where the first value is the old name and the second value is the new name
df_noshow = df_noshow.rename(columns={'appointment_date':'date'}) # rename the column, where the first value is the old name and the second value is the new name

# change to datetime
df_noshow['date'] = pd.to_datetime(df_noshow['date'])
df_noshow.dtypes
df_noshow.shape

# merging with new dataset on date  
merge_on_date = pd.merge(df_noshow, df3, on='date', how='inner')
merge_on_date_zipcode = pd.merge(df_noshow, df3, on=['date', 'zipcode'], how='inner')
merge_on_date_zipcode.shape

#### drop duplicate rows on specific column: id_x
merge_on_date =merge_on_date.drop_duplicates(subset= 'id_x', keep = 'first')
merge_on_date.shape

#saving final datasets
merge_on_date_zipcode.to_csv('./data/master1_merged_on_accidentdate&zipcode.csv')
merge_on_date.to_csv('./data/master2_merged_on_accidentdate&zipcode.csv')








