from bs4 import BeautifulSoup
import requests
from pprint import pprint

from getters.links import get_categories, get_species_links, get_links_recursive

category_links = get_categories()

count = 0

for i in range(1,12):
    relevant_links = []
    relevant_links.append(f'\n-{i}-\n')
    relevant_links.extend(get_links_recursive(category_links[i],[], len(relevant_links)))
    with open('relevant_links.txt', 'w', encoding='utf8') as file:
        file.writelines(relevant_links)
        file.close()
    count += len(relevant_links) - 1
    print()
    print()
    print(f'Entries Found  =====================================>  {len(relevant_links) - 1}')
    print(f'Total Entries Found  ===============================>  {count}')
    print(f'Finished working on  ===============================>  {category_links[i]}')
    print()
    print()


