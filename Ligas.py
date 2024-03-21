import requests
import json
from prettytable import PrettyTable

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

def partido_liga(id):
    url_partido_liga = f"format=json&req=matchs&league={id}"
    data = load_api(url_partido_liga)
    

    for partido in data["match"]:
        competicion = partido["competition_name"]
        ronda = partido["round"]
        equipos = f"{partido['local']} {partido['local_goals']} - {partido['visitor_goals']} {partido['visitor']}"
        fecha = partido["date"]
        hora = f"{partido['hour']}:{partido['minute']}"

        print(f"Competición: {competicion}")
        print(f"Ronda: {ronda}")
        print(f"Equipos y Marcador: {equipos}")
        print(f"Fecha: {fecha}")
        print(f"Hora: {hora}")
        print()

def print_pretty_table(equipos):
    # Crear una instancia de PrettyTable
    tabla = PrettyTable()

    # Definir los nombres de las columnas
    tabla.field_names = ["Pos", "Equipo", "Puntos", "PG", "PE", "PP", "Avg"]

    # Agregar filas a la tabla
    for equipo in equipos:
        tabla.add_row([equipo['pos'], equipo['team'], equipo['points'], equipo['wins'], equipo['draws'], equipo['losses'], equipo['avg']])

    # Imprimir la tabla
    print(tabla)

def tabla(id):
    url_tabla = f"&format=json&req=tables&league={id}"
    
    return print_pretty_table(load_api(url_tabla)['table'])

def estadisticas(id):
    url_estadisticas = f"&tz=Europe/Madrid&format=json&req=league_stats&league={id}"
   
    data = load_api(url_estadisticas)
    goles = data["stats"]["goals"]
    asistencias = data["stats"]["asists"]
    
    tabla_goles = PrettyTable()
    tabla_goles.field_names = ["Nombre", "Equipo", "Goles"]
    for jugador in goles:
        nombre = jugador["nick"]
        valor = jugador["total"]
        equipo = jugador["team_name"]

        tabla_goles.add_row([nombre, equipo, valor])
    tabla_asistencia = PrettyTable()
    tabla_asistencia.field_names = ["Nombre", "Equipo", "Asistencia"]
    for jugado in asistencias:
        nombre = jugado["nick"]
        valor = jugado["total"]
        equipo = jugado["team_name"]

        tabla_asistencia.add_row([nombre, equipo, valor])

    print(tabla_goles)
    print("*" * 50)
    print(tabla_asistencia)

def tabla_estadistica(estadistica):
    
    tabla_de_estadistica = PrettyTable()
    tabla_de_estadistica.field_names = ["Nombre", "Equipo", "Goles"]
    for jugador in estadistica:
        nombre = jugador["nick"]
        valor = jugador["total"]
        equipo = jugador["team_name"]

        tabla_de_estadistica.add_row([nombre, equipo, valor])
    return tabla_de_estadistica

if __name__ == "__main__":
    estadisticas(1)
    tabla(1)
    partido_liga(1)


