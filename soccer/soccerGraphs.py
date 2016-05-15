import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''   Men's Soccer  '''
data = pd.read_csv('male_csv.csv',
                    error_bad_lines=False,
                    delimiter=',')

win = data['win']
loss = data['loss']
draw = data['draw']
total_game = data['total_game']

width = 0.8
ind = np.arange(11)
plt.figure(figsize=(8,6))

# Stacked bar plots for Male's Soccer
rects1 = plt.bar(ind, win, width, color = 'royalblue')
rects2 = plt.bar(ind, draw, width, bottom = np.array(win), color = 'mediumseagreen')
rects3 = plt.bar(ind, loss, width, bottom = np.array(win) + np.array(draw), color = 'red')

plt.xticks(ind + width/2, ('2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015') )

# Labeling x and y axis
plt.xlabel('Year', fontsize=14, color='black')
plt.ylabel('# of Games', fontsize=14, color='black')
plt.legend([rects1,rects2, rects3], ["Win","Draw","Loss"]);
plt.ylim([0,18])
plt.title("Men's Soccer Statistics (2005 - 2015)", fontsize = 15)
plt.savefig('Men_soccer.png')

plt.show()




'''   Women's Soccer  '''
female_data = pd.read_csv('female_csv.csv',
                    error_bad_lines=False,
                    delimiter=',')

w = female_data['win']
d = female_data['draw']
tg = female_data['total_game']
l = female_data['loss']

# Stacked bar plots for Female's Soccer
rects1 = plt.bar(ind, w, width, color = 'royalblue')
rects2 = plt.bar(ind, d, width, bottom = np.array(w), color = 'mediumseagreen')
rects3 = plt.bar(ind, l, width, bottom = np.array(w) + np.array(d), color = 'red')

plt.xticks(ind + width/2, ('2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015') )

# Labeling x and y axis
plt.xlabel('Year', fontsize=14, color='black')
plt.ylabel('# of Games', fontsize=14, color='black')
plt.legend([rects1,rects2, rects3], ["Win","Draw","Loss"]);
plt.ylim([0,18])
plt.title("Women's Soccer Statistics (2005 - 2015)", fontsize = 15)
plt.savefig('Women_soccer.png')
plt.show()
