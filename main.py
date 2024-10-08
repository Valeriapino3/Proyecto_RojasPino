from Misiones import menu_principal_misiones
from estadisticas import menu_principal_estadisticas
from APIs import menu_principal_API

def menu_general():
    while True:
        print("\n/// En una galaxia muy lejana... ///")
        print("1. Misiones")
        print("2. Estadísticas")
        print("3. APIs")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción que desea ejecutar: ")
        while opcion not in ["1", "2", "3", "4"]:
            print("Opción no válida. Intente de nuevo.")
            opcion = input("Ingrese el número de la opción que desea ejecutar: ")

        if opcion == "1":
            menu_principal_misiones()
        elif opcion == "2":
            menu_principal_estadisticas()
        elif opcion == "3":
            menu_principal_API()
        elif opcion == "4":
            print("Que la fuerza te acompañe...")
            exit()


menu_general()