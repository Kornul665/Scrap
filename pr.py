import csv
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import random

url = "https://health-diet.ru/table_calorie/"

req = requests.get(url)
src = req.text
print(src)

with open('index.html', 'w', encoding='utf-8') as f:
	f.write(src)
