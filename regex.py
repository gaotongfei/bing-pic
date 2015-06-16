# coding=utf-8
import re
from bs4 import BeautifulSoup

response = requests.get('https://www.bing.com')
soup = BeautifulSoup(response.text)

text = "g_img={url:'/az/hprichbg/rb/AlgaeAerial_ZH-CN12058812432_1920x1080.jpg';"
pattern = re.compile('g_img={url:\'(.+?)\'')
url = 'https://www.bing.com'+ pattern.findall(text)[0]
print(url)
