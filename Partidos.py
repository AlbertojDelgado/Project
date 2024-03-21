import requests
import json


API_KEY = "c6196c01e7c1d93932590f42beec9ef8"
API = f"https://apiclient.besoccerapps.com/scripts/api/api.php?key={API_KEY}&"


def load_api(formato_url):
    url = str(API + formato_url)
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    data_str = response.text

    # Cargar los datos como un diccionario JSON
    data = json.loads(data_str)
    return data

def todos_los_juegos():
    url_todos_los_juegos = "&format=json&req=matchsday"
    data = load_api(url_todos_los_juegos)

    for partido in data["matches"]:
        competicion = partido["competition_name"]
        ronda = partido["round"]
        equipos = f"{partido['local']} vs. {partido['visitor']}"
        hora = f"{partido['hour']}:{partido['minute']}"

        print(f"Competición: {competicion}")
        print(f"Ronda: {ronda}")
        print(f"Equipos: {equipos}")
        print(f"Hora: {hora}")
        print()

def top3_juegos():
    url_top3_juegos = "8&format=json&req=matchsday"
    data = load_api(url_top3_juegos)

    for partido in data["matches"]:
        competicion = partido["competition_name"]
        ronda = partido["round"]
        equipos = f"{partido['local']} vs. {partido['visitor']}"
        hora = f"{partido['hour']}:{partido['minute']}"

        if competicion == "Serie A":
                print(f"Competición: {competicion}")
                print(f"Ronda: {ronda}")
                print(f"Equipos: {equipos}")
                print(f"Hora: {hora}")
                print()
        if competicion == "Primera División":
                print(f"Competición: {competicion}")
                print(f"Ronda: {ronda}")
                print(f"Equipos: {equipos}")
                print(f"Hora: {hora}")
                print()
        if competicion == "Premier League":
                print(f"Competición: {competicion}")
                print(f"Ronda: {ronda}")
                print(f"Equipos: {equipos}")
                print(f"Hora: {hora}")
                print()
    if competicion != "Serie A" and competicion != "Premier League" and competicion != "Primera División":
        print("Hoy no hay partidos de esas competiciones")
               


if __name__ == "__main__":
    top3_juegos()
    todos_los_juegos()