""" Scrape argos product page """

from multiprocessing import Pool

import re
import datetime
import requests

from bs4 import BeautifulSoup


def get_product_details(url):
    """ Returns a dictionary containing product page information """

    # Record process start datetime
    datetime_start = datetime.datetime.now()

    # Wrap in a catch, informing us if was successful
    try:
        # Set a browser header
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            ' (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
        }

        # Get page content using Requests and BS4
        page = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(page.content, "html.parser")

        # Get elements of the page
        clean_url = get_url(url)
        product_id = get_product_id(url)
        breadcrumbs = get_breadcrumb(soup)
        product_name = get_name(soup)
        product_price = get_price(soup)

    except Exception:
        # Return if error occurs
        return {
            "datetime_start": f"{datetime_start}",
            "datetime_end": f"{datetime.datetime.now()}",
            "search_url": url,
            "status": "Fail"
        }

    # Return if successful
    return {
        "datetime_start": f"{datetime_start}",
        "datetime_end": f"{datetime.datetime.now()}",
        "search_url": url,
        "clean_url": clean_url,
        "id": product_id,
        "product": product_name,
        "breadcrumb-l0": breadcrumbs[0],
        "breadcrumb-l1": breadcrumbs[1],
        "breadcrumb-l2": breadcrumbs[2],
        "breadcrumb-l3": breadcrumbs[3],
        "breadcrumb-l4": breadcrumbs[4],
        "price-currency": product_price[0],
        "price-tag": product_price[1],
        "price-text": product_price[2]
    }


def get_product_details_parallel(urls):
    """ Returns a list of dictionaries containing product page information Running multiple 
    processes in parallel """

    # Record process start datetime
    datetime_start = datetime.datetime.now()

    with Pool() as pool:
        results = pool.map(get_product_details, urls)

    audit = {"datetime_start": f"{datetime_start}",
             "datetime_end": f"{datetime.datetime.now()}"}

    return results, audit


def get_url(url):
    """ Return a "tidied" url using REGEX, removing trailing information after the product id """

    pattern = r"https:\/\/www\.argos\.co\.uk\/product\/\d*"
    match = re.search(pattern, url)

    if match:
        return match.group(0)

    return None


def get_product_id(url) -> str:
    """ Return the product id from the url, using REGEX"""

    pattern = r"(?<=product\/)\d+"
    match = re.search(pattern, url)
    if match:
        return match.group(0)

    return None


def get_name(content) -> str:
    """ Return the product name """

    return content.findAll("span", {"itemprop": "name", "data-test": "product-title"})[0].text


def get_price(content) -> list:
    """ Return the product price """

    price_element = content.findAll("li", {"itemprop": "price"})
    price_currency = content.findAll("span", {"itemprop": "priceCurrency"})

    return [price_currency[0]['content'], price_element[0]['content'], price_element[0].text]


def get_breadcrumb(content) -> str:
    """ Return breadcrumb, limited to 5 items """

    breadcrumbs_elements = content.findAll(
        "li", {"data-test": "component-breadcrumb-item"})

    breadcrumbs = [None for i in range(5)]
    for item, crumb in enumerate(breadcrumbs_elements[:-1]):
        breadcrumbs[item] = crumb.text

    return breadcrumbs


# Main module
if __name__ == '__main__':

    # Run scraping in batches
    BATCH_SIZE = 2

    urls = [
        "https://www.argos.co.uk/product/8448262",
        "https://www.argos.co.uk/product/4562647?clickCSR=slp:cannedSearch",
        "https://www.argos.co.uk/product/3361227?clickCSR=slp:cannedSearch",
        "https://www.argos.co.uk/product/3289725?clickCSR=slp:cannedSearch"
    ]

    batched_urls = [urls[i:i+BATCH_SIZE]
                    for i in range(0, len(urls), BATCH_SIZE)]

    for batch in batched_urls:
        print(get_product_details_parallel(batch))

    # print(get_product_details("https://www.argos.co.uk/product/3447426?clickPR=plp:1:334"))
