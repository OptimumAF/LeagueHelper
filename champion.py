from pprint import pprint
import requests
import json

champion_list = {}

data = requests.get("https://ddragon.leagueoflegends.com/cdn/11.23.1/data/en_US/champion.json").json()["data"]

if __name__ == '__main__':
    pprint(data)
    for champs in data:
        champion_list.update({data[champs]["key"]: champs})
    print(champion_list)
    with open('champions.txt', 'w') as convert_file:
        convert_file.write(json.dumps(champion_list))
    print("Done!")
