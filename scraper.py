from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://www.pararius.com/apartments/amsterdam?ac=1"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_="listing-search-item")

with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Location', 'Price', 'Area']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('h2', class_="listing-search-item__link--title").text.replace('\n', '')
        location = list.find('div', class_="mb-srp__card__ads--name").text.replace('\n', '')
        price = list.find('div', class_="mb-srp__card__price--amount").text.replace('\n', '')
        area = list.find('span', class_="illustrated-features__description").text.replace('\n', '')
        
        info = [title, location, price, area]
        thewriter.writerow(info)