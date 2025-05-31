import requests, json

country = 'FR'
api_url = 'https://api.api-ninjas.com/v1/vat?country={}'.format(country)
response = requests.get(api_url, headers={'X-Api-Key': 'BV+aVla8SvDJx22cAlWr3w==l4k92B43b912ca50'})

class Kereses(object):
    def __init__(self, tipus):
        self.tipus = tipus
        print("létrehoztam a keresést")

    def keres_tipus(self):
        print("elindítottam a kerestipust")
        for elem in json.loads(response.text):
            if elem['type'] == self.tipus:
                print(elem)


Kereses('exempted').keres_tipus()