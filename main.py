import csv
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import random

# url = "https://health-diet.ru/table_calorie/"

# headers = {
#     'Accept': '*/*',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
#     'Chrome/92.0.4515.159 Safari/537.36'

# }
# req = requests.get(url, headers=headers)
# src = req.text
# # print(src)

# with open('index.html', 'w', encoding='utf-8') as f:
#     f.write(src)
