from copy import copy

# METODO 1: LISTE
n = -1
numeri_inseriti = []
while n != 0:
    n = input("Inserisci un numero maggiore o uguale a 0: ")
    n = int(n)
    if n != 0:
        numeri_inseriti.append(n)
print(numeri_inseriti)
# METODO 1.1: VARIABILE
valore_minimo = 100000000000000000
for i in numeri_inseriti:
    if i < valore_minimo:
        valore_minimo = i
print(valore_minimo)
# METODO 1.2: FUNZIONE MIN
valore_minimo = min(numeri_inseriti)
print(valore_minimo)
valore_massimo = max(numeri_inseriti)
print(valore_massimo)

# METODO 2: VARIABILE
n = input("Inserisci un numero maggiore o uguale a 0: ")
n = int(n)
if n != 0:
    valore_minimo = copy(n)
else:
    valore_minimo = "Nessun numero inserito"

while n != 0:
    n = input("Inserisci un numero maggiore o uguale a 0: ")
    n = int(n)
    if n < valore_minimo and n != 0:
        valore_minimo = n
print(valore_minimo)