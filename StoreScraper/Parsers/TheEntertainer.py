"Inherits Parser, processing www.argos.co.uk"
from .Parser import Parser


class TheEntertainer(Parser):
    "Parser for processing TheToyShop.com"

    def __init__(self):
        super().__init__(parser="TheEntertainer")    
        self.page_content = None

    # Get item information from the website
    def __set_item_name(self):
        "Set the product name"
        try:
            self.item_name = self.page_content.select("h1")[0].text
        except:
            super().add_error_message("item_name: fail")

    def __set_categories(self):
        "Set product categories"
        try:
            category_elements = self.page_content.select("ol.breadcrumb")[0].findAll("a")

            for category_id in range (2, len(category_elements)):
                if category_id <= len(category_elements):
                    match category_id:
                        case 2: self.category_one = category_elements[category_id].text
                        case 3: self.category_two = category_elements[category_id].text
                        case 4: self.category_three = category_elements[category_id].text
        except:
            super().add_error_message("item_name: fail")

    def __set_price(self):
        "Set price of product"
        try:
            self.price = self.page_content.select(".price span")[0].text      
        except:
            super().add_error_message("item_name: fail")

    def __set_image(self):
        "Get the primary image url"
        try:
            self.image = f"https://www.thetoyshop.com{self.page_content.select('.lazyOwl')[0]['src']}"      
        except:
            super().add_error_message("item_name: fail")

    # Process page content
    def parse(self, page_content):
        self.page_content = page_content

        # Get information from page content.
        self.__set_item_name()
        self.__set_categories()
        self.__set_price()
        self.__set_image()

        # Return Information using a parent method
        return super().return_information()
