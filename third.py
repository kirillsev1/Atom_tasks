from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def get_soup(url: str) -> BeautifulSoup:
    """Function which parses html page.

    Args:
        url: str - string url on html page.

    Returns:
        BeautifulSoup - object of class BeautifulSoup which can be used to get info about tags.
    """
    req = Request(
        url=url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    webpage = urlopen(req).read()
    return BeautifulSoup(webpage, 'html.parser')


def count_tags(url: str) -> int:
    """Function finds number of tags in html page.

    Args:
        url: str - ulr on html page.

    Returns:
        int - sum of all the tags.
    """
    hashmap = {}
    soup = get_soup(url)
    for tag in soup.find_all():
        if tag.name not in hashmap:
            hashmap[tag.name] = 0
        hashmap[tag.name] += 1
    print(hashmap)
    return sum(hashmap.values())


def count_tags_attrs(url: str) -> int:
    """Function finds number of attributes of tags in html page.

        Args:
            url: str - ulr on html page.

        Returns:
            int - sum of all the attributes of tags.
        """
    hashmap = {}
    soup = get_soup(url)
    for tag in soup.find_all():
        if tag.attrs:
            if tag.name not in hashmap:
                hashmap[tag.name] = 0
            hashmap[tag.name] += 1
    print(hashmap)
    return sum(hashmap.values())


if __name__ == '__main__':
    url_value = 'https://greenatom.ru'
    print(count_tags(url_value))
    print(count_tags_attrs(url_value))
