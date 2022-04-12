import json
import requests

heroes = ['Hulk', 'Captain America', 'Thanos']
token = '2619421814940190'
dict = {}

for hero in heroes:
    url = f'https://superheroapi.com/api/{token}/search/{hero}'

    response = requests.get(url)
    data = response.json()

    dict[hero] = 0
    for item in data['results']:
        dict[hero] = int(item['powerstats']['intelligence'])


max_intelligence = max(dict, key=dict.get)
print(f'Самый умный супергерой - {max_intelligence}')