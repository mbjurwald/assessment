import pandas as pd

#Extract
df = pd.read_csv('imdb_top_1000.csv')

#Transform
df["Runtime"] = df["Runtime"].str.replace("min", " ")
df["Runtime"] = pd.to_numeric(df["Runtime"], errors="coerce")

#Load 
df.to_csv("imdb_runtime_without_min.csv")