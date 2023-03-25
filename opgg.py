import webbrowser
import requests
import time
import json

API_KEY = "YOUR-API-KEY-HERE"

def get_summoner_id(summoner_name):
    url = f"https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data["id"]

def get_current_game(summoner_id):
    url = f"https://na1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{summoner_id}?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def get_champion_id(game_data, summoner_id):
    for participant in game_data["participants"]:
        if participant["summonerId"] == summoner_id:
            return participant["championId"]

def get_champion_name_by_id(champion_id):
    url = f"https://ddragon.leagueoflegends.com/cdn/11.9.1/data/en_US/champion.json"
    response = requests.get(url)
    data = response.json()

    for champion_name, champion_info in data["data"].items():
        if int(champion_info["key"]) == champion_id:
            return champion_name
    return None

def main():
    summoner_name = "YOUR-SUMMONER-NAME-HERE"
    summoner_id = get_summoner_id(summoner_name)

    while True:
        game_data = get_current_game(summoner_id)
        if game_data:
            champion_id = get_champion_id(game_data, summoner_id)
            champion_name = get_champion_name_by_id(champion_id)
            if champion_name:
                url = f"https://www.op.gg/champions/{champion_name}/"
                webbrowser.open(url)
                break
        time.sleep(5)

if __name__ == "__main__":
    main()
