import Ligas
import Partidos

def mostrar_menu_principal():
    print("Futbol DataBase")
    while True:
        opcion = input("1- Partidos   2-Top Grandes Ligas     3-Ligas     4-Programa Finalizado ")
        if opcion == "1":
            Partidos.todos_los_juegos()
        elif opcion == "2":
            Partidos.top3_juegos()
        elif opcion == "3":
            mostrar_menu_ligas()
        elif opcion == "4":
            print("Programa Finalizado")
            break
        else:
            print("Vuelve a intentar")

def mostrar_menu_ligas():
    print("Futbol DataBase")
    print("LIGAS")
    while True:
        liga = input("1- Premier    2- Española     3- Serie A      4- Bundesliga       5- Menu Anterior    6- Cerrar programa ")
        if liga == "1":
            mostrar_menu_liga(10)
        elif liga == "2":
            mostrar_menu_liga(1)
        elif liga == "3":
            mostrar_menu_liga(7)
        elif liga == "4":
            mostrar_menu_liga(8)
        elif liga == "5":
            break
        elif liga == "6":
            print("Programa Finalizado")
            exit()
        else:
            print("Vuelve a intentar")

def mostrar_menu_liga(id):
    while True:
        print("1- Jornada   2- Tabla de posiciones     3- Estadistica de jugadores   4- MENU anterior ")
        liga = input()
        if liga == "1":
            Ligas.partido_liga(id)
        elif liga == "2":
            Ligas.tabla(id)
        elif liga == "3":
            Ligas.estadisticas(id)
        elif liga == "4":
            break
        else:
            print("Vuelve a intentarlo")

mostrar_menu_principal()
