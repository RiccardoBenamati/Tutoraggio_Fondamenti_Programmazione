f = open("testo.txt", "r")
# metodo 1
lista = []
i = 0
for l in f:
    parole = l.strip().split()
    i += 1
    print("Parole nella riga " + str(i) + ": " + str(len(parole)))
    for p in parole:
        lista.append(p)
print(len(lista))
f.close()

print()
# metodo 2
lista = []
i = 0
with open("testo.txt", "r") as f:
    for l in f:
        parole = l.strip().split()
        i += 1
        print("Parole nella riga " + str(i) + ": " + str(len(parole)))
        for p in parole:
            lista.append(p)
print(len(lista))

print()
# metodo 3
lista = []
f = open("testo.txt", "r").readlines()
i = 0
for l in f:
    parole = l.strip().split(" ")
    i += 1
    print("Parole nella riga " + str(i) + ": " + str(len(parole)))
    for p in parole:
        lista.append(p)
print(len(lista))

print()
# metodo 4
lista = []
f = open("testo.txt", "r")
s = f.readline()
i = 0
while s != "":
    parole = s.strip().split(" ")
    i += 1
    print("Parole nella riga " + str(i) + ": " + str(len(parole)))
    for p in parole:
        lista.append(p)
    s = f.readline()
print(len(lista))
