################################
#           Projet 3           #
#      London bike sharing     #
#   Author : Jessim Ahdjoudj   #
################################

##################
### 1) Imports ###
##################

import pandas as pd
import zipfile
# import kaggle

###############################
### 2) Get the data, 2 ways ###
###############################

# Way 1 - classic #
data = pd.read_csv('london_merged.csv')

# Way 2 - to be more fancy #
# download dataset from kaggle using the Kaggle API
# kaggle datasets download -d hmavrodiev/london-bike-sharing-dataset

# extract the file from the downloaded zip file
# zipfile_name = 'london-bike-sharing-dataset.zip'
# with zipfile.ZipFile(zipfile_name, 'r') as file:
#    file.extractall()

# data = pd.read_csv('london_merged')

###########################
### 3) Date exploration ###
###########################
print('\n--- Data exploration ---\n')

print('- Data infos -')
# Get summary infos of the data
data.info()
data.describe()

# Get numbers of rows and columns in dataset
print('\n')
print('Data shape infos :', data.shape)
print('\n')

print('- Dataset overview -')
# See what the dataset looks like
print(data)

##############################
### 4) Data transformation ###
##############################
print('\n--- Data transformation ---\n')

# Global changes #
# Creating a dictionary specifying the column names that I want to use
new_cols_dict ={
    'timestamp':'time',
    'cnt':'count', 
    't1':'temp_real_C',
    't2':'temp_feels_like_C',
    'hum':'humidity_percent',
    'wind_speed':'wind_speed_kph',
    'weather_code':'weather',
    'is_holiday':'is_holiday',
    'is_weekend':'is_weekend',
    'season':'season'
}

# Renaming the columns to the dictionary specified column names
data.rename(new_cols_dict, axis=1, inplace=True)

# Changing the humidity values to percentage
data.humidity_percent = data.humidity_percent / 100

# Season changes #
# Creating a season dictionary to map the integers to the actual written values
season_dict = {
    '0.0':'spring',
    '1.0':'summer',
    '2.0':'autumn',
    '3.0':'winter'
}

# Changing seasons column to string
data.season = data.season.astype('str')

# Mapping values to the actual written seasons
data.season = data.season.map(season_dict)

# Weather changes #
# Creating a weather dictionary to map the integers to the actual written values
weather_dict = {
    '1.0':'Clear',
    '2.0':'Scattered clouds',
    '3.0':'Broken clouds',
    '4.0':'Cloudy',
    '7.0':'Rain',
    '10.0':'Rain with thunderstorm',
    '26.0':'Snowfall'
}

# Changing weather column to string
data.weather = data.weather.astype('str')

# Mapping values to the actual written weathers
data.weather = data.weather.map(weather_dict)

# Check to see if the mappings have worked
print(data.head())

#################
### 6) Export ###
#################

# Exporting transformed data to an excel file that can be use in Tableau for data visualisation
data.to_excel('london_data_transformed.xlsx', sheet_name='Data')