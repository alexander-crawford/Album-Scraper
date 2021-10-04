import requests
from bs4 import BeautifulSoup
import json
import re
from collections import OrderedDict
import unicodedata

def scrape(source_name,source_url,container_tag,container_class,artist_tag,artist_class,album_tag,album_class):

    # get the page
    page = requests.get(source_url)

    # get bs4 object
    soup = BeautifulSoup(page.text,'html.parser')

    # create dictionary to be returned
    response = {}

    # add status, assume success with code 200
    response['meta'] = {
        'status' : 200,
        'status_message' : 'success',
        'source' : source_name
    }

    def fail(error):
        response['meta'] = {
        'status' : 500,
        'status_message' : error + ' error',
        'source' : source_name
        }
        return response
        exit()

    # create data list
    data = []

    # iniitalise position counter
    position_counter = 0

    # iterate over soup object
    for li in soup.find_all(container_tag,container_class):

        # create dictionary
        dict = {}

        # add artist
        for artist in li.find_all(artist_tag,artist_class):

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
        for album in li.find_all(album_tag,album_class):

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
    scrape()
