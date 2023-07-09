from bs4 import BeautifulSoup
import requests

response = requests.get(url='https://news.ycombinator.com/')
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')

class_athing = soup.find_all(name='tr', class_='athing')
for single_class in class_athing:
    rank = single_class.find(name='span', class_='rank').getText()
    name = single_class.find(name='span', class_='titleline').getText()
    link = single_class.find(name='span', class_='titleline').a.get('href')
    print(f'{rank} {name}\n({link})\n')

