﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información en el catalogo")
    print("3- Encontrar puntos de interconexión aérea")
    print("4- Encontrar clusteres de tráfico aéreo")
    print("5- Encontrar la ruta mas corta entre ciudades")
    print("6- Utilizar las millas de viajero ")
    print("7- Cuantificar el eefecto de un aeropuerto cerrado")
    print("0- Salir")
    print("*******************************************")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")

    elif int(inputs[0]) == 2:
            print("cargando datos en el catalogo")

    elif int(inputs[0]) == 3:
            print("Req1")

    elif int(inputs[0]) == 4:
            print("Req2")

    elif int(inputs[0]) == 5:
            print("Req3")

    elif int(inputs[0]) == 6:
            print("Req4")

    elif int(inputs[0]) == 7:
            print("Req5")

    else:
            sys.exit(0)                                   
sys.exit(0)
