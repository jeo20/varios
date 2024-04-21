import random # importo la libreria random

def tirar_cubilete(): # funcion que tira 5 dados
    dados = [] # lista vacía
    for _ in range(5): # _ es un alias para un valor que no se usa, crea 5 valores
        dados.append(random.randint(1, 6)) # random.randint(1, 6) es un número aleatorio entre 1 y 6
    return dados # devuelve una lista con 5 números aleatorios entre 1 y 6

def cuantos_hay(elemento, lista): # funcion que cuenta la cantidad de elementos iguales  en una lista
    contador = 0 # inicializo en 0
    for item in lista: # recorro la lista
        if item == elemento: # si el item es igual al elemento
            contador += 1 # sumo 1 al contador
    return contador # devuelvo el contador 

def puntos_por_unos(lista_dados): # funcion que devuelve el puntaje obtenido por cantidad de unos
    unos = cuantos_hay(1, lista_dados) # uso la funcion cuantos_hay para saber cuantos 1 existen en la lista
    if unos >= 3: # si unos es mayor o igual a 3
        if unos == 3: # si unos es igual a 3
            return 1000 # devuelvo 1000
        elif unos == 4: # si unos es igual a 4
            return 1100 # devuelvo 1100
        else: # si no
            return 10000 # devuelvo 10000
    else: # si no
        return 100 * unos # devuelvo 100 * unos 

def puntos_por_cincos(lista_dados): # funcion que devuelve el puntaje obtenido por cantidad de cincos
    cincos = cuantos_hay(5, lista_dados) # cuantos_hay(5, lista_dados) es un número
    if cincos >= 3: # si cincos es mayor o igual a 3
        if cincos == 3: # si cincos es igual a 3
            return 500 # devuelvo 500
        elif cincos == 4: # si cincos es igual a 4
            return 550 # devuelvo 550
        else: # si no
            return 600 # devuelvo 600
    else: # si no
        return 50 * cincos # devuelvo 50 * cincos

def total_puntos(lista_dados): # funcion que devuelve el puntaje total obtenido de unos y cincos
    return puntos_por_unos(lista_dados) + puntos_por_cincos(lista_dados) # devuelvo la suma de los puntajes obtenidos por unos y cincos

def jugar_ronda(cant_jugadores): # funcion que devuelve los puntajes obtenidos en una ronda
    puntajes_ronda = [] # lista que contiene los puntajes obtenidos en una ronda 
    for _ in range(cant_jugadores): # simula la jugada para cada jugador
        puntajes_ronda.append(total_puntos(tirar_cubilete()))# agrego el puntaje obtenido en una ronda a la lista de puntajes_ronda
    return puntajes_ronda # devuelvo la lista de puntajes_ronda

def acumular_puntos(puntajes_acumulados, puntajes_ronda): # funcion que devuelve los puntajes acumulados
    puntajes_actualizados = [] # lista que contiene los puntajes acumulados
    for i in range(len(puntajes_acumulados)): # puntaje para cada jugador
        puntajes_actualizados.append(puntajes_acumulados[i] + puntajes_ronda[i]) # agrego el puntaje obtenido en una ronda a la lista de puntajes_actualizados
    return puntajes_actualizados # devuelvo la lista de puntajes_actualizados


def hay_10mil(puntajes_acumulados): # funcion que devuelve si hay un jugador con 10000 o mas puntos
    for puntaje in puntajes_acumulados: # recorre para cada puntaje de los acumulados
        if puntaje >= 10000 or puntaje == 10000: # si el puntaje es mayor o igual a 10000
            return True # devuelvo True
    return False # devuelvo False

# Simulacion de una partida completa
def partida_completa(cant_jugadores): # funcion que devuelve la cantidad de rondas necesarias para que haya un jugador con 10000 o mas puntos
    puntajes = [0] * cant_jugadores # lista que contiene los puntajes de los jugadores
    rondas = 0 # cantidad de rondas inicial en 0
    while not hay_10mil(puntajes): # mientras no haya un jugador con 10000 o mas puntos
        puntajes = acumular_puntos(puntajes, jugar_ronda(cant_jugadores)) # actualizo los puntajes
        rondas += 1 # sumo una ronda
    return rondas # devuelvo la cantidad de rondas

# Simulacion de varias partidas
def simular_partidas(cant_jugadores, n_rep): # funcion que devuelve la cantidad de rondas necesarias para que haya un jugador con 10000 o mas puntos
    cant_rondas = [] # lista que contiene la cantidad de rondas para cada partida
    for _ in range(n_rep): # para cada partida
        cant_rondas.append(partida_completa(cant_jugadores)) # agrego la cantidad de rondas necesarias para que haya un jugador con 10000 o mas puntos
    return cant_rondas # devuelvo la lista de cant_rondas

# Simulación con 10 jugadores y 10000 repeticiones

n_rep = 10000 # cantidad de repeticiones de la simulación igual a 10000
cant_jugadores = 10 # cantidad de jugadores igual a 10
cant_rondas = simular_partidas(cant_jugadores, n_rep) # simular partidas con 10 jugadores y 10000 repeticiones


# a) Promedio de rondas con 10 jugadores
suma_rondas = 0 # suma de las rondas
for rondas in cant_rondas: # para cada ronda
    suma_rondas += rondas # sumo la ronda
promedio_rondas = suma_rondas / n_rep # promedio de rondas
print(f"En promedio, con 10 jugadores se necesitan {promedio_rondas:.2f} rondas.") # imprimo el promedio de rondas

# b) Probabilidad de terminar en 18 rondas o menos con 10 jugadores
partidas_18_rondas = 0 # cantidad de partidas que terminan en 18 rondas o menos
for rondas in cant_rondas: # recorre todas las cantidades de rondas
    if rondas <= 18: # si la ronda es menor o igual a 18
        partidas_18_rondas += 1 # sumo una partida
prob_18_rondas = partidas_18_rondas / n_rep # probabilidad de terminar en 18 rondas o menos con 10 jugadores
print(f"La probabilidad de terminar en 18 rondas o menos con 10 jugadores es: {prob_18_rondas:.4f}") 
# imprimo la probabilidad de terminar en 18 rondas o menos con 10 jugadores

# c) Probabilidad de terminar en 18 rondas o menos con 20 jugadores
cant_jugadores = 20 # cantidad de jugadores igual a 20
cant_rondas_20 = simular_partidas(cant_jugadores, n_rep) # simular partidas con 20 jugadores y 10000 repeticiones
suma_rondas_20 = 0 # suma de las rondas
for rondas in cant_rondas_20: # recorre todas las cantidades de rondas
    suma_rondas_20 += rondas # sumo la ronda
promedio_rondas_20 = suma_rondas_20 / n_rep # promedio de rondas
print(f"En promedio, con 20 jugadores se necesitan {promedio_rondas_20:.2f} rondas.") # imprimo el promedio de rondas