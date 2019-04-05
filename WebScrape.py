from urllib.request import urlopen as Req
from bs4 import BeautifulSoup as soup


f = open('data.csv', 'w')

url = 'https://www.dicksmith.co.nz/dn/shop/phones/iphone/?page=1'

Client = Req(url)
page_html = Client.read()
Client.close()

page_soup = soup(page_html, 'html.parser')

containers = page_soup.find_all('div', class_='_1umis')

f.write('Phone, Rating, Price \n')

for container in containers:
    Phone = container.find('a', itemprop='url').text
    if container.find('meta', itemprop='ratingValue') == None:
        Rating = 'no rating'
    else:
        Rating = container.find('meta', itemprop='ratingValue')['content']
    Price = container.find('span', itemprop='price')['content']
    f.write(Phone.replace(',',' |') + ', '+ Rating+', '+ Price + "\n")
    print(Phone.replace(',',' |') + ', '+ Rating+','+ Price.replace(',','') + "\n")

f.close()
