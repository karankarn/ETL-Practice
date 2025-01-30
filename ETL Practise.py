"""
Project Scenario:
An international firm that is looking to expand its business in different countries across 
the world has recruited you. You have been hired as a junior Data Engineer and are tasked with 
creating a script that can extract the list of the economies of the world in 
descending order of their GDPs in Billion USD (rounded to 2 decimal places), as logged by the 
International Monetary Fund (IMF).

The data is saved in a dataFrame, Database and Json File. They are then queried to return the 
top 10 largest economies """

import pandas as pd
import numpy as np
import sqlite3


URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

"""
-------
Extract
-------
"""
# saves all the information from the URL in a list. index [3] on the list is the information i require
webdata = pd.read_html(URL, header=0) 

# saving the dataframe as an object df
df = webdata[3]

# removing the rows corresponding to repeat labels and WORLD stats
df = df[2:]

# resetting index after removind top two rows
df = df.reset_index()

# Renaming the columns
df = df.rename( 
    columns = {"Country/Territory" : "Country",
               
               "IMF[1][13]" : "IMF Estimate (millions)",
               })

# Taking the subset of data we will be working with
df = df[["Country","IMF Estimate (millions)"]]



# removing countries without datapoints
df["IMF Estimate (millions)"].unique()
df = df.drop(df[df["IMF Estimate (millions)"] == '—'].index)




"""
---------
Transform
---------
"""
# convert the string type to numeric to perform mathematical opertaions
df["IMF Estimate (millions)"] = pd.to_numeric(df["IMF Estimate (millions)"])

# IMF Estimate is in millions. I need the value in billions with two decimal places.
df["IMF Estimate (billions)"] = (df["IMF Estimate (millions)"]/1000).round(2)

df = df[["Country","IMF Estimate (billions)"]]




"""
-----
Load
-----
"""
"Loading the transformed data into a csv file"

target_file = "Countries_by_GDP.csv"

def load_data(target_file, transformed_data): 
    transformed_data.to_csv(target_file)   
  
load_data(target_file,df)
  

  
  

"""To create a table in the database, you first need to have
 the attributes of the required table. Attributes are columns of the 
 table. Along with their names, the knowledge of their data types are
  also required."""

# connection to database
conn = sqlite3.connect("World_Economies.db")
# table name
table_name = "World_Economies"
# attribute(columns) list
attribute_list = ["Country","IMF Estimate (billions)"]

# convert the df to an sql database
df.to_sql(table_name,conn,if_exists = "replace", index = False)

# Query to select all countries with GDP over 100B
query_statement = f'SELECT * FROM "World_Economies" WHERE "IMF Estimate (billions)" >= 100'
query_output = pd.read_sql(query_statement, conn)
print(query_statement)
print(query_output)







