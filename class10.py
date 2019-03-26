from bs4 import BeautifulSoup
import urllib.request
import os, csv

page = urllib.request.urlopen("https://www.imdb.com/chart/top")
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find("td", attrs = {"class": "titleColumn"})

name_box = soup.find_all("td", attrs = {"class": "titleColumn"})
print(len(name_box))


for i in range(len(name_box)):
    a = name_box[i].text.strip()
    a = a.split('\n')[1].strip()
    print(a)

ratings = soup.find_all("td", attrs = {"class": "ratingColumn imdbRating"})

sdata = {}
for i in range(10):
    a = name_box[i].text.strip().split('\n')[1].strip()
    sdata[a] = float(ratings[i].text.strip())

with open("filmdata.csv", "w") as toWrite:
    writer = csv.writer(toWrite, delimiter = ",")
    writer.writerow(["Film","Rating"])
    for a in sdata.keys():
        writer.writerow([a.encode("utf-8"), sdata[a]])




