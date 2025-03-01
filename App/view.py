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
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. p See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from os import name
import config as cf
import sys
import controller
from DISClib.ADT import map as mp
from DISClib.ADT import list as lt
from DISClib.DataStructures import heap as h
from DISClib.ADT import stack as sk
from DISClib.Algorithms.Graphs import prim as pr
from DISClib.Algorithms.Graphs import dfs as df
from DISClib.ADT.graph import gr
assert cf

Rutas = "routes-utf8-small.csv"
Aereopuertos = "airports-utf8-small.csv" 
Worldcities = "worldcities-utf8.csv"
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("----------------------------------------")
    print("Bienvenido")
    print("1- Iniciar y cargar información en el catálogo")
    print("2- Encontrar puntos de interconexión aérea ")
    print("3- Encontrar clústeres de tráfico aéreo ")
    print("4- Encontrar la ruta más corta entre ciudades")
    print("5- Utilizar las millas de viajero")
    print("6- Cuantificar el efecto de un aereopuerto cerrado")
    print("----------------------------------------")
def printfirstandlast(primero,ultimo):
    Iata1 = primero["IATA"]
    city1 = primero["City"]
    name1 = primero["Name"]
    country1 = primero["Country"]
    latitude1 = primero["Latitude"]
    longitude1 = primero["Longitude"]
    Iata2 = ultimo["IATA"]
    city2 = ultimo["City"]
    name2 = ultimo["Name"]
    country2 = ultimo["Country"]
    latitude2 = ultimo["Latitude"]
    longitude2 = ultimo["Longitude"]
    print("---------------------------")
    print("Iata: " + Iata1)
    print("Name: "+ name1)
    print("City: " +  city1)
    print("Country: " +  country1)
    print("Latitude: " + latitude1)
    print("Longitude: " + longitude1)
    print("----------------------------")
    print("Iata: " + Iata2)
    print("Name: " + name2)
    print("City: " +  city2)
    print("Country: " +  country2)
    print("Latitude: " + latitude2)
    print("Longitude: " + longitude2)
def printCities(primera,ultima):
    city1= primera["city"]
    country1= primera["country"]
    lat1 = primera["lat"]
    long1 = primera["lng"]
    population1 = primera["population"]
    city2= ultima["city"]
    country2= ultima["country"]
    lat2 = ultima["lat"]
    long2 = ultima["lng"]
    population2 = ultima["population"]
    print("----------------------------")
    print("City: " +  str(city1))
    print("Country: " + str(country1))
    print("Lat: " + lat1)
    print("Lng: " + long1)
    print("Population: " + population1)
    print("----------------------------")
    print("City: " +  str(city2))
    print("Country: " + str(country2))
    print("Lat: " + lat2)
    print("Lng: " + long2)
    print("Population: " + population2)



def PrintCarga(Catalogo,primeroyUlti):
    mapaIatas = Catalogo["AirportsByIATA"]
    elementosgraph = Catalogo["ElementosGraph"]
    mapaCity = Catalogo["Ciudades"]
    print("===Airports-Routes Digraph===")
    Digraph = Catalogo["VuelosDirec"]
    numedgesdI = controller.totalConnections(Catalogo,Digraph)
    numvertexdI = controller.totalfligths(Catalogo,Digraph)
    print("Nodes: " + str(numvertexdI) + " loaded airports")
    print("Edges: " + str(numedgesdI) + " loades routes")
    print("First and Last Airport loaded in the DiGraph.")
    primeroDi = primeroyUlti["Airports"][0]["IATA"]
    UltimoDi = primeroyUlti["Airports"][1]["IATA"]
    GetprimeroDi = mp.get(mapaIatas,primeroDi)['value']
    GetUltimoDi = mp.get(mapaIatas,UltimoDi)['value']
    printfirstandlast(GetprimeroDi,GetUltimoDi)
    #---------------------------------------------------
    print("===Airports-Routes Graph===")
    graph = Catalogo["VuelosInDirec"]
    numedges = controller.totalConnections(Catalogo,graph)
    numvertex = controller.totalfligths(Catalogo,graph)
    print("Nodes: " + str(numvertex) + " loaded airports")
    print("Edges: " + str(numedges) + " loades routes")
    print("First and Last Airport loaded in the Graph.")
    primero = lt.getElement(elementosgraph,1)["Departure"]
    ultimo = lt.getElement(elementosgraph,lt.size(elementosgraph))["Destination"]
    Getprimero = mp.get(mapaIatas,primero)['value']
    GetUltimo = mp.get(mapaIatas,ultimo)['value']
    printfirstandlast(Getprimero,GetUltimo)
    #---------------------------------------------------
    print("===City Network===")
    print("The number of cities are: " + str(mp.size(mapaCity)))
    PrimeraC = PrimerosyUlti["cities"][0]
    UltimaC = PrimerosyUlti["cities"][1]
    print("First and Last City loaded in the data structure")
    printCities(PrimeraC,UltimaC)
def printReq1(cola,Catalogo,conected):
    print("=== Req 1 ===")
    Digraph = Catalogo["VuelosDirec"]
    mapaIatas = Catalogo["AirportsByIATA"]
    numvertexdI = controller.totalfligths(Catalogo,Digraph)
    print("Number of airports in network: " +  str(numvertexdI))
    print("Conected airports insede network: " + str(conected))
    print("Top 5 most connected airports...")
    i = 1
    while i <= 5:
        airport = h.delMin(cola)
        vertice = airport["Vertice"]
        conections = airport["Conections"]
        inbound = airport["Indegree"]
        outbound = airport["Outdegree"]
        info = mp.get(mapaIatas,vertice)['value']
        name = info["Name"]
        ciudad = info["City"]
        country = info["Country"]
        print("-------------------------")
        print("Name: "+ name)
        print("City: " + ciudad)
        print("Country: "+ country)
        print("IATA: " + vertice)
        print("Conections: " + str(conections))
        print("Inbound: " + str(inbound))
        print("Outbound: " + str(outbound))
        i +=1
def PrintReq2(resultado,Ar1,Ar2,catalogo):
    mapaIatas = catalogo["AirportsByIATA"]
    info1 = mp.get(mapaIatas,Ar1)['value']
    name1 = info1["Name"]
    ciudad1 = info1["City"]
    country1 = info1["Country"]
    info2 = mp.get(mapaIatas,Ar2)['value']
    name2 = info2["Name"]
    ciudad2 = info2["City"]
    country2 = info2["Country"]
    print("--------------------------------")
    print("Airport - 1 IATA code: " + Ar1)
    print("--------------------------------")
    print("IATA: " + Ar1)
    print("Name: "+ name1)
    print("City: " + ciudad1)
    print("Country: "+ country1)
    print("--------------------------------")
    print("Airport - 2 IATA code: " + Ar2)
    print("--------------------------------")
    print("IATA: " + Ar2)
    print("Name: "+ name2)
    print("City: " + ciudad2)
    print("Country: "+ country2)
    print("--------------------------------")
    print("- Number of SCC in Airport-route network: " + str(resultado[1]))
    print("Does the " + name1 + " and " + name2 + " belong together?")
    print("Ans: " + str(resultado[0]))
def printSeleccionHomonimos(homonimos,ciudad1,ciudad2,catalogo):
    print("Ciudades homonimas de " + ciudad1)
    print("--------------------------------------")
    iterador1 = lt.iterator(homonimos[0])
    i = 1 
    while i <= lt.size(homonimos[0]):
        elemento = next(iterador1)
        print(str(i) + ")" + str(elemento["city"]) + " Country: " + str(elemento["country"]) + " Lat: " + str(elemento["lat"]) + " long: " + str(elemento["lng"]))
        i+=1
    Ciudadeleg1 = int(input("Selecciona una ciudad: "))
    print("--------------------------------------")
    CiudadOfi1 = lt.getElement(homonimos[0],Ciudadeleg1)
    print("Ciudades homonimas de " + ciudad2)
    print("--------------------------------------")
    iterador2 = lt.iterator(homonimos[1])
    j = 1 
    while j <= lt.size(homonimos[1]):
        elemento2 = next(iterador2)
        print(str(j) + ")" + str(elemento2["city"]) + " Country: " + str(elemento2["country"]) + " Lat: " + str(elemento2["lat"]) + " long: " + str(elemento2["lng"]))
        j+=1
    Ciudadeleg2 = int(input("Selecciona una ciudad: "))
    CiudadOfi2 = lt.getElement(homonimos[1],Ciudadeleg2)
    return CiudadOfi1, CiudadOfi2
def PrintResultAero(aereo1,aereo2,ciudad1,ciudad2):
    print("--- The deperture airport in " +  ciudad1 + " is: ")
    print("Iata: " + aereo1["IATA"] + " Name: " + aereo1["Name"] + " City: " + aereo1["City"] + " country: " + aereo1["Country"])
    print("--------------------------------------------------------")
    print("--- The arrival airport in " +  ciudad2 + " is: ")
    print("Iata: " + aereo2["IATA"] + " Name: " + aereo2["Name"] + " City: " + aereo2["City"] + " country: " + aereo2["Country"])
def PrintRe3(camino,catalogo):
    paradas = lt.newList(datastructure="ARRAY_LIST")
    mapaIatas = catalogo["AirportsByIATA"]
    mapaAirlines = catalogo["Airlines"]
    pesoTotal = 0
    print("--- Dijkstra´s trip details ---")
    print("- Trip path: ")
    for stak in lt.iterator(camino):
        elemento = sk.pop(camino)
        verticeA = elemento["vertexA"]
        verticeB = elemento["vertexB"]
        peso = float(elemento["weight"])
        pesoTotal += peso
        aereo1 = mp.get(mapaIatas,verticeA)["value"]
        lt.addLast(paradas,aereo1)
        aereo2 = mp.get(mapaIatas,verticeB)["value"]
        aereolinea= mp.get(mapaAirlines,verticeA)["value"]
        Aereolina = ""
        for vuelo in lt.iterator(aereolinea):
            destino = vuelo["destino"]
            if destino == verticeB:
                Aereolina = vuelo["Aereolinea"]
        print("---------------------------------------")
        print("Airline: " + Aereolina +  " Deperture: " + verticeA + " Destination: " + verticeB + " Distance_km: " + str(peso))
    print("------------------------------------------------")
    print("Total distance: " + str(pesoTotal) + " (km)")
    print("-----------------------------------------------")
    print("-Trip stops ")
    for parada in lt.iterator(paradas):
        print("Iata: " + parada["IATA"] + " Name: " + parada["Name"] + " City: " + parada["City"] + " Country: " + parada["Country"])
    print("Iata: " + aereo2["IATA"] + " Name: " + aereo2["Name"] + " City: " + aereo2["City"] + " country: " + aereo2["Country"])
def printAereo(aereo,catalogo):
    mapaIatas = catalogo["AirportsByIATA"]
    elemento = mp.get(mapaIatas,aereo)["value"]
    print("--- Deperture  Airport for IATA code: " + aereo + " ---")
    print("Iata : " + aereo + " Name: " + elemento["Name"] + " City: " + elemento["City"] + " Country: " + elemento["Country"])




def PrintReq4(milla,Begining,arco,cola,cont):
    mapaAirlines = cont["Airlines"]
    aveliablemiles = milla * 1.60
    mapaIndirect = cont["VuelosInDirec"]
    numAirports = controller.totalfligths(cont,mapaIndirect)
    print("- Numer of possible airports: " + str(numAirports))
    print("- Traveling distance sum between airports: " + str(round(arco,2)))
    print("- Passanger avaliable traveling miles: " + str(aveliablemiles))
    print("")
    print("--- Longest possible route with airport " + Begining + " ---")
    mayorcamino = h.delMin(cola)
    pesoTotal = 0
    print("- Longest possible path details: ")
    i = 1 
    while i < lt.size(mayorcamino["Camino"]):
        origen = lt.getElement(mayorcamino["Camino"],i)
        if i+1 <= lt.size(mayorcamino["Camino"]):
            destination = lt.getElement(mayorcamino["Camino"],i+1)
        aereo1 = mp.get(mapaAirlines,origen)["value"]
        marked = False
        for vuelo in lt.iterator(aereo1):
            destino = vuelo["destino"]
            if destino == destination and not marked:
                marked = True
                peso = vuelo["Distancia"]
                pesoTotal += peso
                aereolinea = vuelo["Aereolinea"]
                print("---------------------------------------")
                print("Airline: " + aereolinea +  " Deperture: " + origen + " Destination: " + destination + " Distance_km: " + str(peso))
        i+=1
    print("")
    print("- Longest possible path distance: " + str(round(pesoTotal,2)))
    if pesoTotal > aveliablemiles:
        MillasNecesarias = (pesoTotal - aveliablemiles) / 1.60
        print("--------------------------------------")
        print("The passanger needs " + str(round(MillasNecesarias,2)) + " miles to complete the trip")
    elif aveliablemiles > pesoTotal:
        print("--------------------------------------")
        MillasNecesarias = milla - ((aveliablemiles - pesoTotal) / 1.60)
        print("The passanger does not needs more miles. The passanger can efforts this trip and has an excedent of " + str(round(MillasNecesarias,2)))
def PrintRe5(resultados,cont,codigo):
    Graph = cont["VuelosInDirec"]
    Graphd = cont["VuelosDirec"]
    mapaIata = cont["AirportsByIATA"]
    print("Closing the airport with IATA code: " + codigo)
    print("")
    print("--- Airports-Routes DiGraph ---")
    OriginalNumVd = controller.totalConnections(cont,Graphd)
    OriginalNumEd = controller.totalfligths(cont,Graphd)
    print("Original number of airports: " + str(OriginalNumEd) + " and " + " Routes: " + str(OriginalNumVd))
    print("")
    print("--- Airports-Routes Graph ---")
    OriginalNumV = controller.totalConnections(cont,Graph)
    OriginalNumE = controller.totalfligths(cont,Graph)
    print("Original number of airports: " + str(OriginalNumE) + " and " + " Routes: " + str(OriginalNumV))
    print("")
    print("--- Removing Airport with IATA: " + codigo + " ---")
    removed = gr.removeVertex(Graphd,codigo)
    ReNumDV = controller.totalConnections(cont,removed)
    ReNumDE = controller.totalfligths(cont,removed)
    print("Resulting number of airports: " + str(ReNumDE) + " and " + " Routes: " + str(ReNumDV))
    print("")
    print("--- Airports-Routes Graph ---")
    Iremoved = gr.removeVertex(Graph,codigo)
    ReNumV = controller.totalConnections(cont,Iremoved)
    ReNumE = controller.totalfligths(cont,Iremoved)
    print("Resulting number of airports: " + str(ReNumE) + " and " + " Routes: " + str(ReNumV))
    print("")
    print("There are " + str(resultados[0]) + " Airports affected by the removal of " + codigo)
    print("The fisrts 5 airports affected are: ")
    i = 1
    iterador = lt.iterator(resultados[1])
    while i <=5:
        elemento = next(iterador)
        airport = mp.get(mapaIata,elemento)["value"]
        print("Iata: " + elemento + " Name: " + airport["Name"] + " City: " + airport["City"] + " Country: " + airport["Country"])

        i+=1


        





catalog = None
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("\nInicializando....")
        cont = controller.init()
        print("Cargando información de los archivos ....")
        PrimerosyUlti = controller.LoadInfo(cont,Rutas,Worldcities,Aereopuertos)
        PrintCarga(cont,PrimerosyUlti)

    elif int(inputs[0]) == 2:
        cola = controller.maxconections(cont["VuelosDirec"])
        printReq1(cola[0],cont,cola[1])
    elif int(inputs[0]) ==3:
        codigo1= input("Código IATA del aereopuerto 1: ")
        codigo2= input("Código IATA del aereopuerto 2: ")
        Resultado =controller.ComponentesConectados(cont["VuelosDirec"],codigo1,codigo2)
        PrintReq2(Resultado,codigo1,codigo2,cont)
    elif int(inputs[0]) == 4:
        ciudad1 = input("Ciudad de origen: ")
        ciudad2 = input (" Ciudad de destino: ")
        homonimos = controller.BuscarHomonimos(cont,ciudad1,ciudad2)
        CiudadesSeleccionadas = printSeleccionHomonimos(homonimos,ciudad1,ciudad2,cont)
        DistanciasAerepuertos = controller.AereopuertosCercanos(CiudadesSeleccionadas[0],CiudadesSeleccionadas[1],cont)
        PrintResultAero(DistanciasAerepuertos[0],DistanciasAerepuertos[1],ciudad1,ciudad2)
        camino = controller.DijkstraReqcorrido(cont["VuelosDirec"],DistanciasAerepuertos[0]["IATA"],DistanciasAerepuertos[1]["IATA"])
        PrintRe3(camino,cont)
    elif int(inputs[0]) == 5:
        milla = float(input("Millas disponibles: "))
        Begining = input("Aereopuerto de salida: ")
        printAereo(Begining,cont)
        resultados = controller.ArbolExpanciónMinima (cont, Begining)
        PrintReq4(milla,Begining,resultados[0],resultados[1],cont)
    elif int(inputs[0]) == 6:
        codigo = input("Codigo IATA del aereopuerto fuera de funcionamiento: ")
        resultados = controller.AfectedVertex(cont,codigo)
        PrintRe5(resultados,cont,codigo)

            
    else:
        sys.exit(0)
sys.exit(0)