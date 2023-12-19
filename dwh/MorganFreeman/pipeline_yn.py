import pandas as pd

#Extract
df = pd.read_csv('imdb_top_1000.csv')

#Transform
df['Released_Year'] = pd.to_datetime(df['Released_Year'], errors='coerce')
df['year'] = df['Released_Year'].dt.year

#Load 
df.to_csv("imdb_years_num.csv")