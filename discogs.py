import requests
import keys
from ratelimit import limits

if __name__ == '__main__':
    getAlbumCover(seach_string)

# no more than 60 calls in a 1 minute period 
@limits(calls=60,period=60)
def getAlbumCover(seach_string):
    url = "https://api.discogs.com/database/search"

    querystring = {
        "key":keys.discogs_key,
        "secret":keys.discogs_secret,
        "q":seach_string
    }

    response = requests.request("GET", url, params=querystring)

    if response.json()['results'][0]['type']=='master' and response.status_code == 200:
        return response.json()['results'][0]['cover_image']
    else:
        return None
