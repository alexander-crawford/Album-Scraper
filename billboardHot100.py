import requests
from bs4 import BeautifulSoup
import json
import re
from collections import OrderedDict

def billboard():
    # set url
    url = "https://www.billboard.com/charts/top-album-sales"

    # get the page
    page = requests.get(url)

    # get bs4 object
    soup = BeautifulSoup(page.text,'html.parser')

    # create dictionary to be returned
    response = OrderedDict()

    # add status, assume success with code 200
    response['meta'] = {
        'status' : 200,
        'status_message' : 'success'
    }

    # create data list
    data = []

    # iterate over soup object
    for li in soup.find_all('div','chart-list-item'):

        # create dictionary
        dict = {}

        # add position
        for position in li.find_all('div','chart-list-item__rank'):
            dict['position'] = re.sub('[^0-9]','',position.get_text())

        # add artist
        for artist in li.find_all('div','chart-list-item__artist'):
            dict['artist'] = re.sub('[^a-zA-Z]','',artist.get_text())

        # add album
        for album in li.find_all('span','chart-list-item__title-text'):
            dict['album'] = album.get_text().replace('\n','')

        # add dictionary to list
        data.append(dict)

    # add data list to response dictionary
    response['data'] = data

    # print output as json
    print(json.dumps(response,indent=4))

    # return data
    return response

billboard()
