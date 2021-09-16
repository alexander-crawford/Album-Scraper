import requests
from bs4 import BeautifulSoup
import json
import re
from collections import OrderedDict
import unicodedata


def get():
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
        'status_message' : 'success',
        'source' : 'billboard top album sales'
    }

    def fail(error):
        response['meta'] = {
        'status' : 500,
        'status_message' : error + ' error',
        'source' : 'billboard top album sales'
        }
        return response
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
            text = unicodedata.normalize("NFKD",position.get_text().strip())

            # allow between 1 and 3 single digit numbers only
            pattern = re.compile('^\d{1,3}$')

            if pattern.fullmatch(text)!=None:
                dict['position'] = text
            else:
                fail('position')

        # add artist
        for artist in li.find_all('div','chart-list-item__artist'):

            # get artist name and remove white space
            text = unicodedata.normalize("NFKD",artist.get_text().strip())

            # Allows one or more instance of a non white space character
            # followed by zero or one space character
            pattern = re.compile('^(\S+ {0,1})+$')

            if pattern.fullmatch(text) is not None:
                dict['artist'] = text
            else:
                fail('artist')

        # add album
        for album in li.find_all('span','chart-list-item__title-text'):

            # get album name and remove white space
            text = unicodedata.normalize("NFKD",album.get_text().strip())

            # Allows one or more instance of a non white space character
            # followed by zero or one space character
            pattern = re.compile('^(\S+ {0,1})+$')

            if pattern.fullmatch(text) is not None:
                dict['album'] = text
            else:
                fail('album')


        # add dictionary to list
        data.append(dict)

    # add data list to response dictionary
    response['data'] = data

    # return data
    return json.dumps(response)

if __name__ == '__main__':
    get()
