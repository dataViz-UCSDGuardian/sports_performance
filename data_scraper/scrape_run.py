def main():
   import sports_scraper as s

   s.scrape("baseball","http://www.ucsdtritons.com/SportSelect.dbml?SPSID=29807&SPID=2331&DB_OEM_ID=5800&Q_SEASON=2014",False)

   #s.scrape("softball","http://www.ucsdtritons.com/SportSelect.dbml?SPSID=29937&SPID=2342&DB_OEM_ID=5800&Q_SEASON=2014",False)

   #s.scrape("men_basketball","http://www.ucsdtritons.com/SportSelect.dbml?SPSID=29886&SPID=2337&DB_OEM_ID=5800&Q_SEASON=2014")

   #s.scrape("women_basketball","http://www.ucsdtritons.com/SportSelect.dbml?SPSID=29896&SPID=2338&DB_OEM_ID=5800&Q_SEASON=2005")

   #s.scrape("men_volleyball","http://www.ucsdtritons.com/SportSelect.dbml?SPSID=29875&SPID=2336&DB_OEM_ID=5800&Q_SEASON=2014",False)

   #s.scrape("women_volleyball","http://www.ucsdtritons.com/SportSelect.dbml?SPSID=31944&SPID=2334&DB_OEM_ID=5800&Q_SEASON=2012")

   #s.scrape("men_soccer","http://www.ucsdtritons.com/SportSelect.dbml?SPSID=29740&SPID=2328&DB_OEM_ID=5800&Q_SEASON=2012",False)

   #s.scrape("women_soccer","http://www.ucsdtritons.com/SportSelect.dbml?SPSID=29909&SPID=2339&DB_OEM_ID=5800&Q_SEASON=2015",False)

if __name__ == "__main__":
   main()