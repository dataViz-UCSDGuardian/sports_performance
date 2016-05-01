### TO-DO: comment, clean-up, and generalize

import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import os


def scrape(sport_name, first_url, split_results=True):
   page = urllib2.urlopen(first_url)

   soup = BeautifulSoup(page)

   years = []

   form_head = soup.find("td", "sm")
   form = form_head.find("form")

   for opt in form.findAll("option"):
       years.append(opt['value'])
       
   #drop the last 
   base_url = first_url[:-4]

   urls_to_scrape = []

   page = None
   soup = None

   for year in years:
      page_scrape(sport_name, base_url, year, split_results)


def page_scrape(sport_name, base_url, year, split_results=True):
   url = base_url + year

   print(url)

   page = urllib2.urlopen(url)
   soup = BeautifulSoup(page)

   schedule_table = soup.find("table", "ScheduleTable")
   raw_header = [x.getText() for x in schedule_table.findAll("tr")[0].findAll('th')]

   header = [' '.join(x.split()) for x in raw_header]

   data = []

   for row in schedule_table.findAll("tr")[1:]:
       if row.find("td").find("table"):
           pass
       else:
           new_d = []
           for cell in row.findAll("td"):
               new_d.append(' '.join(cell.getText().split()))
           data.append(new_d)

   data = [x for x in data if len(x) != 1 and not all(map(lambda y: y == '', x))]


   df = pd.DataFrame.from_dict(data)

   #our dataframe doesn't have column names yet, let's change that by setting them
   df.columns = header

   #we don't have any values in the Media column, let's get rid of it
   df = df.drop(['Media'],axis=1)

   #make a column to show whether the game was won (1) or lost (0)
   df.loc[ df.Results.str.contains("(W)") , 'Won'] = 1
   df.loc[ df.Results.str.contains("(L)") , 'Won'] = 0

   #make a column to show which games were conference games
   df['Conference'] = 0
   df.loc[ df['Opponent'].str.contains("*",regex=False), 'Conference'] = 1

   if split_results == True:
      results = df['Results'].values

      print results

      if len(results) == 0:
         return

      if all(x=="" for x in results):
         return

      UCSD_results = [int(x.split()[0]) if x != "" else "" for x in results]
      Opp_results = [int(x.split()[2]) if x != "" else "" for x in results]
      print UCSD_results

      df['UCSD Score'] = pd.Series(UCSD_results, index=df.index)
      df['Opp Score'] = pd.Series(Opp_results, index=df.index)

      df = df.drop(['Results'],axis=1)

   df.to_csv(sport_name + "_" + year + ".csv",index=False)