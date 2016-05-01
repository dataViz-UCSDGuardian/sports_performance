def main():
   import sports_scraper as s

   #s.scrape("baseball","http://www.ucsdtritons.com/SportSelect.dbml?SPSID=31944&SPID=2334&DB_OEM_ID=5800&Q_SEASON=2016")

   #s.scrape("softball","http://www.ucsdtritons.com/SportSelect.dbml?SPSID=29937&SPID=2342&DB_OEM_ID=5800&Q_SEASON=2014")

   #s.scrape("men_basketball","http://www.ucsdtritons.com/SportSelect.dbml?SPSID=29886&SPID=2337&DB_OEM_ID=5800&Q_SEASON=2014")

   #s.scrape("women_basketball","http://www.ucsdtritons.com/SportSelect.dbml?SPSID=29896&SPID=2338&DB_OEM_ID=5800&Q_SEASON=2005")

   #s.scrape("men_volleyball","http://www.ucsdtritons.com/SportSelect.dbml?SPSID=29875&SPID=2336&DB_OEM_ID=5800&Q_SEASON=2014")

   s.scrape("women_volleyball","http://www.ucsdtritons.com/SportSelect.dbml?SPSID=31944&SPID=2334&DB_OEM_ID=5800&Q_SEASON=2012")

if __name__ == "__main__":
   main()