from PageObtainer import PageObtainer
from Parsers.Argos import Argos
from Parsers.TheEntertainer import TheEntertainer
from datetime import datetime

class StoreScraper():

    def __init__(self):
        "StoreScraper is created with a PageObtainer"
        self.page_obtainer = PageObtainer()

    def get_information(self, url):
        "Get the information for a given url"
        # Record the start time
        start_datetime = datetime.now().__str__()

        # Factory assign the relevant parser for processing the urls page content
        parser = None
        if("ARGOS.CO.UK" in url.upper()):
            parser = Argos()
        elif("THETOYSHOP.COM" in url.upper()):
            parser = TheEntertainer()
        else:
            # No parser exists for the given urls
            return {"url": url, "start_datetime": start_datetime, "end_datetime": datetime.now().__str__(), "status": "fail", "errors": 1, "error_messages": [f"No parser found for url:{url}"]}


        #  Get page content
        status, page_content = self.page_obtainer.get_page(url)

        if(status != 200):
            # return error if fails to get page content
            return {"url": url, "start_datetime": start_datetime, "end_datetime": datetime.now().__str__(), "status": "fail", "errors": 1, "error_messages": [f"status: {status}"]}
        else:
            # Parse Product Information and return values
            return {**{"url": url, "start_datetime": start_datetime, "end_datetime": datetime.now().__str__()} , **parser.parse(page_content)}
