"Obtains the content of a web page using response"
from curl_cffi import requests
from bs4 import BeautifulSoup


class PageObtainer():

    def __init__(self, impersonate_browser="chrome110"):
        "Create a requests session"
        self.__session: requests.session = requests.Session()
        self.__impersonate_browser = impersonate_browser

    # Return the page 
    def get_page(self, url) -> tuple[int, str]:
        "Return the html of a web page"
        r: requests.Response = None

        #Handle connection issues
        try:
            r = self.__session.get(url, impersonate=self.__impersonate_browser, timeout=5)
        except requests.RequestsError as e:
            return 408, f"WebScraper(): {e}"

        return r.status_code, BeautifulSoup(r.content, "html.parser")
