import requests
from bs4 import BeautifulSoup as bs


def parse_wiki():
    url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
    response = requests.get(url)
    soup = bs(response.content, 'html.parser')
    table = soup.find('table', 'wikitable sortable')
    table_full = []

    for tr in table.find_all('tr'):
        table_full.append(tr.text.strip().split('\n'))
    return table_full

