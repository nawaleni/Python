from bs4 import BeautifulSoup
import urllib.request
import os, csv

# Q1 - 

page = urllib.request.urlopen("https://www.dell.com/community/Laptops/ct-p/Laptops")
soup = BeautifulSoup(page, 'html.parser')
category_box = soup.find_all("div", attrs = {"class": "cat-card-title"})
posts_box = soup.find_all("span", attrs = {"class": "cat-card-posts"})
sdata = {}

for i in range(len(category_box)):
    a = category_box[i].text
    if(a == "Inspiron" or a == "XPS" or a == "Latitude"):
        sdata[a] = posts_box[i].text.split('\t')[6].split(" ")[0]
print(sdata)


#Q2 - scrap first 5 pages discussions

data = []
for j in range(1,6):
    pages = urllib.request.urlopen("https://www.dell.com/community/Inspiron/bd-p/Inspiron/page/" + str(j))
    soup = BeautifulSoup(pages, 'html.parser')
    title = soup.find_all("a", attrs = {"class": "page-link lia-link-navigation lia-custom-event"})
    details = soup.find_all("div", attrs = {"class": "lia-info-area"})
    kudos = soup.find_all("div", attrs = {"class": "lia-component-messages-column-message-kudos-count"})
    replies = soup.find_all("div", attrs = {"class": "lia-component-messages-column-message-replies-count"})
    views = soup.find_all("div", attrs = {"class": "lia-component-messages-column-topic-views-count"})
    solved_or_not = soup.find_all("td", attrs = {"class" : "triangletop lia-data-cell-secondary lia-data-cell-icon"})
    
    for i in range(len(details)):
        #details[i].find_all
        t = title[i].text.split('\n')[1].strip()
        auth = details[i].text.split('\n')[4].strip() if details[i].text.split('\n')[3].strip() == '' else details[i].text.split('\n')[3].strip()
        time_post = details[i].text.split('\n')[7].strip() if details[i].text.split('\n')[3].strip() == '' else details[i].text.split('\n')[6].strip()
        likes = kudos[i].text.split('\n')[3].strip()
        reply = replies[i].text.split('\n')[2].strip()
        view = views[i].text.split('\n')[1]
        if(len(details[i]) > 6): 
            author_reply = details[i].text.split('\n')[16].strip() if details[i].text.split('\n')[15].strip() == '' else details[i].text.split('\n')[15].strip()
            time_reply = time_reply = details[i].text.split('\n')[14].strip() if details[i].text.split('\n')[3].strip() == '' else details[i].text.split('\n')[13].strip() 
        
        else:
            author_reply = 'None'
            time_reply = 'None'
        solved = 'No' if str(solved_or_not[i]).find("solved") == -1  else 'Yes'

        list_dell = [str(j) + " . " + str(i+1), t, auth, time_post, author_reply, time_reply, likes, reply, view, solved]
        data.append(list_dell)

with open("Dell.csv", "w") as toWrite:
    writer = csv.writer(toWrite, delimiter = ",")
    writer.writerow(["Sr. No." , "Title","Author", "Time Posted", "Author of Reply", "Time of Reply", "Kudos", "Replies", "Views", "Issued Solved"])
    for item in data:
            writer.writerow(item)

