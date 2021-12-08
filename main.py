from time import sleep
import requests
import json
from datetime import datetime

API_KEY = "RGAPI-2c834bb8-c933-4040-822f-93e0dc403f38"

with open('champions.txt', 'r') as grab_file:
    champions = json.load(grab_file)


def player_ids(IGN):  # id | account id | puuid | name | summonerLevel
    jsondata = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + IGN + "?api_key=" + API_KEY).json()
    sleep(1.5)
    return jsondata["id"], jsondata["accountId"], jsondata["puuid"], jsondata["name"], jsondata["summonerLevel"]
    print(jsondata)

def champion_masteries(id):
    json = requests.get("https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + id + "?api_key=" + API_KEY).json()
    sleep(1.5)
    for x in range(10):
        print(champions[str(json[x]["championId"])] + " | Champion Level: " + str(json[x]["championLevel"]) + " | Last Played: " + str(datetime.fromtimestamp(json[x]["lastPlayTime"] // 1000)))
    return json

def player_stats(id):
    json = requests.get("https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + id + "?api_key=" + API_KEY).json()[0]
    sleep(1.5)
    print(json["summonerName"] + " is " + json["tier"] + " " + json["rank"] + " with a " + str(round(json["wins"]/(json["losses"]+ json["wins"])*100, 1)) + "% winrate")
    return json

def matches(puuid):
    champions_played = {}
    list_of_matches = []
    match_data = requests.get("https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid + "/ids?type=ranked&start=0&count=10&api_key=" + API_KEY).json()
    sleep(1.5)
    for games in match_data:
        game = requests.get("https://americas.api.riotgames.com/lol/match/v5/matches/" + games + "?api_key=" + API_KEY).json()["info"]["participants"]
        sleep(1.5)
        for players in game:
            if players["puuid"] == puuid:
                game = players
        if game["win"]:
            print("======== WIN ========")
        else:
            print("======== LOSS ========")
        if game["teamPosition"] == "UTILITY":
            game["teamPosition"] = "SUPPORT"
        print(game["championName"] + " | " + game["teamPosition"] + " | " + str(game["kills"]) + "/" + str(game["deaths"]) + "/" + str(game["assists"]))
        if champions_played.get(game["championName"]) == None:
            champions_played[game["championName"]] = {}
            champions_played[game["championName"]]["kills"] = game["kills"]
            champions_played[game["championName"]]["deaths"] = game["deaths"]
            champions_played[game["championName"]]["assists"] = game["assists"]
        else:
            champions_played[game["championName"]]["kills"] += game["kills"]
            champions_played[game["championName"]]["deaths"] += game["deaths"]
            champions_played[game["championName"]]["assists"] += game["assists"]
        print(game)
    print(match_data)
    return champions_played, list_of_matches

if __name__ == '__main__':
    # player_ids("OptimumAF")[2]
    player = player_ids("OptimumAF")
    # print(champions["266"])
    champion_masteries(player[0])
    player_stats(player[0])
    output = matches(player[2])
    print(output[0], output[1])



