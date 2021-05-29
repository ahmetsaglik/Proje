import warnings
warnings.filterwarnings("ignore")
import pandas as pd

columns = ["user_id","item_id","rating","timestamp"]

df = pd.read_csv("/home/admin/Project/filmOnerisi/files.tsv",sep='\t',names=columns, encoding="utf-8")
movies = pd.read_csv("/home/admin/Project/filmOnerisi/movies.csv")

## item_id üzerinden iki dataframe birleştirme
data = pd.merge(df,movies,on="item_id")

## Filmlerin puanların ortalamasını hesaplama
moviesRatings = data.groupby("title")["rating"].mean().sort_values(ascending=False)

## Filmelere kaç oy kullanıldığını hesaplama
rateCounts = data.groupby('title')["rating"].count().sort_values(ascending=False)

## Filmlerin ortalama puanlarını dataframe'e aktarmak
ratings = pd.DataFrame(data.groupby("title")["rating"].mean())

## ratings df'sine oy sayılarını eklemek
ratings["numOfRatings"] = pd.DataFrame(data.groupby("title")["rating"].count())



moviemat = data.pivot_table(index="user_id",columns="title",values="rating")

def movieCheck(m):
    for i,row in movies.iterrows():
        if m in row["title"].lower():
            return row["title"]
        if m in row["title"]:
            return row["title"]


def oneriYap(movie):
    mov = movieCheck(movie)
    movie = moviemat[mov]
    similarMovie = moviemat.corrwith(movie)
    corrMovie = pd.DataFrame(similarMovie,columns=["Correlation"])
    corrMovie.dropna(inplace=True)
    corrMovie = corrMovie.join(ratings["numOfRatings"])
    mostSimilarMovie = corrMovie[corrMovie["numOfRatings"]>100].sort_values("Correlation",ascending=False)
    listOfFilm = []
    count = 0
    for i,row in mostSimilarMovie.iterrows():
        listOfFilm.append(i)
        count += 1
        if count == 10:
            return listOfFilm[1:]


