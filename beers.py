import sys

import requests

if __name__ == '__main__':

    greater_than = sys.argv[1]
    first_url = 'https://api.punkapi.com/v2/beersa'
    second_url = 'https://s3-eu-west-1.amazonaws.com/kg-it/devopsTest/api-punkapi-com-v2-beers.json'
    response = requests.get(first_url)
    if response.status_code != 200:
        response = requests.get(second_url)
    beers = response.json()
    beers_output = []
    for beer in beers:
        beer_output = {}
        if int(greater_than) < beer['abv']:
            beer_output.update({'name': beer['name']})
            beer_output.update({'abv': beer['abv']})
            beers_output.append(beer_output)

    ordered_beers_ouptut = sorted(beers_output, key=lambda k: k['name'])
    for ordered_beer_output in ordered_beers_ouptut:
        print(ordered_beer_output['name'] + ',' + str(ordered_beer_output['abv']))