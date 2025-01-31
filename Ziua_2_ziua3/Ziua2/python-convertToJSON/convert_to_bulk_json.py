import csv
import json


import pandas as pd

# 128445,"Legend of Lizzie Borden, The (1975)","Drama"
# {
#     "id" : 128445, 
#     "title" : "Legend of Lizzie Borden, The",
#     "year" : 1975,
#     "genres" : ["Drama"]
# }


from pprint import pprint
with open("movies.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    filme = [  ]
    
    for row in reader:
        # print(row, type(row))

        genres = row['genres'].split("|")
        # print(genres)


        titlu_an = row['title'].split("(")
        # print(titlu_an)
        try:
            titlu = titlu_an[0]
            an = titlu_an[1].replace(")", "")
            # print(titlu)
            # print(an)
        except:
            continue

        converted = {
            "id" : row['movieId'],
            "title": titlu,
            "year" : an,
            "genres": genres
        }

        filme.append(converted)


    with open("bulk.txt", "w", encoding="utf-8") as fwriter:
        for film in filme:
            print('{"index":{}}')
            print(json.dumps(film))
            
            fwriter.write('{"index":{}}')
            fwriter.write("\n")
            fwriter.write(json.dumps(film))
            fwriter.write("\n")
   

