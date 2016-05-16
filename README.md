# sports_performance

#####This is a series of 7 visualizations for the UCSD Guardian paper on the ranking of 7 UCSD sports team for the years from 2005 to 2015. 
#####Data Source: 
######Notes on the Data: 
###### * Use the drop down menu to access other years. 
###### * Only CCAA tournament games were considered (indicated with a star). 
* Men's Basketball: http://www.ucsdtritons.com/SportSelect.dbml?&DB_OEM_ID=5800&SPID=2337&SPSID=29886
* Women's Basketball: http://www.ucsdtritons.com/SportSelect.dbml?&DB_OEM_ID=5800&SPID=2338&SPSID=29896
* Men's Soccer: http://www.ucsdtritons.com/SportSelect.dbml?&DB_OEM_ID=5800&SPID=2328&SPSID=29740
* Women's Soccer: http://www.ucsdtritons.com/SportSelect.dbml?DB_OEM_ID=5800&SPID=2339&SPSID=29909&DB_OEM_ID=5800
* Men's Baseball: http://www.ucsdtritons.com/SportSelect.dbml?DB_OEM_ID=5800&SPID=2331&SPSID=29807&DB_OEM_ID=5800
* Women's Baseball: http://www.ucsdtritons.com/SportSelect.dbml?DB_OEM_ID=5800&SPID=2342&SPSID=29937&DB_OEM_ID=5800
* Women's Volleyball: http://www.ucsdtritons.com/SportSelect.dbml?DB_OEM_ID=5800&SPID=2334&SPSID=31944&DB_OEM_ID=5800

#####Process:
1. Data was found on the UCSD sport website under the schedule tab for each team. 
1. Data was scrapped from the site using beautiful soup library. Scrapper information is found under data_scraper folder
1. Four members of the team each took a sport, and worked on making the visualizations individually. Different metrics were used for different teams. 
1. Final product can be found on the website here: 


#####Metrics used:
1. Percent wins: This is the percent of games won out of total games in the season. Used by Basketball, Volleyball
1. Point differential: This is the average of the all points a game was won or lost by. For example, if a team played four games with the scores 10-5 (Win), 4-9(Loss), 3-4(Loss), 13-0(win), the point differential will be the average of ( 5 + -5 + -1 + 13 ). USed by Basketball. 
1. Average Set Matches Won: This is a special metric we made for volleyball that is similar to the point differential in basketball. This is the average of the difference of the number of matches a set was won by or lost by. For example, if a team played 3 gamed with the scores 3-0 (win), 3-1(win), 0-3(Loss), the metric will be the average of ( 3 + 2 + -3). Used by volleyball. 
1. Plotting game results: For soccer, which small point differences and has more ties overall as a sport, plotting the results of the games per year was simple enough. A stacked bar graph that showed number of wins, then ties then losses was used. Used for Soccer. 

