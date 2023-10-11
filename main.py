from ProductScraper.StoreScraper import StoreScraper

if __name__ == "__main__":
    scraper = StoreScraper()
    results = scraper.get_information("https://www.argos.co.uk/product/8992866?clickSR=slp:term:superman:3:6:1")
    print(results)
    results = scraper.get_information("https://www.thetoyshop.com/collectibles/adult-collectibles/DC-Comics-30cm-Superman-Figure/p/545842?queryId=83dec2295943aff8586c518c6f031006")
    print(results)