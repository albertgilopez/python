print("***************************")
print("JUEGO PIEDRA, PAPEL, TIJERA")
print("***************************")

import random

# Antes de cualquier desarrollo, diseña mediante una estructura que quieres conseguir. En este caso:

# 1. Preguntar el nombre al jugador
# 2. Explicar las reglas del juego
# 3. Preguntar al jugador qué quiere sacar
# 4. Hacer una tirada aleatoria por el ordenador
# 5. Resolver quien ha ganado y sumarle el punto
# 6. Repetir del 3 al 5 diez veces
# 7. Evaluar el ganador final
# 8. Mostrar el resultado

# Crea funciones para aquellas operaciones que pueden ser aisladas o se repitan varias veces. En este caso:

# - Preguntar al jugador qué quiere sacar
# - Hacer una tirada aleatoria por el ordenador
# - Resolver quien ha ganado y sumarle el punto

# PASO 1. Definir una función, llamada jugador, que pregunte al jugador qué jugada quiere hacer usandos los códigos de abajo y devuelva un entero:

# 1: Piedra
# 2: Papel
# 3: Tijera

def jugador():

	respuesta = int(input("\n ¿Qué jugada quieres elegir (1:Piedra, 2:Papel, 3:Tijera)? "))
	return(respuesta)

# PASO 2. Definir una función, llamada ordenador, que seleccione aleatoriamente entre piedra, papel o tijera (utilizando el módulo random) y devuelva el resultado

def ordenador():

	opciones = ["Piedra", "Papel", "Tijera"]
	opcion = random.choice(opciones)
	return(opcion)

# PASO 3. Define una función, llamada compara, que tome como parámetros el resultado de la jugada del jugador y del ordenador, implemente la lógica del juego y devuelva el resultado, que podrá ser quien ha ganado o si ha habido empate.

def compara(jugador,ordenador):

	ganador = None

	if   (jugador == 1 and ordenador == "Tijera"): ganador = "Jugador"
	elif (jugador == 1 and ordenador == "Papel") : ganador = "Ordenador"
	elif (jugador == 1 and ordenador == "Piedra") : ganador = "Empate"

	elif (jugador == 2 and ordenador == "Tijera"): ganador = "Ordenador"
	elif (jugador == 2 and ordenador == "Papel") : ganador = "Empate"
	elif (jugador == 2 and ordenador == "Piedra") : ganador = "Jugador"

	elif (jugador == 3 and ordenador == "Tijera"): ganador = "Empate"
	elif (jugador == 3 and ordenador == "Papel") : ganador = "Jugador"
	elif (jugador == 3 and ordenador == "Piedra") : ganador = "Ordenador"

	else: print("\n Has seleccionado una opción incorrecta. Vuelve a intentarlo")

	return(ganador)

# PASO 4

# Define la parte principal del programa que vaya siguiendo lo definido en el diseño y llamando a las funciones que hemos creado cuando sea necesario.

nombre = input("\n ¿Cómo te llamas? ")

print("Hola %s vamos a jugar a piedra-papel-tijera 10 veces. ¡El que consiga más puntos gana." %nombre)

puntos_jugador = 0
puntos_ordenador= 0

# Para hacer un bucle de 10 tiradas
for cada in range(10):

	tirada_jugador = jugador()
	print(tirada_jugador)
	tirada_ordenador = ordenador()
	print(tirada_ordenador)

	ganador = compara(tirada_jugador,tirada_ordenador)

	if ganador == "Jugador":

		print("\n Yo he sacado %s" %tirada_ordenador)
		print("\n Tú has ganado esta ronda :)")
		puntos_jugador += 1

	elif ganador == "Ordenador":

		print("\n Yo he sacado %s" %tirada_ordenador)
		print("\n Esta ronda se va para casa ;)")
		puntos_ordenador += 1

	elif ganador == "Empate":

		print("\n Yo he sacado %s" %tirada_ordenador)
		print("\n Hemos sacado lo mismo, vamos a desempatar.")

	else: 
		print("\n Vaya, parece que ha habido un problema") 


if puntos_jugador > puntos_ordenador:

	puntos_finales = puntos_jugador
	print("\n Ya hemos hecho las 10 rondas")
	print("\n El resultado final es que has ganado tú con {} puntos".format(puntos_finales))

elif puntos_jugador < puntos_ordenador:

	puntos_finales = puntos_ordenador
	print("\n Ya hemos hecho las 10 rondas")
	print("\n El resultado final es que he ganado yo con {} puntos".format(puntos_finales))

else: print("\n Al final hemos empatado, bien jugado.")
