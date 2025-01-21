import json
import pandas as pd

# 載入 JSON
movie_data = {
    "Title": "Harry Potter and the Deathly Hallows: Part 2",
    "Year": "2011",
    "Rated": "PG-13",
    "Released": "15 Jul 2011",
    "Runtime": "130 min",
    "Genre": "Adventure, Family, Fantasy",
    "Director": "David Yates",
    "Writer": "Steve Kloves, J.K. Rowling",
    "Actors": "Daniel Radcliffe, Emma Watson, Rupert Grint",
    "Plot": "As the battle between the forces of good and evil in the wizarding world escalates, Harry Potter draws ever closer to his final confrontation with Voldemort.",
    "Language": "English, Latin",
    "Country": "United Kingdom, United States",
    "Awards": "Nominated for 3 Oscars. 49 wins & 95 nominations total",
    "Poster": "https://m.media-amazon.com/images/M/MV5BOTA1Mzc2N2ItZWRiNS00MjQzLTlmZDQtMjU0NmY1YWRkMGQ4XkEyXkFqcGc@._V1_SX300.jpg",
    "Ratings": [
        {
            "Source": "Internet Movie Database",
            "Value": "8.1/10"
        },
        {
            "Source": "Rotten Tomatoes",
            "Value": "96%"
        },
        {
            "Source": "Metacritic",
            "Value": "85/100"
        }
    ],
    "Metascore": "85",
    "imdbRating": "8.1",
    "imdbVotes": "979,804",
    "imdbID": "tt1201607",
    "Type": "movie",
    "DVD": "N/A",
    "BoxOffice": "$381,447,587",
    "Production": "N/A",
    "Website": "N/A",
    "Response": "True"
}
df = pd.json_normalize(movie_data)

# 顯示 DataFrame
#print(df)

excel_file = '\\workspaces\\TIR104_g2\\V_Victor\\read\\movie_data.xlsx'  # 設定檔案名稱及儲存路徑

# 儲存成 Excel 檔案
if df.to_excel(excel_file, index=False, engine='openpyxl'):
    print(f"檔案已成功儲存為 {excel_file}")
else:
    print('失敗')