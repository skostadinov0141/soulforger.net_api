import os
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from pymongo import MongoClient
import requests
from pprint import pprint
import json
import re

from getters.links import get_categories, get_links_recursive
from getters.spezies import get_SF

category_links = get_categories()
category_names = [
    'Spezies',
    'Kulturen',
    'Professionen',
    'Sonderfertigkeiten',
    'Vor- und Nachteile',
    'Magie',
    'Götterwirken',
    'Rüstkammer',
    'Bestiarium',
    'Herbarium',
    'Gifte und Krankheiten',
]

count = 0

load_dotenv('dsa_soulforger.env')

uri = "mongodb://%s:%s@%s/?authSource=%s" % (
    quote_plus(os.environ.get('DSA_SOULFORGER_DB_ACCOUNTMANAGER_UNAME')), 
    quote_plus(os.environ.get('DSA_SOULFORGER_DB_ACCOUNTMANAGER_PASS')), 
    f"{os.environ.get('DSA_SOULFORGER_DB_IP')}:{os.environ.get('DSA_SOULFORGER_DB_PORT')}",
    quote_plus(os.environ.get('DSA_SOULFORGER_DB_ACCOUNTMANAGER_SOURCE')),
)

mongo = MongoClient(uri, serverSelectionTimeoutMS=5)

database = mongo['dsa_soulforger_net']

for i in range(1,12):
    result = get_links_recursive(category_links[i], category_names[i - 1])
    database['wiki'].insert_many(result)


