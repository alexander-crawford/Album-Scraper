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
    response = {}

    # add status, assume success with code 200
    response['meta'] = {
        'status' : 200,
        'status_message' : 'success'
    }

    def fail(error):
        response['meta'] = {
        'status' : 500,
        'status_message' : error + ' error'
        }
        print(response)
        exit()

    # create data list
    data = []

    # iterate over soup object
    for li in soup.find_all('div','chart-list-item'):

        # create dictionary
        dict = {}

        # add position
        for position in li.find_all('div','chart-list-item__rank'):

            # get album position and remove white space
            text = position.get_text().strip()

            # allow between 1 and 3 single digit numbers only
            pattern = re.compile('^\d{1,3}$')

            if pattern.fullmatch(text)!=None:
                dict['position'] = text
            else:
                fail('position')

        # add artist
        for artist in li.find_all('div','chart-list-item__artist'):

            # get artist name and remove white space
            text = artist.get_text().strip()

            # Allows two or more non-whitespace characters
            # or whitespaces
            pattern = re.compile('[\S ]{2,}')

            if pattern.fullmatch(text) is not None:
                dict['artist'] = text
            else:
                fail('artist')

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
