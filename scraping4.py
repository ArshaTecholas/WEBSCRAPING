# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# url="https://books.toscrape.com/catalogue/page-1.html"
# page=requests.get(url)
# soup=BeautifulSoup(page.text,"html")
# all_books = soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

# d = {"description":[], "upc":[], "review":[], "stock":[],"price":[], "tax":[],"title":[]}

# for book in all_books:
#   link = "https://books.toscrape.com/catalogue/"+book.find("a").attrs["href"]
#   new_page = requests.get(link)
#   new_soup=BeautifulSoup(new_page.text,"html")
#   d['description'].append(new_soup.find_all("p")[3].text)
#   d['upc'].append(new_soup.find("table",class_="table table-striped").find_all("tr")[0].find("td").text)
#   d['review'].append(new_soup.find("table",class_="table table-striped").find_all("tr")[6].find("td").text)
#   d['stock'].append(new_soup.find("table",class_="table table-striped").find_all("tr")[5].find("td").text)
#   d['price'].append(new_soup.find("table",class_="table table-striped").find_all("tr")[3].find("td").text[2:])
#   d['tax'].append(new_soup.find("table",class_="table table-striped").find_all("tr")[4].find("td").text[2:])
#   d['title'].append(new_soup.find("h1").text)

# df = pd.DataFrame(d)
# print(df)

import requests
from bs4 import BeautifulSoup
import pandas as pd

current_page = 1
data = []
proceed = True
while(proceed):
    print("Currently scraping page: "+str(current_page))
    url = "https://books.toscrape.com/catalogue/page-"+str(current_page)+".html"
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html")
    if soup.title.text == "404 Not Found":
        proceed = False
    else:
        all_books = soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        for book in all_books:
            item = {}
            item['Title'] = book.find("img").attrs["alt"]
            item['Link'] = "https://books.toscrape.com/catalogue/"+book.find("a").attrs["href"]
            item['Price'] = book.find("p", class_="price_color").text[2:]
            item['Stock'] = book.find("p", class_="instock availability").text.strip()
            data.append(item)
    current_page += 1
df = pd.DataFrame(data)
print(df)
df.to_excel("books.xlsx")
df.to_csv("books.csv")
