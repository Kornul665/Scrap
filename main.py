import csv
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import random

# url = "https://health-diet.ru/table_calorie/"
#
headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    'Chrome/92.0.4515.159 Safari/537.36'

}
# req = requests.get(url, headers=headers)
# src = req.text
#
# with open('index.html', 'w', encoding='utf-8') as f:
#     f.write(src)
# # print(src)
# with open('index.html', encoding='utf-8') as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
# all_products_hrefs = soup.find_all(class_='mzr-tc-group-item-href')
#
# all_categories_dict = {}
# for item in all_products_hrefs:
#     item_text = item.text
#     item_href = 'https://health-diet.ru' + item.get('href')
#
#     all_categories_dict[item_text] = item_href
#
# with open('all_categories_dict.json', 'w') as file:
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

with open('all_categories_dict.json') as f:
    all_categories = json.load(f)

    
count = 0
for category_name, category_href in all_categories.items():
    rep = [",", ", ", "-", " ", "'"]
    for i in rep:
        if i in category_name:
            category_name = category_name.replace(i, '_')
    # print(category_name)

    req = requests.get(url=category_href, headers=headers)
    src = req.text

    with open(f'data/{count}_{category_name}.html', 'w', encoding='utf-8') as f:
        f.write(src)

    count += 1
