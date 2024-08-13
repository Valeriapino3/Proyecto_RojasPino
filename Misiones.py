import pandas as pd
from Mision import Mision

# Leer archivos CSV
planetas = pd.read_csv('starwars (1)/csv/planets.csv')
naves = pd.read_csv('starwars (1)/csv/starships.csv')
personajes = pd.read_csv('starwars (1)/csv/characters.csv')
armas = pd.read_csv('starwars (1)/csv/weapons.csv')

# Lista global para almacenar misiones
misiones = []

# Función para guardar misiones en un archivo de texto
def guardar_misiones():
    with open('misiones.txt', 'w') as file:
        for mision in misiones:
            file.write(f"{mision.nombre}|{mision.planeta_destino}|{mision.nave}|{','.join(mision.armas)}|{','.join(mision.integrantes)}\n")
    print("Misiones guardadas en misiones.txt")

# Función para cargar misiones desde un archivo de texto
def cargar_misiones():
    try:
        with open('misiones.txt', 'r') as file:
            for line in file:
                nombre, planeta_destino, nave, armas, integrantes = line.strip().split('|')
                mision = Mision(nombre, planeta_destino, nave)
                mision.armas = armas.split(',') if armas else []
                mision.integrantes = integrantes.split(',') if integrantes else []
                misiones.append(mision)
        print("Misiones cargadas desde misiones.txt")
    except FileNotFoundError:
        print("No se encontró el archivo misiones.txt")

# Función para mostrar el menú y crear una misión
def crear_mision():
    print("/// CREAR MISIÓN ///")

    # Seleccionar nombre de la misión
    nombre_mision = input("Ingrese el nombre de la misión: ")

    # Seleccionar planeta
    print("\nSeleccione un planeta de destino:")
    for indice, fila in planetas.iterrows():
        print(f"{indice + 1}. {fila['name']}")
    indice_planeta = int(input("Ingrese el número del planeta: ")) - 1
    planeta_destino = planetas.iloc[indice_planeta]['name']

    # Seleccionar nave
    print("\nSeleccione una nave:")
    for indice, fila in naves.iterrows():
        print(f"{indice + 1}. {fila['name']}")
    indice_nave = int(input("Ingrese el número de la nave: ")) - 1
    nave = naves.iloc[indice_nave]['name']

    # Crear objeto misión
    mision = Mision(nombre_mision, planeta_destino, nave)

    # Agregar armas
    print("\nSeleccione armas (máximo 7):")
    for indice, fila in armas.iterrows():
        print(f"{indice + 1}. {fila['name']}")
    while len(mision.armas) < 7:
        indice_arma = int(input("Ingrese el número del arma (0 para terminar): ")) - 1
        if indice_arma == -1:
            break
        arma = armas.iloc[indice_arma]['name']
        mision.agregar_arma(arma)

    # Agregar personajes
    print("\nSeleccione integrantes (máximo 7):")
    for indice, fila in personajes.iterrows():
        print(f"{indice + 1}. {fila['name']}")
    while len(mision.integrantes) < 7:
        indice_personaje = int(input("Ingrese el número del integrante (0 para terminar): ")) - 1
        if indice_personaje == -1:
            break
        personaje = personajes.iloc[indice_personaje]['name']
        mision.agregar_integrante(personaje)

    # Agregar misión a la lista global
    misiones.append(mision)

    # Mostrar detalles de la misión
    print("\nMisión creada:")
    print(mision)

# Función para ver misiones
def ver_misiones():
    if not misiones:
        print("No hay misiones creadas.")
        return

    print("\n/// MISIONES ///")
    for indice, mision in enumerate(misiones):
        print(f"{indice + 1}. {mision.nombre}")

    indice_mision = int(input("Ingrese el número de la misión para ver detalles: ")) - 1
    if 0 <= indice_mision < len(misiones):
        print(misiones[indice_mision])
    else:
        print("Número de misión no válido.")

# Función para modificar una misión
def modificar_mision():
    if not misiones:
        print("No hay misiones creadas.")
        return

    print("\n/// MODIFICAR MISIÓN ///")
    for indice, mision in enumerate(misiones):
        print(f"{indice + 1}. {mision.nombre}")

    indice_mision = int(input("Ingrese el número de la misión para modificar: ")) - 1
    if 0 <= indice_mision < len(misiones):
        mision = misiones[indice_mision]

        # Modificar armas
        print("\n/// MODIFICAR ARMAS ///")
        print("1. Agregar arma")
        print("2. Eliminar arma")
        opcion_arma = input("Seleccione una opción: ")
        if opcion_arma == '1':
            print("\nSeleccione armas para agregar (máximo 7):")
            for indice, fila in armas.iterrows():
                print(f"{indice + 1}. {fila['name']}")
            while len(mision.armas) < 7:
                indice_arma = int(input("Ingrese el número del arma (0 para terminar): ")) - 1
                if indice_arma == -1:
                    break
                arma = armas.iloc[indice_arma]['name']
                mision.agregar_arma(arma)
        elif opcion_arma == '2':
            print("\nSeleccione armas para eliminar:")
            for indice, arma in enumerate(mision.armas):
                print(f"{indice + 1}. {arma}")
            while mision.armas:
                indice_arma = int(input("Ingrese el número del arma (0 para terminar): ")) - 1
                if indice_arma == -1:
                    break
                mision.armas.pop(indice_arma)

        # Modificar integrantes
        print("\n/// MODIFICAR INTEGRANTES ///")
        print("1. Agregar integrante")
        print("2. Eliminar integrante")
        opcion_integrante = input("Seleccione una opción: ")
        if opcion_integrante == '1':
            print("\nSeleccione integrantes para agregar (máximo 7):")
            for indice, fila in personajes.iterrows():
                print(f"{indice + 1}. {fila['name']}")
            while len(mision.integrantes) < 7:
                indice_personaje = int(input("Ingrese el número del integrante (0 para terminar): ")) - 1
                if indice_personaje == -1:
                    break
                personaje = personajes.iloc[indice_personaje]['name']
                mision.agregar_integrante(personaje)
        elif opcion_integrante == '2':
            print("\nSeleccione integrantes para eliminar:")
            for indice, integrante in enumerate(mision.integrantes):
                print(f"{indice + 1}. {integrante}")
            while mision.integrantes:
                indice_integrante = int(input("Ingrese el número del integrante (0 para terminar): ")) - 1
                if indice_integrante == -1:
                    break
                mision.integrantes.pop(indice_integrante)

        # Actualizar misión en la lista global
        misiones[indice_mision] = mision

        # Mostrar detalles de la misión modificada
        print("\nMisión modificada:")
        print(mision)
    else:
        print("Número de misión no válido.")

# Menú principal
def menu_principal():
    while True:
        print("\n/// MENÚ PRINCIPAL ///")
        print("1. Crear misión")
        print("2. Ver misiones")
        print("3. Modificar misión")
        print("4. Guardar misiones")
        print("5. Cargar misiones")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            crear_mision()
        elif opcion == '2':
            ver_misiones()
        elif opcion == '3':
            modificar_mision()
        elif opcion == '4':
            guardar_misiones()
        elif opcion == '5':
            cargar_misiones()
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu_principal()