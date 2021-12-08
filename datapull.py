from time import sleep
import requests
import json
from datetime import datetime
from config import API_KEY

def championList():
    data = requests.get("https://ddragon.leagueoflegends.com/cdn/11.23.1/data/en_US/champion.json").json()["data"]
    champion_list = {}
    for champs in data:
        champion_list.update({data[champs]["key"]: champs})


def __init__():
    championList()

def player_ids(IGN):  # id | account id | puuid | name | summonerLevel
    jsondata = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + IGN + "?api_key=" + API_KEY).json()
    sleep(1.5)
    globals()[IGN] = [jsondata["id"], jsondata["accountId"], jsondata["puuid"], jsondata["name"], jsondata["summonerLevel"]]
    return jsondata["id"], jsondata["accountId"], jsondata["puuid"], jsondata["name"], jsondata["summonerLevel"]



