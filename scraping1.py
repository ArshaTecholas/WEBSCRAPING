import requests
from bs4 import BeautifulSoup
url = "https://infopark.in/companies/job-search"
response = requests.get(url,  verify=False)
soup=BeautifulSoup(response.text,'lxml')
jobs=soup.find_all("div",{"class":"row company-list joblist"})
for job in jobs:
    title_element=job.find("a")
    title=title_element.text
    link=title_element["href"]
    company_name=job.find("div",{"class":"jobs-comp-name"}).text
    last_date=job.find("div",{"class":"job-date"}).text
    print(title,link,company_name,last_date)

# print(response.text)







# import requests
# from bs4 import BeautifulSoup

# url = "https://infopark.in/companies/job-search"
# # keywords=["python","php"]
# keywords=["python"]
# output_file=open("jobs.txt","w")
# response = requests.get(url,  verify=False)
# soup=BeautifulSoup(response.text,'lxml')
# jobs=soup.find_all("div",{"class":"row company-list joblist"})
# # print(jobs)
# for job in jobs:
#     title_element=job.find("a")
#     title=title_element.text
#     link=title_element["href"]
#     company_name=job.find("div",{"class":"jobs-comp-name"}).text
#     last_date=job.find("div",{"class":"job-date"}).text
#     if any(word.lower() in title.lower() for word in keywords):
#     #   print(title,link,company_name,last_date)
#      output_file.write(title + " "+company_name+" "+last_date+"\n"+link+"\n\n")
# # print(response.text)

