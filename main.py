import tkinter as tk
import time
import requests
from bs4 import BeautifulSoup
import datetime



master = tk.Tk()
master.title("Covid Numbers")
x=1

soup_attrib = "id"
soup_value = ["main_table_countries_yesterday2","main_table_countries_yesterday","main_table_countries_today"]
display_countries = ['USA', 'UK', 'Spain', 'Poland']



url = 'https://www.worldometers.info/coronavirus/'

#print(soup.prettify())


##//*[@id="main_table_countries_today"]/tbody[1]
#covid_table = soup.find_all(attrs={"id": "main_table_countries_today"})
#covid_table = soup.find('table', {'id':'main_table_countries_today'})
while(x == 1):
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    now = datetime.datetime.now()
    for iteration in range(0, len(soup_value)):
        data = {}
        soup_find = {soup_attrib: soup_value[iteration]}
        print(soup_find)
        covid_table = soup.find('table', soup_find)

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
    for display in range (0,len(display_countries)):
        display_data = display_countries[display] + str(data[display_countries[display]][2]) + " " + str(data[display_countries[display]][4])
        tk.Label(master, text=display_data).grid(row=display+1)
    #datal1= "USA" + str(data['USA'][2]) + " " + str(data['USA'][4])
    #datal2= "UK" + str(data['UK'][2]) + " " + str(data['UK'][4])
    print("Current date and time : ")

    lasttime = now.strftime("Last updated - %Y-%m-%d %H:%M:%S")
    print(lasttime)

    tk.Label(master, text=lasttime).grid(row=0)
    #tk.Label(master, text=datal1).grid(row=1)
    #tk.Label(master, text=datal2).grid(row=2)

    #e1 = tk.Entry(master)
    #e2 = tk.Entry(master)



    #master.mainloop()
    master.update()
    time.sleep(300)


