# StoreScraper
## Description
This library will allow you to scrape "basic" product information from online retailers, including the products name, price, categories and primary image.

### Suported Websites
- https://www.argos.co.uk
- https://thetoyshop.com
## Basic UML Diagram
![UML Diagram](UML.png)

## Usage
An example can be found in main.py

The below code scrapes two stores and prints out the results
```python
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
```

### Result 1 Output                         
>{'url': 'https://www.argos.co.uk/product/8992866', 'start_datetime': '2023-10-11 19:55:14.920228', 'end_datetime': '2023-10-11 19:55:15.296868', 'status': 'success', 'errors': 0, 'error_messages': [], 'parser': 'Argos', 'item_name': 'DC 12-inch Superman Figure', 'category_one': None, 'category_two': None, 'category_three': None, 'price': '£10.00', 'image_url': '//media.4rgos.it/i/Argos/8992866_R_Z001A?w=750&h=440&qlt=70'}

### Result 2 Output
>{'url': 'https://www.thetoyshop.com/collectibles/adult-collectibles/DC-Comics-30cm-Superman-Figure/p/545842?queryId=83dec2295943aff8586c518c6f031006', 'start_datetime': '2023-10-11 19:55:15.328904', 'end_datetime': '2023-10-11 19:55:15.604712', 'status': 'success', 'errors': 0, 'error_messages': [], 'parser': 'TheEntertainer', 'item_name': 'DC Comics 30cm Superman Figure', 'category_one': 'Collectible Toys', 'category_two': 'Adult Collectibles', 'category_three': None, 'price': '£10.00', 'image_url': 'https://www.thetoyshop.com/medias/545842-Primary-515Wx515H?context=bWFzdGVyfGltYWdlc3wzNzgxM3xpbWFnZS9qcGVnfGFXMWhaMlZ6TDJnNE55OW9PRFF2T1RJeE9ESTVPRFV4TVRNNU1DNXFjR2N8NmYxOGNkNmIwZWYxNjE0YzVjZWU5N2FhNGRiZGIyMmM0Zjk0NmY4NDhiNzU3YTc3MWVkODkwZWM4NDllNjA1ZA'}   
