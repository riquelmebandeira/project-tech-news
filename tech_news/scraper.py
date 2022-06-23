import time
import requests
from requests.exceptions import HTTPError, ReadTimeout
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"})

        if not response.status_code == 200:
            response.raise_for_status()

    except (ReadTimeout, HTTPError):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)

    links = selector.css(".entry-title a::attr(href) ").getall()

    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
