# Tienes una caja de regalos de Navidad que Santa Claus quiere entregar a los niños.
# Cada regalo está representado por una cadena. Santa Claus tiene un trineo que
# puede llevar un peso limitado, y cada regalo dentro de la caja tiene un peso que es
# igual al número de letras en el nombre del regalo.

# Santa Claus también tiene una
# lista de renos que pueden ayudarlo a entregar los regalos. Cada reno tiene un límite
# de peso máximo que puede llevar. El límite de peso máximo de cada reno es igual a
# dos veces el número de letras en su nombre.

# Tu tarea es implementar una función distributeGifts(packOfGifts, reindeers) que
# recibe una caja de regalos y una lista de renos y devuelve el número máximo de
# cajas de estos regalos que Santa Claus puede entregar a los niños. Las cajas de
# regalos no se pueden dividir.

# Funcion para encontrar renos
# Funcion para encontrar regalos

Regalo1=input("Regalo1:")
Regalo2=input("Regalo2:")
Regalo3=input("Regalo3:")

print("----------------------------------------------")

Reno1="Rodolfo"
Reno2="Adan"
Reno3="Eva"

ListaRegalos= (Regalo1,Regalo2,Regalo3)
ListaRenos = (Reno1,Reno2,Reno3)
CargaRenos = int(len(Reno1 * 2) + len(Reno2 * 2) + len(Reno3 * 2))
CajaRegalos = int(len(Regalo1) + len(Regalo2) + len(Regalo3))

def encontrar_renos():
    print("Lista de renos:")
    for reno in ListaRenos:
        print(f"{reno}")

def encontrar_regalos():
    print("Lista de regalos:")
    for regalo in ListaRegalos:
        print(f"{regalo}")

print(encontrar_renos())
print("-------------------------------------------------")
print(encontrar_regalos())

print("----------------------------------------------------------------")
print(f"Peso maximo de los Caja de regalos:{CajaRegalos}KG")
print(f"Carga maxima por los renos:{CargaRenos}KG")
print(f"Carga maxima del trineo:{CargaRenos}KG")

def distribucion (CargaRenos,CajaRegalos):
    R = CargaRenos // CajaRegalos
    return f"Las cajas de regalos que se pueden cargar:{R} cajas"

print(distribucion(CargaRenos, CajaRegalos))

# Resultado= ListaRenos // CajaRegalos
# pint(f"Las cajas de regalos que se pueden cargar:{Resultado}")






