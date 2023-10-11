"Method for scraping basic product information"
from datetime import datetime
from .PageObtainer import PageObtainer
from .Parsers.Argos import Argos
from .Parsers.TheEntertainer import TheEntertainer


class StoreScraper():
    "Class for scraping information from web stores"

    def __init__(self):
        "StoreScraper is created with a PageObtainer"
        self.__page_obtainer = PageObtainer()

    def get_information(self, url):
        "Get the information for a given url"
        # Record the start time
        start_datetime = datetime.now().__str__()

        # Factory assign the relevant parser for processing the urls page content
        parser = None
        if "ARGOS.CO.UK" in url.upper():
            parser = Argos()
        elif "THETOYSHOP.COM" in url.upper():
            parser = TheEntertainer()
        else:
            # No parser exists for the given urls
            return {
                "url": url,
                "start_datetime": start_datetime, 
                "end_datetime": datetime.now().__str__(), 
                "status": "fail", 
                "errors": 1, 
                "error_messages": [f"No parser found for url:{url}"]
                }


        #  Get page content
        status, page_content = self.__page_obtainer.get_page(url)

        # Check HTTP Resposne is valid
        if status == 200:
             # Parse Product Information and return values
            return {**{"url": url, 
                       "start_datetime": start_datetime, 
                       "end_datetime": datetime.now().__str__()
                       },
                    **parser.parse(page_content)
                    }

        # return error if HTTP response is not valid
        return {"url": url, 
                "start_datetime": start_datetime, 
                "end_datetime": datetime.now().__str__(), 
                "status": "fail", 
                "errors": 1, 
                "error_messages": [f"status: {status}"]
                }

