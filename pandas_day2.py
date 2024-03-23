# -*- coding: utf-8 -*-
"""pandas_day2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XQcEqD_w-nymEBjM47P7qYHI7iMuhLOW
"""

# Concatenate Data Frames
import  pandas as pd
india_weather = pd.DataFrame({
    "city" : ["Mumbai", "Delhi", "Banglore"],
    "temperature" : [32,45,30],
    "humidity" : [80,60,78]
                                })

india_weather

us_weather = pd.DataFrame({
    "city" : ["new york","chicago","orlando"],
    "temperature" :[21,14,35],
    "humidity" : [68,65,75]

})
us_weather

# concate two dataframes
df = pd.concat([india_weather, us_weather])
df

# if you want to continuos index
df = pd.concat([india_weather, us_weather], ignore_index = True)
df

df =pd.concat([india_weather, us_weather], axis = 1)
df

# merge data frames
temperature_df = pd.DataFrame({
    "city" : ["mumbai","delhi","bangalore","hyderabad"],
    "temperature" : [32,45,30,40]
})
temperature_df

humidity_df = pd.DataFrame({
    "city": ["delhi","mumbai","banglore"],
    "humidity" : [68,65,75]
})
humidity_df

# merge two data frames with out explicitly mention index
df = pd.merge(temperature_df, humidity_df, on='city')
df

# OUTER JOIN
df = pd.merge(temperature_df, humidity_df, on = 'city', how='outer')
df

df = pd.DataFrame([1,2,3,4,5,6,7,8,9,10])
df

# numerical indexing
df = pd.DataFrame([1,2,3,4,5,6,7,8,9,10], index = [49,48,47,46,45,1,2,3,4,5])
df