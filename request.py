import requests
import pandas as pd
import json
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup


''' Get request + return games names and tags : 
names type is class 'bs4.element.NavigableString,
tags type is div TODO:check the type
'''
def scrap_names_and_tags():
    response = requests.get('https://store.steampowered.com/explore/new/')
    soup = BeautifulSoup(response.content, 'html.parser')
    names = soup.find_all('div',{'class':'tab_item_name'})
    games_details = soup.find_all('div',{'class':'tab_item_details'})
    return names , games_details