import pandas as pd
import requests
import json
import csv

url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&primary_release_year=2024&sort_by=popularity.desc"

headers = {
"accept": "application/json",
"Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzMjMzNGEwZGJiNjU0NDIzMjlkODg4NWQxNjMzZGZhNSIsIm5iZiI6MTczNjkzOTQ2NS4zNDgsInN1YiI6IjY3ODc5N2M5YmQ3OTNjMDM1NDRmMjBlNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.c0Fm2RPV9hH_cZ6t_7PTSw5HTjGuKZSQDbeU5c-D99c"
	}

response = requests.get(url, headers=headers)
tw_movie_2024 = response.text

with open("movie_2024.json", "w", encoding="utf-8") as f:
	json.dump(tw_movie_2024, f, ensure_ascii=False)
print('存取成功') 















