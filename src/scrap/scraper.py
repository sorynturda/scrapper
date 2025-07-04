# scraper.py

import http
from bs4 import BeautifulSoup
from urllib.request import urlopen

base_url = "https://ro.wikipedia.org/wiki/"


def get_info(input: str) -> list:
    """
    Scrap a wikipedia page

    Args:
        input (str): wikipedia page

    Returns:
        list:
            list where first element is the scraped text and second is a number if page exists
            otherwise one element list with an error message

    """

    try:
        page = urlopen(base_url + input)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        paras = soup.find_all("p", class_="")

        last_edit = "Ultima editare a paginii a fost efectuată la "
        idx = soup.text.index(last_edit) + len(last_edit)
        last_edit_date = int(soup.text[idx : idx + 2])
        text_to_save = ""
        for p in paras[:3]:
            text = p.text.strip(" \r\n\t")
            if text == "":
                continue
            text_to_save += text + "\n"
        return [text_to_save, last_edit_date]
    except Exception as e:
        print(str(e))
        raise http.HTTPStatus.NOT_FOUND
