from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2020_per_game.html').text

soup = BeautifulSoup(source, 'lxml')

soup.findAll('tr', limit=2)
headers = [th.getText() for th in soup.findAll('tr', limit=2)
           [0].findAll('th')]
headers = headers[1:]
#print(headers)

rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats = pd.DataFrame(player_stats, columns = headers)
stats.head(10)

stats.to_csv (r'C:\Users\Aaron\Documents\School\IUS\2020\Fall\B438 - DOYLE\NBA Project\export_dataframe.csv', index = False, header=True)
print(stats)
