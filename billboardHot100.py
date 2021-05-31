import requests
from bs4 import BeautifulSoup
import json

# set url
url = "https://www.billboard.com/charts/top-album-sales"

# get the page
data = requests.get(url)

# get bs4 object
soup = BeautifulSoup(data.text,'html.parser')

# create list to be returned
data = []

# iterate over soup object
for li in soup.find_all('div','chart-list-item'):

    # create dictionary
    dict = {}

    # add position
    for position in li.find_all('div','chart-list-item__rank'):
        dict['position'] = position.get_text().replace('\n','')

    # add artist
    for artist in li.find_all('div','chart-list-item__artist'):
        dict['artist'] = artist.get_text().replace('\n','')

    # add album
    for album in li.find_all('span','chart-list-item__title-text'):
        dict['album'] = album.get_text().replace('\n','')

    # add dictionary to list
    data.append(dict)

# print output as json
print(json.dumps(data,sort_keys=True, indent=4))

# TODO: https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
