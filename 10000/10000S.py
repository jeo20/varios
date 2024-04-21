import random

dados_tirados = []

def tirar_cubilete():
    while len(dados_tirados) < 5:
        dados = random.randint (1,6)
        dados_tirados.append(dados)
    return dados_tirados

dados_tirados = tirar_cubilete()

def cuantos_hay(elemento, lista):
    cantidad = 0
    i = 0
    while (i < len(lista)):
        if (lista[i] == elemento):
            cantidad = cantidad + 1
        i = i + 1
    return cantidad

"""""
cantidad1 = cuantos_hay(1, dados_tirados)
cantidad5 = cuantos_hay(5, dados_tirados)
"""""

def puntos_por_unos (lista_dados):
    puntos1 = 0
    cantidad1 = cuantos_hay(1, dados_tirados)
    if cantidad1 == 1:
            puntos1 = puntos1 + 100
    elif cantidad1 == 2:
            puntos1 = puntos1 + 200
    elif cantidad1 == 3:
            puntos1 = puntos1 + 1300
    elif cantidad1 == 4:
            puntos1 = puntos1 + 1400
    elif cantidad1 == 5:
            puntos1 = puntos1 + 10500
    return puntos1    

def puntos_por_cincos (lista_dados):
    puntos5 = 0
    cantidad5 = cuantos_hay(5, dados_tirados)
    if cantidad5 == 1:
        puntos5 = puntos5 + 50
    elif cantidad5 == 2:
        puntos5 = puntos5 + 100
    elif cantidad5 == 3:
        puntos5 = puntos5 + 500
    elif cantidad5 == 4:
        puntos5 = puntos5 + 550
    elif cantidad5 == 5:
        puntos5 = puntos5 + 650
    return puntos5

def total_puntos (lista_dados):
    puntos_totales = puntos_por_unos(lista_dados) + puntos_por_cincos(lista_dados)
    return puntos_totales

def jugar_ronda (cant_jugadores):
    rondas = 0
    jugadores = cant_jugadores 
    while rondas < jugadores:
        dados = tirar_cubilete()
        puntaje = total_puntos(dados)
        rondas += 1
    return puntaje
"no la estaría entendiendo, preguntar:"
"me salen 10 jugadroes, pero con la misma jugada, como discrimino?"
