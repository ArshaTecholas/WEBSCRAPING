import requests
from bs4 import BeautifulSoup
import pandas as pd
df1=pd.DataFrame()
current_page = 1
proceed = True
while(proceed):
    print("Currently scraping page: "+str(current_page))
    url = "https://www.scrapethissite.com/pages/forms/?page_num="+str(current_page)
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html")
    table = soup.find('table')
    titles = table.find_all('th')
    table_titles = [title.text.strip() for title in titles]
    df = pd.DataFrame(columns = table_titles)
    column_data = table.find_all('tr',class_="team")
    print(column_data)
#     if len(column_data)==0:
#       proceed=False
#     else:
#       for row in column_data:
#         row_data = row.find_all('td')
#         individual_row_data = [data.text.strip() for data in row_data]
#         length = len(df)
#         df.loc[length] = individual_row_data
#     df1=pd.concat([df1, df], ignore_index=True)
#     current_page += 1


# df1.to_csv("books.csv")