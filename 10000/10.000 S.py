import random 

dados_tirados = [] 
"lista vacía"

def tirar_cubilete(): 
    "tirada de dados"
    while len(dados_tirados) < 5: 
        "se tiran dados hasta que la longitud de la lista (dados_tirados) sea 5"
        dados_tirados.append(random.randint (1,6)) 
        "se añade a la lista un número aleatorio entre a y b"
    return dados_tirados
    "nos devuelve dados_tirados"

dados_tirados = tirar_cubilete()

def cuantos_hay(elemento, lista):
    cantidad = 0 #contador de cantidad de los elementos que buscamos
    i = 0 #contador de elementos distintos a los que buscamos
    while (i < len(lista)): #mientras i sea menor a la lista dados_tirados
        if (lista[i] == elemento):
            cantidad = cantidad + 1
        i = i + 1
        "si es un elemento que buscamos se suma a cantidad y a i, sino simplemente a i"
    return cantidad

"""""
cantidad1 = cuantos_hay(1, dados_tirados)
cantidad5 = cuantos_hay(5, dados_tirados)
"""""

def puntos_por_unos (lista_dados):
    "función para buscar y encontrar los elementos que valgan 1"
    puntos1 = 0 #depenidendo la cantidad de unos en una tirada
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
    "puntos por cantidad de uno, incluido <combos>"
    return puntos1    
    "nos devuelven los puntos en uno"
    
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
    "lo mismo que en la anterior función pero con el número 5"

def total_puntos (lista_dados):
    puntos_totales = puntos_por_unos(lista_dados) + puntos_por_cincos(lista_dados)
    return puntos_totales
    "sumatoria de puntos por uno y puntos por cinco"

def jugar_ronda (cant_jugadores):
    puntajes_ronda = [] 
    for _ in range (cant_jugadores): #puntaje para cada jugador
        puntajes_ronda.append(total_puntos(tirar_cubilete)) #añado el puntaje de una ronda a la lista
    return puntajes_ronda #regresa la lista los puntajes_ronda

"me da todas las jugadas el mismo valor en lacada elemento de la lista"

def acumular_puntos (puntajes_acumulados, puntajes_ronda):
    puntajes_actualizados = []
    for i in range (len(puntajes_acumulados)):#puntos para C/jugador; recorre la lista
        puntajes_actualizados.append(puntajes_acumulados + puntajes_ronda)
    return puntajes_actualizados

def hay_10mil(puntajes_acumulados):
    for puntaje in puntajes_acumulados: #recorre y ve puntajes de puntajes_acumulados
        if puntaje > 10000:
            return True
        return False

    
def partida_completa(cant_jugadores):
    puntajes = [0]*cant_jugadores
    num_rondas = 0
    while not hay_10mil(puntajes):
        puntajes = acumular_puntos(puntajes, jugar_ronda(cant_jugadores))
        num_rondasrondas = num_rondas + 1
    return num_rondasrondas

def partidas (nrep , cant_jugadores):
    cant_rondas = []
    for _ in range(nrep): # 
        cant_rondas.append(partida_completa(cant_jugadores)) # agrego la cantidad de rondas necesarias para que haya un jugador con 10000 o mas puntos
    return cant_rondas 


#1000 repeticiones, 10 jugadores
nrep = 1000
cant_jugadores = 10
cant_rondas = partidas(nrep , cant_jugadores)        


"10)a_ promedio con 10 jugadores"
sumatoria_rondas = 0
for rondas in cant_rondas: # para cada ronda
    sumatoria_rondas += rondas # sumo la ronda
promedio_rondas = sumatoria_rondas / nrep # promedio de rondas
print ("promedio de {prob_18_rondas:.4f}")
        
        
        