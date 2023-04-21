from bs4 import BeautifulSoup, ResultSet, Tag
from requests import get
from uuid import uuid4


def get_categories():
    base_link = 'https://ulisses-regelwiki.de/'
    start_link = 'https://ulisses-regelwiki.de/start.html'
    page = get(start_link)
    content = page.content

    soup = BeautifulSoup(content, 'html.parser')

    global_uls : ResultSet = soup.find_all(
        'ul'
    )

    category_ul : Tag = None

    for i in global_uls:
        tag: Tag = i
        for k,v in tag.attrs.items():
            if k == 'class' and v == ['sf-menu', 'level_1']:
                category_ul = tag
    
    links_a: ResultSet = category_ul.find_all('a')
    links_content: list = []
    
    for i in links_a:
        i : Tag = i
        links_content.append(f'{base_link}{i.get("href")}')

    return links_content


def get_species_links(link : str):
    base_link = 'https://ulisses-regelwiki.de/'
    page = get(link)
    content = page.content

    soup = BeautifulSoup(content, 'html.parser')

    links : list = []

    for i in soup.find_all('a', {'class':'ulSubMenu'}):
        links.append(f'{base_link}{i.get("href")}')
    
    return links


def get_links_recursive(link: str, result: list, count: int = 0) -> list:
    base_link = 'https://ulisses-regelwiki.de/'
    page = get(link)
    content = page.content

    soup = BeautifulSoup(content, 'html.parser')

    if len(soup.find_all('a', {'class':'ulSubMenu'})) == 0 and soup.find('div', {'class':'body'}) == None:
        print(find_all(link, 'https://'))
        result.append('\n' + link)
        count += 1
        print(f'{count}  --------->  {str(uuid4())}')

    for i in soup.find_all('a', {'class':'ulSubMenu'}):
        get_links_recursive(f'\n{base_link}{i.get("href")}', result, count)
    
    if soup.find_all('div', {'class':'body'}) != None:
        for i in soup.find_all('div', {'class':'body'}):
            for j in i.find_all('a'):
                get_links_recursive(f'{base_link}{j.get("href")}', result, count)
    
    return result


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: break
        start += len(sub)
    return start