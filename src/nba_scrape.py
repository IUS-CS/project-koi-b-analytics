from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

#2020
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2020_per_game.html').text

soup = BeautifulSoup(source, 'lxml')

soup.findAll('tr', limit=2)
headers = [th.getText() for th in soup.findAll('tr', limit=2)
           [0].findAll('th')]
headers = headers[1:]
#print(headers)

rows = soup.findAll('tr')[1:]
players2020 = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2020 = pd.DataFrame(players2020, columns = headers)
stats2020.head(10)

stats2020.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2020Stats.csv', index = False, header=True)
print(stats2020)
#2020

#2019
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2019_per_game.html').text
players2019= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2019= pd.DataFrame(players2019, columns = headers)
stats2019.head(10)

stats2019.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2019Stats.csv', index = False, header=True)
print(stats2019)
#2019

#2018
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2018_per_game.html').text
players2018= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2018= pd.DataFrame(players2018, columns = headers)
stats2018.head(10)

stats2018.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2018Stats.csv', index = False, header=True)
print(stats2018)
#2018

#2017
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2017_per_game.html').text
players2017= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2017= pd.DataFrame(players2017, columns = headers)
stats2017.head(10)

stats2017.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2017Stats.csv', index = False, header=True)
print(stats2017)
#2017

#2016
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2016_per_game.html').text
players2016= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2016= pd.DataFrame(players2016, columns = headers)
stats2016.head(10)

stats2016.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2016Stats.csv', index = False, header=True)
print(stats2016)
#2016

#2015
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2015_per_game.html').text
players2015= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2015= pd.DataFrame(players2015, columns = headers)
stats2015.head(10)

stats2015.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2015Stats.csv', index = False, header=True)
print(stats2015)
#2015

#2014
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2014_per_game.html').text
players2014= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2014= pd.DataFrame(players2014, columns = headers)
stats2014.head(10)

stats2014.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2014Stats.csv', index = False, header=True)
print(stats2014)
#2014

#2013
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2013_per_game.html').text
players2013= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2013= pd.DataFrame(players2013, columns = headers)
stats2013.head(10)

stats2013.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2013Stats.csv', index = False, header=True)
print(stats2013)
#2013

#2012
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2012_per_game.html').text
players2012= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2012= pd.DataFrame(players2012, columns = headers)
stats2012.head(10)

stats2012.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2012Stats.csv', index = False, header=True)
print(stats2012)
#2012

#2011
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2011_per_game.html').text
players2011= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2011= pd.DataFrame(players2011, columns = headers)
stats2011.head(10)

stats2011.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2011Stats.csv', index = False, header=True)
print(stats2011)
#2011

#2010
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2010_per_game.html').text
players2010= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2010= pd.DataFrame(players2010, columns = headers)
stats2010.head(10)

stats2010.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2010Stats.csv', index = False, header=True)
print(stats2010)
#2010

#2009
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2009_per_game.html').text
players2009= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2009= pd.DataFrame(players2009, columns = headers)
stats2009.head(10)

stats2009.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2009Stats.csv', index = False, header=True)
print(stats2009)
#2009

#2008
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2008_per_game.html').text
players2008= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2008= pd.DataFrame(players2008, columns = headers)
stats2008.head(10)

stats2008.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2008Stats.csv', index = False, header=True)
print(stats2008)
#2008

#2007
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2007_per_game.html').text
players2007= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2007= pd.DataFrame(players2007, columns = headers)
stats2007.head(10)

stats2007.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2007Stats.csv', index = False, header=True)
print(stats2007)
#2007

#2006
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2006_per_game.html').text
players2006= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2006= pd.DataFrame(players2006, columns = headers)
stats2006.head(10)

stats2006.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2006Stats.csv', index = False, header=True)
print(stats2006)
#2006

#2005
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2005_per_game.html').text
players2005= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2005= pd.DataFrame(players2005, columns = headers)
stats2005.head(10)

stats2005.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2005Stats.csv', index = False, header=True)
print(stats2005)
#2005

#2004
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2004_per_game.html').text
players2004= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2004= pd.DataFrame(players2004, columns = headers)
stats2004.head(10)

stats2004.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2004Stats.csv', index = False, header=True)
print(stats2004)
#2004

#2003
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2003_per_game.html').text
players2003= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2003= pd.DataFrame(players2003, columns = headers)
stats2003.head(10)

stats2003.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2003Stats.csv', index = False, header=True)
print(stats2003)
#2003

#2002
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2002_per_game.html').text
players2002= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2002= pd.DataFrame(players2002, columns = headers)
stats2002.head(10)

stats2002.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2002Stats.csv', index = False, header=True)
print(stats2002)
#2002

#2001
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2001_per_game.html').text
players2001= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2001= pd.DataFrame(players2001, columns = headers)
stats2001.head(10)

stats2001.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2001Stats.csv', index = False, header=True)
print(stats2001)
#2001

#2000
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2000_per_game.html').text
players2000= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2000= pd.DataFrame(players2000, columns = headers)
stats2000.head(10)

stats2000.to_csv (r'C:\Users\Aaron\Desktop\Project\project-koi-b-analytics\data\2000Stats.csv', index = False, header=True)
print(stats2000)
#2000
