print("******")
print("AGENDA")
print("******")

# 1. Crear un diccionario vacío al iniciarse
# 2. Mostrar un menú al usuario que le permita elegir entre: crear, modificar o eliminar un registro, o salir del programa
# 3. Resolver esa acción que ha eligido el usuario y después volver al menú principal (salvo que haya elegido salir en cuyo caso el programa termina)
# 4. Si ha elegido crear, el programa preguntará el nombre y el teléfono y lo añadirá al diccionario siendo el nombre la clave y el teléfono el valor
# 5. Si ha elegido borrar, el programa pedirá un nombre y borrará ese registro de la agenda
# 6. Si ha elegido modificar, el programa preguntará el nombre y el teléfono, buscará ese nombre en la agenda y modificará su valor (el teléfono)

# Crea funciones para aquellas operaciones que pueden ser aisladas o se repitan varias veces. En este caso:

# - Los procesos de cear, modificar y borrar usuarios

# PASO 1. Crea un diccionario vacío llamado agenda y define, siguiendo el diseño indicado, funciones para:

# Crear un registro
# Borrar un registro
# Modificar un registro

agenda = diccionario = dict()

def crear():

	nombre = input("Nombre: ")
	telefono = input("Teléfono: ")
	agenda[nombre] = telefono

	print("\n El registro se ha creado correctamente.")


def borrar():

	nombre_aborrar = input("¿Qué nombre quieres borrar? ")
	del agenda[nombre_aborrar]

	print("\n El registro se ha borrado correctamente.")
	
def modificar():

	nombre_amodificar = input("Introduce el nombre: ")
	telefono_amodificar = input("Introduce el nuevo número de teléfono: ")
	agenda[nombre_amodificar] = telefono_amodificar

	print("\n El registro se ha modificado correctamente.")


# PASO 2. Crea la lógica principal del programa donde se muestre un menú con las siguientes opciones que estará activo y funcionando hasta que el usuario elija la opción de Salir:

# - Crear un nuevo registro
# - Modificar un registro existente
# - Eliminar un registro
# - Salir

opcion = 0

while opcion != 4:

	print("1. Crear un nuevo registro")
	print("2. Modificar un registro existente")
	print("3. Eliminar un registro")
	print("4. Salir")

	opcion = int(input("\n Elige una opción: "))

	if   opcion == 1: crear()
	elif opcion == 2: modificar()
	elif opcion == 3: borrar()

	else: print("\n Esa opción no es válida. Elige una opción del menú.")

	print("\n\n")

# PASO 3. Crea, modifica y borra unos cuantos registros, y cuando hayas terminado y elegido salir imprime la agenda por consola y comprueba el resultado.

print(agenda)
