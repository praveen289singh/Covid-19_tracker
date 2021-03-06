# Importing important libraries

import pandas as pd
import requests

# Getting the desired data 

url = "https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory#wrapper65150380"
req = requests.get(url)

list_of_df = pd.read_html(req.text)
target_df = list_of_df[9]

# Cleaning the data 

# 1) Removing redundant columns 
target_df = target_df.drop(columns=["Country","Unnamed: 5", "Unnamed: 6", "Unnamed: 7"])

# 2) Renaming the columns
target_df.columns = ["Country_name", "Death/million", "Deaths", "Cases"]

# 3) Removing redundant rows
target_df = target_df.drop([0,target_df.index[-1]], axis=0)

# 4) Correcting inconsistent country names
target_df["Country_name"] = target_df["Country_name"].str.replace("\[.*\]", "")

# 5) Replacing null values with zero
target_df["Death/million"] = target_df["Death/million"].str.replace("—", "0")
target_df["Deaths"] = target_df["Deaths"].str.replace("—", "0")

# 6) Converting the count data to numeric 
target_df["Death/million"] = pd.to_numeric(target_df["Death/million"])
target_df["Deaths"] = pd.to_numeric(target_df["Deaths"])
target_df["Cases"] = pd.to_numeric(target_df["Cases"])

# Exporting the data to an excel file 
target_df.to_excel(r"Covid-19_data.xlsx")





