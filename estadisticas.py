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
