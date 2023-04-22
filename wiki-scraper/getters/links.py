from bs4 import BeautifulSoup, ResultSet, Tag
from requests import get
from uuid import uuid4
from pprint import pprint


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


def get_links_recursive(link: str, category_path: str) -> list | dict:
    base_link = 'https://ulisses-regelwiki.de/'
    page = get(link)
    content = page.content

    soup = BeautifulSoup(content, 'html.parser')

    result = []

    divs_all : ResultSet = soup.find_all('div', attrs={
        'class': ['ulSubMenuRTable-cell', 'body', 'body_einzeln']
    })
    
    relevant_links = []

    for div in divs_all:
        div : Tag = div
        a : ResultSet = div.find_all('a', href=True, recursive=False)
        if a:
            for element in a:
                if element.get('href').count('https://') == 0:
                    relevant_links.append({
                        'link' : f'{base_link}{element.get("href")}',
                        'category' : element.string
                    })

    if len(relevant_links) == 0:
        category_path = category_path.replace('ﾃ､','ä').replace('Ă¤','ä').replace('ĂĽ','ü').replace('Ă¶','ö').replace('Ăź','ß').replace('Ă´','Ô').replace('Ă„','Ä').replace('ﾃｼ','ü').replace('ﾃ彙','Ü').replace('ÃĪ','ä').replace('Ãž','ü').replace('â€™','\'').replace('Ãķ','ö').replace('Ăś','Ü').replace('Ă–','Ö')
        print(category_path)
        return {
            'category_path':'|'.join(category_path.split('|')[:-1]),
            'title':category_path.split('|')[len(category_path.split('|')) - 1],
            'tags':category_path.split('|'),
            'link': link
        }

    for _link in relevant_links:
        response = get_links_recursive(_link['link'],f'{category_path}|{_link["category"]}')
        if(type(response) == dict):
            result.append(response)
        else:
            result.extend(response)

    return result

    