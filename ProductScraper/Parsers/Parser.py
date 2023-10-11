"Parse web pages, returned in a standard format"
from iParser import iParser

class Parser(iParser):

    def __init__(self, parser="Unknown"):
        self.PARSER = parser
        self.item_name = None
        self.category_one = None
        self.category_two = None
        self.category_three = None
        self.price = None
        self.image = None
        self.status = None
        self.error_messages = []


    # Method for processing the page contents
    def parse(self, page_content):
        "Child classes must implement this method to process page_content and set values"
        raise NotImplementedError('users must define parse() to use this base class')


    def return_information(self):
        "Return information in a standard form"
        
        return {
            "status": self.get_status(),
            "errors": len(self.get_error_messages()),
            "error_messages": self.get_error_messages(),
            "parser": self.get_store(),
            "item_name": self.get_item_name(),
            "category_one": self.get_category_one(),
            "category_two": self.get_category_two(),
            "category_three": self.get_category_three(),
            "price": self.get_price(),
            "image_url": self.get_image()
        }
    
    def add_error_message(self, message):
        "Append error messages"
        self.error_messages.append(message)
    
    # Implement Interface Methods    
    def get_store(self):
        return self.PARSER

    def get_item_name(self):
        return self.item_name

    def get_category_one(self):
        return self.category_one
    
    def get_category_two(self):
        return self.category_two

    def get_category_three(self):
        return self.category_three

    def get_price(self):
        return self.price

    def get_image(self):
        return self.image
    
    def get_status(self):
        if(len(self.get_error_messages()) == 0):
            return "success"
        else:
            return "error"
    
    def get_error_messages(self):
        return self.error_messages
    
