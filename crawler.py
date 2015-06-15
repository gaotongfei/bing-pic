# coding=utf-8
import re
import requests
import shutil
from bs4 import BeautifulSoup

response = requests.get('https://www.bing.com')
soup = BeautifulSoup(response.text)
pattern = re.compile('g_img={url:\'(.+?)\'')
url = 'https://www.bing.com'+ pattern.findall(soup.text)[0]
image_response = requests.get(url, stream=True)
path = 'bing_image/image.jpg'
if image_response.status_code == 200:
    with open(path, 'w+b') as image:
        image_response.raw.decode_content = True
        shutil.copyfileobj(image_response.raw, image)
