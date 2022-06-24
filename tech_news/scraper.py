import time
import requests
from requests.exceptions import HTTPError, ReadTimeout
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )

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
    selector = Selector(text=html_content)

    next_page_link = selector.css(".next::attr(href) ").get()

    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    news_details = {
        "url": selector.css("link[rel='canonical']::attr(href)").get(),
        "title": selector.css(".entry-title::text").get(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".author a::text").get(),
        "summary": selector.xpath("string(//p)").get(),
        "comments_count": 0,
        "tags": selector.css("a[rel='tag']::text").getall(),
        "category": selector.css(".label::text").get(),
    }

    return news_details


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
