from bs4 import BeautifulSoup
import requests
from pprint import pprint

from getters.links import get_categories, get_species_links, get_links_recursive

category_links = get_categories()

relevant_links = []

for i in range(3,12):
    relevant_links.append(f'\n-{i}-\n')
    relevant_links.extend(get_links_recursive(category_links[i],[], len(relevant_links)))
    print()
    print()
    print(f'Current Count  =====================================>  {len(relevant_links)}')
    print(f'Finished working on  ===============================>  {category_links[i]}')
    print()
    print()

print()
print()
print(f'Final Count  ===============================>  {len(relevant_links)}')

with open('relevant_links.txt', 'w', encoding='utf8') as file:
    file.writelines(relevant_links)

