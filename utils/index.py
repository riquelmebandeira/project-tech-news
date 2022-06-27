from collections import namedtuple
import re


months = {
    "01": "janeiro",
    "02": "fevereiro",
    "03": "março",
    "04": "abril",
    "05": "maio",
    "06": "junho",
    "7": "julho",
    "8": "agosto",
    "09": "setembro",
    "10": "outubro",
    "11": "novembro",
    "12": "dezembro",
}

Date = namedtuple("Date", "year month day")


def validate_date_format(date):
    try:
        valid_format = r"\d{4}-\d{2}-\d{2}"

        match = re.search(valid_format, date)

        if not match:
            raise ValueError

        year, month, day = Date(*date.split("-"))

        if month == '02' and int(day) > 28:
            raise ValueError

        return f"{day.strip('0')} de {months[month]} de {year}"

    except (KeyError, ValueError):
        raise ValueError("Data inválida")


def get_news_title_and_url(news):
    return [(n["title"], n["url"]) for n in news]
