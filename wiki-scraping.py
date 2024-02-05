from bs4 import BeautifulSoup
import requests

url = 'https://en.m.wikipedia.org/wiki/List_of_largest_companies_in_India'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')
table = soup.find_all('table')[0]
headers_temp = table.find_all('th')
headers = [header.text.strip() for header in headers_temp]
print(headers)


######### Creating dataframes and adding headers
import pandas as pd

df = pd.DataFrame(columns = headers)
# df
rows = table.find_all('tr')


######### Data Entry in the dataframe
for i in range(1,len(rows)):
    data_temp = rows[i].find_all('td')
    row = [data.text.strip() for data in data_temp]
    row.remove(row[1])
    row.remove(row[2])

    df.loc[len(df.index)] = row



# data_temp = rows[1].find_all('td')
# row = [data.text.strip() for data in data_temp]
# print(row)

# len(df.index)
    

######### Saving to csv file
df.to_csv(r'C:\Users\saura\Downloads\Top-Companies.csv', index=False)