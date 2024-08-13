import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar datos del archivo CSV

datos_personajes = pd.read_csv("starwars (1)/csv/characters.csv")


def personajes_por_planeta():
    #  Generar un gráfico en el que se muestre la cantidad de personajes nacidos en cada planeta que aparece en la saga.
    #  Para ello, se debe contar la cantidad de personajes nacidos en cada planeta y mostrarlo en un gráfico de barras.

    # Contar la cantidad de personajes nacidos en cada planeta
    personajes_por_planeta = datos_personajes["homeworld"].value_counts()

    # Crear el gráfico
    plt.figure(figsize=(10, 6))
    # Separar las barras para que se vean mejor
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.3)
    personajes_por_planeta.plot(kind="bar", color="yellow")
    plt.title("Cantidad de personajes nacidos en cada planeta de Star Wars")
    plt.xlabel("Planeta")
    plt.ylabel("Cantidad de personajes")
    plt.xticks(rotation=90)
    plt.show()


def comparar_naves():
    # Cargar el archivo csv starships
    datos_naves = pd.read_csv("starwars (1)/csv/starships.csv")

    # Seleccionar las columnas de interés
    columnas_interes = ["name", "length", "cargo_capacity", "hyperdrive_rating", "MGLT"]
    datos_naves = datos_naves[columnas_interes]

    # Colocar index en el nombre de la nave
    datos_naves.set_index("name", inplace=True)

    # Crear un gráfico con 4 subplots, uno para cada característica de las naves
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.3)

    # Crear los subplots
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))
    datos_naves["length"].plot(kind="bar", ax=axes[0, 0], color="blue", title="Longitud")
    datos_naves["cargo_capacity"].plot(kind="bar", ax=axes[0, 1], color="green", title="Capacidad de carga")
    datos_naves["hyperdrive_rating"].plot(kind="bar", ax=axes[1, 0], color="red", title="Hiperimpulsor")
    datos_naves["MGLT"].plot(kind="bar", ax=axes[1, 1], color="purple", title="MGLT")

    # Colocar los nombres de las naves en el eje x y rotarlos para que se ve
    for ax in axes.flat:
        ax.set_xlabel("Naves")
        ax.set_ylabel("Valor")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90, fontsize=8)

    plt.tight_layout()
    plt.show()

def tabla_estadisticas_naves():
    #Para cargar los datos de las naves 
    datos_naves=pd.read_csv("starwars (1)/csv/starships.csv")
    
    #Agrupar los datos por clase de nave 
    grouped_naves=datos_naves.groupby("starship_class")
    
    #Calcular estadísticas 
    summary = grouped_naves.agg({
        'hyperdrive_rating': ['mean', 'max', 'min', lambda x: x.mode().iloc[0] if not x.mode().empty else None],
        'MGLT': ['mean', 'max', 'min', lambda x: x.mode().iloc[0] if not x.mode().empty else None],
        'max_atmosphering_speed': ['mean', 'max', 'min', lambda x: x.mode().iloc[0] if not x.mode().empty else None],
        'cost_in_credits': ['mean', 'max', 'min', lambda x: x.mode().iloc[0] if not x.mode().empty else None]
    })
    
    #Renombrar las columnas 
    summary.columns = ['_'.join(col).strip() for col in summary.columns.values]
    summary.rename(columns={
        'hyperdrive_rating_<lambda_0>': 'hyperdrive_rating_mode',
        'MGLT_<lambda_0>': 'MGLT_mode',
        'max_atmosphering_speed_<lambda_0>': 'max_atmosphering_speed_mode',
        'cost_in_credits_<lambda_0>': 'cost_in_credits_mode'
    }, inplace=True)
              
    # Mostrar la tabla resumen
    print(summary)


def menu_principal_estadisticas():
    while True:
        print("\n/// Compara el mundo de STAR WARS! ///")
        print("1. Mostrar cantidad de personajes por planeta")
        print("2. Comparar naves")
        print("3. Mostrar tabla de estadísticas de naves")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción que desea ejecutar: ")
        while opcion not in ["1", "2", "3", "4"]:
            print("Opción no válida. Intente de nuevo.")
            opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == "1":
            personajes_por_planeta()
        elif opcion == "2":
            comparar_naves()
        elif opcion == "3":
            tabla_estadisticas_naves()
        elif opcion == "4":
            break

