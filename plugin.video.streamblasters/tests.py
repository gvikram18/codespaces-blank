import search_movies

query = "Star Wars"
movies = search_movies(query)

for title, link in movies:
    print(title, link)
    