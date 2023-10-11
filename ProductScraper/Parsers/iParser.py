"Interface for Parser"
from abc import ABCMeta, abstractmethod

class iParser(metaclass=ABCMeta):
    @abstractmethod
    def return_information(self):
        "return a information in a standard form"

    @abstractmethod
    def get_store(self):
        "Return the store"

    @abstractmethod
    def get_item_name(self):
        "Return the products name"

    @abstractmethod
    def get_category_one(self):
        "Return category 1"
    
    @abstractmethod
    def get_category_two(self):
        "Return category 1"
    
    @abstractmethod
    def get_category_three(self):
        "Return category 2"

    @abstractmethod
    def get_price(self):
        "Return the products price"

    @abstractmethod
    def get_image(self):
        "Return the products image url"

    @abstractmethod
    def get_status(self):
        "Return the products image url"

    @abstractmethod
    def get_error_messages(self):
        "Return the products image url"




