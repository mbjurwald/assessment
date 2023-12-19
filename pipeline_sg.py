import pandas as pd

#Extract
df = pd.read_csv('imdb_top_1000.csv')

# Transform 
df["Genre"] = df["Genre"].str.split(", ")

exploded_df = df.explode("Genre")

exploded_df['IMDB_Rating'] = pd.to_numeric(exploded_df['IMDB_Rating'], errors='coerce')

#Load 
df.to_csv("imdb_split_genres.csv")