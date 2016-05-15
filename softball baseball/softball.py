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
#read in softball data\
softball_data = pd.read_csv("softball.csv", header=None, dtype=str)\
softball.columns = [\'91Year\'92, \'91SD points\'92, \'91Opp\'92,\'92Difference\'92, \'91Wins\'92]\
\
softball.head(394)\
\
#calculating point differential\
softball['Point_difference'] = softball['SD Points'] - softball['Opp']\
softball.head()\
\
#calcuating win percentage\
columns = ['Total_Games', 'Wins', 'Win_Percentage', 'Percentage']\
results = pd.DataFrame(index=years,columns=columns)\
\
for year in softball[\'91Year\'92]:\
  Total_Games = len(softball[softball['Year'] == year])\
  Wins = len(softball[(softball['Year'] == year) & (softball['Wins'] == 1)])\
  Percentage = softball[softball['Year'] == year][\'91Difference\'92].mean()\
  results.ix[year] = [Total_Games, Wins, float(wins)/float(Total_Games)*100, percentage]\
\
results\
\
#plot data\
results['Win_Percentage\'92].plot(kind='bar')\
\
plt.title('UC San Diego Softball')\
plt.ylabel('Wins')\
plt.xlabel('Seasons')\
\
plt.show()\
}