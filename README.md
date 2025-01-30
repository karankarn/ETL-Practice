# ETL-Practice
Practicing ETL pipeline with a project for beginners

## World Economies by GDP (IMF Estimates)  

This repository contains a Python script that automates the extraction, transformation, and loading of country GDP data from the International Monetary Fund (IMF), as listed on Wikipedia. The data is then stored in both a CSV file and a local SQLite database. Finally, it demonstrates a simple SQL query to extract the top economies with an IMF GDP estimate above 100 billion USD.  


## Project Overview
An international firm is looking to expand its business globally and needs an up-to-date, organized record of the GDP of countries around the world. As a junior Data Engineer, you are responsible for creating a script that fetches the latest GDP data (in billions of USD) from the IMF, processes it, and stores it for further analytics and decision-making.

The script is designed to be run periodically (twice a year or whenever new IMF data is published) so that the data remains current and accurate.

## Data Source
The data is extracted from the archived version of the Wikipedia page: "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"  

## Script Workflow  
### 1. Extract  
The script uses pandas.read_html() to read all HTML tables from the Wikipedia page.  
It then selects the relevant table (index 3) which contains the GDP information as per the IMF estimates.  

### 2. Transform
Removes irrelevant rows such as repeated headers and the "World" row.  
Filters out any rows where the GDP data is missing ('—').  
Converts the GDP data from millions of USD to billions of USD, rounding to 2 decimal places.  

### 3. Load  
Writes the transformed dataset to a CSV file (Countries_by_GDP.csv).  
Creates a local SQLite database (World_Economies.db) and stores the data in a table (World_Economies).  

### 4. Query
Demonstrates a sample SQL query selecting records for countries with a GDP >= 100 (billion USD).  


