#!/home/gao/project/bingapi/venv/bin/python3
# coding=utf-8
import re
import os
import requests
import shutil
from bs4 import BeautifulSoup

response = requests.get('https://www.bing.com')
soup = BeautifulSoup(response.text)
pattern = re.compile('g_img={url:\'(.+?)\'')
url = 'https://www.bing.com'+ pattern.findall(soup.text)[0]
image_response = requests.get(url, stream=True)
path = os.path.split(os.path.realpath(__file__))[0] + '/bing_image/image.jpg'
print(path)
if image_response.status_code == 200:
    with open(path, 'w+b') as image:
        image_response.raw.decode_content = True
        shutil.copyfileobj(image_response.raw, image)
