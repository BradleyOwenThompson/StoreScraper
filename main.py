"Example using Argos and TheEntertainer"
from ProductScraper.StoreScraper import StoreScraper

scraper = StoreScraper()

result1 = scraper.get_information("https://www.argos.co.uk/product/8992866")

result2 = scraper.get_information("https://www.thetoyshop.com/collectibles/adult-collectibles/DC-C"
                                  "omics-30cm-Superman-Figure/p/545842?queryId=83dec2295943aff8586"
                                  "c518c6f031006"
                                  )

print(result1)
print(result2)
