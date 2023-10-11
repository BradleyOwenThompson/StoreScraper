"Inherits Parser, processing www.argos.co.uk"
from .Parser import Parser


class Argos(Parser):
    "Parser for process www.argos.co.uk"

    def __init__(self):
        super().__init__(parser="Argos")
        self.page_content = None

    # Get item information from the website
    def __set_item_name(self):
        "Set the product name"
        try:
            self.item_name = self.page_content.select(".h2 span:nth-child(1)")[0].text
        except:
            super().add_error_message("item_name: fail")

    def __set_categories(self):
        "Set product category"
        try:
            category_elements = self.page_content.findAll("li", {"data-test":
                                                                 "component-breadcrumb-item"})

            for category_id, category in enumerate(category_elements):
                if category_id <= len(category_elements):
                    match id:
                        case 0: self.category_one = category.text
                        case 1: self.category_two = category.text
                        case 2: self.category_three = category.text
        except:
            super().add_error_message("category: fail")

    def __set_price(self):
        "Set the price of product"
        try:
            self.price = self.page_content.select(".hYxevI h2")[0].text
        except:
            super().add_error_message("price: fail")

    def __set_image(self):
        "Get the primary image url"
        try:
            self.image = self.page_content.select(".eDqOMU img")[0]['src']
        except:
            super().add_error_message("image: fail")

    def parse(self, page_content):
        "Process the page content"
        self.page_content = page_content

        # Get information from page.
        self.__set_item_name()
        self.__set_categories()
        self.__set_price()
        self.__set_image()

        # Return Information using a parent method
        return super().return_information()
