from tech_news.database import search_news
from utils.index import (
    get_news_title_and_url,
    validate_date_format,
)


# Requisito 6
def search_by_title(title):
    news = list(search_news({"title": {"$regex": title, "$options": "i"}}))

    return get_news_title_and_url(news)


# Requisito 7
def search_by_date(date):
    query = validate_date_format(date)

    news = list(search_news({"timestamp": query}))

    return get_news_title_and_url(news)


# Requisito 8
def search_by_tag(tag):
    news = list(
        search_news({"tags": {"$elemMatch": {"$regex": tag, "$options": "i"}}})
    )

    return get_news_title_and_url(news)


# Requisito 9
def search_by_category(category):
    news = list(
        search_news({"category": {"$regex": category, "$options": "i"}})
    )

    return get_news_title_and_url(news)
