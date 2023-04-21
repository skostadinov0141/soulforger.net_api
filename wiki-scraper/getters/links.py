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


def get_links_recursive(link: str) -> list | False | str:
    if link.count('https://www.ulisses-ebooks.de') != 0:
        return False
    base_link = 'https://ulisses-regelwiki.de/'
    page = get(link)
    content = page.content

    soup = BeautifulSoup(content, 'html.parser')

    result = []

    a_tags_all : ResultSet = soup.find_all('a')
    a_links_relevant = []

    for i in a_tags_all:
        i : Tag = i
        href:str = i.attrs['href']
        if (href.count('.html') == 1) and (href.count('https://www.ulisses-ebooks.de') == 0):
            a_links_relevant.append(f'{base_link}{i.get("href")}')

    if len(a_links_relevant) == 0:
        return str
    else:
        for link in a_links_relevant:
            get_links_recursive(link)




    # if len(soup.find_all('a', {'class':'ulSubMenu'})) == 0 and len(soup.find_all('div', {'class':'body'})) == 0:
    # if link.count('https://') == 1 and len(soup.find_all('a', {'class':'ulSubMenu'})) == 0:
    #     for i in soup.find_all('div', {'class':'body'}):
    #         if(len(i.find_all('a')))
    #     print(f'Entry  --------->  {str(uuid4())}')
    #     return link

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