import argparse
import requests
from secrets import EDAMAM_API_ID, EDAMAM_API_KEY


BASE_URL = 'https://api.edamam.com/'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ingredient')
    args = parser.parse_args()

    res = search_edamam(args.ingredient)
    print(res)


def search_edamam(ingredient):
    url = BASE_URL + 'search'
    params = {
        'q': ingredient,
        'app_id': EDAMAM_API_ID,
        'app_key': EDAMAM_API_KEY,
    }
    r = requests.get(url, params=params)
    print(r)
    return r.json()


if __name__ == '__main__':
    main()
