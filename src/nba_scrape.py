from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
import psycopg2
from sqlalchemy import create_engine
import io

engine = create_engine('postgresql://doadmin:a8kz5iiddjdx1fdm@db-postgresql-nyc3-35484-do-user-8902057-0.b.db.ondigitalocean.com:25060/defaultdb?sslmode=require')

def dickbutt(richard_butt, table):
    stats2020.head(0).to_sql(table, engine, if_exists='replace',index=False) #drops old table and creates new empty table
    conn = engine.raw_connection()
    cur = conn.cursor()
    output = io.StringIO()
    stats2020.to_csv(output, sep='\t', header=False, index=False)
    output.seek(0)
    contents = output.getvalue()
    cur.copy_from(output, table, null="") # null values become ''
    conn.commit()



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

dickbutt(stats2020,'t20_21_pergame')

# #2020

#2019
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2019_per_game.html').text
players2019= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2019= pd.DataFrame(players2019, columns = headers)
stats2019.head(10)

dickbutt(stats2019,'t19_20_pergame')
#2019

#2018
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2018_per_game.html').text
players2018= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2018= pd.DataFrame(players2018, columns = headers)
stats2018.head(10)

dickbutt(stats2018,'t18_19_pergame')
#2018

#2017
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2017_per_game.html').text
players2017= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2017= pd.DataFrame(players2017, columns = headers)
stats2017.head(10)

dickbutt(stats2017,'t17_18_pergame')
#2017

#2016
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2016_per_game.html').text
players2016= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2016= pd.DataFrame(players2016, columns = headers)
stats2016.head(10)

dickbutt(stats2016,'t16_17_pergame')
#2016

#2015
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2015_per_game.html').text
players2015= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2015= pd.DataFrame(players2015, columns = headers)
stats2015.head(10)

dickbutt(stats2015,'t15_16_pergame')
#2015

#2014
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2014_per_game.html').text
players2014= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2014= pd.DataFrame(players2014, columns = headers)
stats2014.head(10)

dickbutt(stats2014,'t14_15_pergame')
#2014

#2013
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2013_per_game.html').text
players2013= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2013= pd.DataFrame(players2013, columns = headers)
stats2013.head(10)

dickbutt(stats2013,'t13_14_pergame')
#2013

#2012
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2012_per_game.html').text
players2012= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2012= pd.DataFrame(players2012, columns = headers)
stats2012.head(10)

dickbutt(stats2012,'t12_13_pergame')
#2012

#2011
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2011_per_game.html').text
players2011= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2011= pd.DataFrame(players2011, columns = headers)
stats2011.head(10)

dickbutt(stats2011,'t11_12_pergame')
#2011

#2010
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2010_per_game.html').text
players2010= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2010= pd.DataFrame(players2010, columns = headers)
stats2010.head(10)

dickbutt(stats2010,'t10_11_pergame')
#2010

#2009
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2009_per_game.html').text
players2009= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2009= pd.DataFrame(players2009, columns = headers)
stats2009.head(10)

dickbutt(stats2009,'t09_10_pergame')
#2009

#2008
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2008_per_game.html').text
players2008= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2008= pd.DataFrame(players2008, columns = headers)
stats2008.head(10)

dickbutt(stats2008,'t08_09_pergame')
#2008

#2007
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2007_per_game.html').text
players2007= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2007= pd.DataFrame(players2007, columns = headers)
stats2007.head(10)

dickbutt(stats2007,'t07_08_pergame')
#2007

#2006
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2006_per_game.html').text
players2006= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2006= pd.DataFrame(players2006, columns = headers)
stats2006.head(10)

dickbutt(stats2006,'t06_07_pergame')
#2006

#2005
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2005_per_game.html').text
players2005= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2005= pd.DataFrame(players2005, columns = headers)
stats2005.head(10)

dickbutt(stats2005,'t05_06_pergame')
#2005

#2004
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2004_per_game.html').text
players2004= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2004= pd.DataFrame(players2004, columns = headers)
stats2004.head(10)

dickbutt(stats2004,'t04_05_pergame')
#2004

#2003
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2003_per_game.html').text
players2003= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2003= pd.DataFrame(players2003, columns = headers)
stats2003.head(10)

dickbutt(stats2003,'t03_04_pergame')
#2003

#2002
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2002_per_game.html').text
players2002= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2002= pd.DataFrame(players2002, columns = headers)
stats2002.head(10)

dickbutt(stats2002,'t02_03_pergame')
#2002

#2001
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2001_per_game.html').text
players2001= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2001= pd.DataFrame(players2001, columns = headers)
stats2001.head(10)

dickbutt(stats2001,'t01_02_pergame')
#2001

#2000
source = requests.get('https://www.basketball-reference.com/leagues/NBA_2000_per_game.html').text
players2000= [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats2000= pd.DataFrame(players2000, columns = headers)
stats2000.head(10)

dickbutt(stats2000,'t00_01_pergame')
#2000
cur.close()
conn.close()