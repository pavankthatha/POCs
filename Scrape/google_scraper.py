from google import search
import sys
ip=["tivo vox customer review","tivo vox customer complaints","tivo bolt talk to the vox","tivo vox review"]
#ip = ["tivo vox customer review"]
for each in ip:
    for url in search(each, stop=20):
         print(url)
