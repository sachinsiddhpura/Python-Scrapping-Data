import requests
from bs4 import BeautifulSoup

url='https://www.yelp.com/search?find_desc=Restaurants&find_loc=San+Francisco%2C+CA'

html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')


businesses = soup.findAll('div', {'class': 'biz-listing-large'})

for biz in businesses:
    #print(biz)
    title = biz.findAll('a', {'class': 'biz-name'})[0].text
    print(title)
    address = biz.findAll('address')[0] #.replace(' ', '')
    print(address)
    print('\n')
    phone = biz.findAll('span', {'class': 'biz-phone'})[0].text
    print(phone)
