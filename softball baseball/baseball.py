{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf460
{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl280\partightenfactor0

\f0\fs24 \cf0 \expnd0\expndtw0\kerning0
import pandas as pd\
from matplotlib import pyplot as plt\
from matplotlib import style\
%matplotlib inline\
style.use('ggplot')\
\
#read in baseball data\
baseball_data = pd.read_csv(\'93baseball.csv", header=None, dtype=str)\
baseball.columns = [\'91Year\'92, \'91SD points\'92, \'91Opp\'92,\'92Difference\'92,\'92Wins\'92]\
\
baseball.head(388)\
\
\
#calcuating win percentage\
columns = ['Total_Games', 'Wins', 'Win_Percentage', 'Percentage']\
results = pd.DataFrame(index=years,columns=columns)\
\
for year in baseball[\'91Year\'92]:\
  Total_Games = len(baseball[baseball[\'91Year'] == year])\
  Wins = len(baseball[(baseball[\'91Year'] == year) & (baseball[\'91Wins'] == 1)])\
  Percentage = baseball[baseball[\'91Year'] == year][\'91Difference\'92].mean()\
  results.ix[year] = [Total_Games, Wins, float(wins)/float(Total_Games)*100, percentage]\
\
results\
\
#plot data\
results['Win_Percentage\'92].plot(kind='bar')\
\
plt.title('UC San Diego Baseball\'92)\
plt.ylabel('Wins')\
plt.xlabel('Seasons')\
\
plt.show()\
}