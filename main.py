
import requests
from bs4 import BeautifulSoup


url = 'https://www.worldometers.info/coronavirus/'
html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "lxml")
#print(soup.prettify())

data = {}
##//*[@id="main_table_countries_today"]/tbody[1]
#covid_table = soup.find_all(attrs={"id": "main_table_countries_today"})
covid_table = soup.find('table', {'id':'main_table_countries_today'})
table_body = covid_table.find('tbody')

covid_table_data = covid_table.tbody.find_all('tr')
headers = covid_table.find_all('th')


for th in headers:
    th_cols = covid_table.find_all('th')
    th_cols = [ele.text.strip() for ele in th_cols]

#print(th_cols)

rows = table_body.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    #print(th_cols[1],":",cols[1])
    #print("=====")
    #data.append([ele for ele in cols])
    #print(cols)
    data[cols[1]] = {}
    data1 = []
    for i in range(1, len(th_cols)):
        #print(th_cols[i], ":", cols[i])
        a = [th_cols[i], cols[i]]
        data1.append(a)
    #print(data1)
    data[cols[1]] = data1
    #print("==========")
#print(headers[1])
print(data['USA'])
print(data['UK'])
#print(covid_table)


#print(covid_table_data)

