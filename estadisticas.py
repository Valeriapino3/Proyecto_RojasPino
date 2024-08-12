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

personajes_por_planeta()

def comparar_naves():
    # Cargar el archivo csv starships
    datos_naves = pd.read_csv("starwars (1)/csv/starships.csv")

    # Seleccionar las columnas de interés
    columnas_interes = ["name", "length", "cargo_capacity", "hyperdrive_rating", "MGLT"]
    datos_naves = datos_naves[columnas_interes]

    # Colocar index en el nombre de la nave
    datos_naves.set_index("name", inplace=True)

    # Crear un gráfico con 4 subplots, uno para cada característica de las naves
    plt.figure(figsize=(14, 8))
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
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

    plt.tight_layout()
    plt.show()


comparar_naves()