import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import glob

path =r'../data/volleyball_women'
all_files = glob.glob(path + "/*.csv")

years = []
for item in all_files:
	 years.append(item[-8:-4:])

frames = []

for year in years:
	 path_name = path + "/women_volleyball_" + year + ".csv"
	 df = pd.read_csv(path_name, index_col=None,header=0)
	 df['Year'] = year
	 frames.append(df)

data = pd.concat(frames, ignore_index=True)
data = data[data.Conference == 1]
data['Score_diff'] = data['UCSD Score'] - data['Opp Score']

columns = ['Played','Won','Percent Won','Set Diff Avg','UCSD Sets Avg']
summary = pd.DataFrame(index=years,columns=columns)

for year in years:
	 played = len(data[data['Year'] == year])
	 won = len(data[ (data['Year'] == year) & (data['Won'] == 1) ])
	 score_diff_avg = data[data['Year'] == year]['Score_diff'].mean()
	 ucsd_score_avg = data[data['Year'] == year]['UCSD Score'].mean()
	 summary.ix[year] = [played, won, float(won)/float(played)*100, score_diff_avg, ucsd_score_avg]

print summary


#PLOTTING

fig, ax1 = plt.subplots()
t = np.arange(2005, 2016, 1)
s1 = summary['Percent Won'].values

ax1.plot(t, s1, 'b-',linewidth=2.5)
ax1.set_xlabel('year')

# Make the y-axis label and tick labels match the line color.
ax1.set_ylabel('win percentage', color='b')
for tl in ax1.get_yticklabels():
    tl.set_color('b')

years = [int(x) for x in years]
    
x = range(0,len(years))
ps = range(0,110,10)

axes = plt.gca()
axes.set_ylim([0,100])
plt.yticks(ps)
    
ax2 = ax1.twinx()
s2 = summary['Set Diff Avg'].values

ax2.plot(t, s2, 'r-',linewidth=2.5)
ax2.set_ylabel('avg # of sets matches were won/lost by', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')

ax1.set_xticks(years)
#ax2.set_xticks()    

plt.title("Women's Volleyball Statistics (2005 - 2015)", fontsize = 15)
plt.savefig('Women_volleyball.png')
plt.show()




