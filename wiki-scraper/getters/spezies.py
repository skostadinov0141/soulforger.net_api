from bs4 import BeautifulSoup, ResultSet, Tag
from requests import get
from uuid import uuid4
import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
from pymongo import MongoClient
from pprint import pprint
import json
import re


load_dotenv('dsa_soulforger.env')

uri = "mongodb://%s:%s@%s/?authSource=%s" % (
    quote_plus(os.environ.get('DSA_SOULFORGER_DB_ACCOUNTMANAGER_UNAME')), 
    quote_plus(os.environ.get('DSA_SOULFORGER_DB_ACCOUNTMANAGER_PASS')), 
    f"{os.environ.get('DSA_SOULFORGER_DB_IP')}:{os.environ.get('DSA_SOULFORGER_DB_PORT')}",
    quote_plus(os.environ.get('DSA_SOULFORGER_DB_ACCOUNTMANAGER_SOURCE')),
)

mongo = MongoClient(uri, serverSelectionTimeoutMS=5)

database = mongo['dsa_soulforger_net']


def get_SF(url:str):
    page = get(url)
    content = page.content
    soup = BeautifulSoup(content, 'html.parser')

    result = {}

    target_div : Tag = soup.find('div', class_='ce_text block')
    target_div_children : ResultSet = soup.find_all('p')

    if target_div and target_div_children:
        for p in target_div_children:
            p : Tag = p
            if p.find_all('strong'):
                title = p.find('strong').extract().string
                result[title] = extract_text_recursive(p,'').replace(':','').strip()

    return result


def extract_text_recursive(div : Tag, text : str):

    # track
    result = ''

    # if div has children
    if div.children:
        # loop through children
        for child in div.children:
            # extract the child thereby removing it from tree
            extraction = child.extract()
            # if the child WAS a tag 
            if type(extraction) == Tag and extraction.children:
                text += extract_text_recursive(extraction,text)
                return text
            elif type(extraction) == str:
                return text
            elif type(extraction) == Tag:
                text += extract_text_recursive(extraction,text).string
                return text