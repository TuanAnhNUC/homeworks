import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

# User persona
persona = {
    "adventurous": 0.8,
    "emotional": 0.5,
    "humorous": 0.6,
    "analytical": 0.7,
    "imaginative": 0.9,
    "intense": 0.4
}

mapping = {
    "Action": ["adventurous"],
    "Adventure": ["adventurous"],
    "Animation": ["humorous", "imaginative"],
    "Biography": ["emotional"],
    "Comedy": ["humorous"],
    "Crime": ["analytical", "intense"],
    "Drama": ["emotional"],
    "Family": ["humorous"],
    "Fantasy": ["imaginative"],
    "Film-Noir": ["analytical"],
    "History": ["emotional"],
    "Horror": ["intense"],
    "Music": ["emotional"],
    "Musical": ["humorous"],
    "Mystery": ["analytical"],
    "Romance": ["emotional"],
    "Sci-Fi": ["imaginative"],
    "Sport": ["adventurous"],
    "Thriller": ["analytical", "intense"],
    "War": ["adventurous", "intense"],
    "Western": ["adventurous"]
}

genre_vector = {}

for genre, traits in mapping.items():
    score = sum(persona[t] for t in traits)
    genre_vector[genre] = score

print(genre_vector)


df = pd.read_csv('imdb_top_1000.csv')
cols_to_drop = [
    "Poster_Link", "Overview", "Director",
    "Star1", "Star2", "Star3", "Star4",
    "Gross", "Certificate"
]

df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])
df["Genre"] = df["Genre"].str.split(", ")
genre_dummies = df["Genre"].explode().str.get_dummies().groupby(level=0).max()
df = pd.concat([df, genre_dummies], axis=1)
df = df.fillna(0)

print(genre_dummies.columns.tolist())

genre_cols = list(genre_vector.keys())

user_vec = [genre_vector[g] for g in genre_cols]
movie_matrix = df[genre_cols].values

similarity = cosine_similarity([user_vec], movie_matrix)[0]

df["similarity"] = similarity

top10 = df.sort_values(by="similarity", ascending=False).head(10)

print(top10[["Series_Title", "similarity"]])
# Graphic
top10 = df.sort_values(by="similarity", ascending=False).head(10)

plt.figure()
plt.barh(top10["Series_Title"], top10["similarity"])
plt.xlabel("Similarity Score")
plt.title("Top 10 Recommended Movies")
plt.gca().invert_yaxis()

plt.show()

plt.figure()
plt.hist(df["similarity"], bins=20)
plt.title("Distribution of Similarity Scores")
plt.xlabel("Similarity")
plt.ylabel("Number of Movies")

plt.show()