import pandas as pd
from Mision import Mision

# Read CSV files
planets_df = pd.read_csv('starwars (1)/csv/planets.csv')
starships_df = pd.read_csv('starwars (1)/csv/starships.csv')
characters_df = pd.read_csv('starwars (1)/csv/characters.csv')
weapons_df = pd.read_csv('starwars (1)/csv/weapons.csv')

# Global list to store missions
missions = []

# Function to display menu and create a mission
def create_mission():
    print("/// CREAR MISIÓN ///")

    # Select mission name
    mission_name = input("Ingrese el nombre de la misión: ")

    # Select planet
    print("\nSeleccione un planeta de destino:")
    for index, row in planets_df.iterrows():
        print(f"{index + 1}. {row['name']}")
    planet_index = int(input("Ingrese el número del planeta: ")) - 1
    planet_destino = planets_df.iloc[planet_index]['name']

    # Select starship
    print("\nSeleccione una nave:")
    for index, row in starships_df.iterrows():
        print(f"{index + 1}. {row['name']}")
    starship_index = int(input("Ingrese el número de la nave: ")) - 1
    nave = starships_df.iloc[starship_index]['name']

    # Create mission object
    mission = Mision(mission_name, planet_destino, nave)

    # Add weapons
    print("\nSeleccione armas (máximo 7):")
    for index, row in weapons_df.iterrows():
        print(f"{index + 1}. {row['name']}")
    while len(mission.armas) < 7:
        weapon_index = int(input("Ingrese el número del arma (0 para terminar): ")) - 1
        if weapon_index == -1:
            break
        weapon = weapons_df.iloc[weapon_index]['name']
        mission.agregar_arma(weapon)

    # Add characters
    print("\nSeleccione integrantes (máximo 7):")
    for index, row in characters_df.iterrows():
        print(f"{index + 1}. {row['name']}")
    while len(mission.integrantes) < 7:
        character_index = int(input("Ingrese el número del integrante (0 para terminar): ")) - 1
        if character_index == -1:
            break
        character = characters_df.iloc[character_index]['name']
        mission.agregar_integrante(character)

    # Add mission to global list
    missions.append(mission)

    # Display mission details
    print("\nMisión creada:")
    print(mission)

# Function to view missions
def view_missions():
    if not missions:
        print("No hay misiones creadas.")
        return

    print("\n/// MISIÓNES ///")
    for index, mission in enumerate(missions):
        print(f"{index + 1}. {mission.nombre}")

    mission_index = int(input("Ingrese el número de la misión para ver detalles: ")) - 1
    if 0 <= mission_index < len(missions):
        print(missions[mission_index])
    else:
        print("Número de misión no válido.")

# Main menu
def main_menu():
    while True:
        print("\n/// MENÚ PRINCIPAL ///")
        print("1. Crear misión")
        print("2. Ver misiones")
        print("3. Salir")
        choice = input("Seleccione una opción: ")
        if choice == '1':
            create_mission()
        elif choice == '2':
            view_missions()
        elif choice == '3':
            break
        else:
            print("Opción no válida. Intente de nuevo.")


main_menu()