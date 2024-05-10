# METODO 1
f = open("testo.txt", "r")
i = 0
cont = 0
for l in f:
    riga_senza_a_capo = l.strip()
    lista_parole_riga = riga_senza_a_capo.split(" ")
    i += 1
    print("Il numero di parole nella riga " + str(i) + " è: " + str(len(lista_parole_riga)))
    cont += len(lista_parole_riga)
print(cont)
f.close()

print()
# METODO 2
i = 0
cont = 0
with open("testo.txt", "r") as f:
    for l in f:
        riga_senza_a_capo = l.strip()
        lista_parole_riga = riga_senza_a_capo.split(" ")
        i += 1
        print("Il numero di parole nella riga " + str(i) + " è: " + str(len(lista_parole_riga)))
        cont += len(lista_parole_riga)
print(cont)

print()
# METODO 3
i = 0
cont = 0
f = open("testo.txt", "r").readlines()
for l in f:
    riga_senza_a_capo = l.strip()
    lista_parole_riga = riga_senza_a_capo.split(" ")
    i += 1
    print("Il numero di parole nella riga " + str(i) + " è: " + str(len(lista_parole_riga)))
    cont += len(lista_parole_riga)
print(cont)

print()
# METODO 4
i = 0
cont = 0
f = open("testo.txt", "r")
s = f.readline()
while s != "":
    riga_senza_a_capo = s.strip()
    lista_parole_riga = riga_senza_a_capo.split(" ")
    i += 1
    print("Il numero di parole nella riga " + str(i) + " è: " + str(len(lista_parole_riga)))
    cont += len(lista_parole_riga)
    s = f.readline()
print(cont)
f.close()