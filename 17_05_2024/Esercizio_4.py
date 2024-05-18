# METODO 1
f = open("matrice.txt", "r")
matrice = []
for riga in f:
    lista = []
    lista_elementi = riga.strip().split(" ")
    for elemento in lista_elementi:
        lista.append(int(elemento))
    matrice.append(lista)
N = len(matrice)
f.close()

# METODO 2
with open("matrice.txt", "r") as f:
    matrice = []
    for riga in f:
        lista = []
        lista_elementi = riga.strip().split(" ")
        for elemento in lista_elementi:
            lista.append(int(elemento))
        matrice.append(lista)
    N = len(matrice)

somma_riga = []
for i in range(N):
    somma_riga.append(sum(matrice[i]))

somma_colonna = []
for i in range(N):
    for j in range(N):
        if i == 0:
            somma_colonna.append(matrice[i][j])
        else:
            somma_colonna[j] += matrice[i][j]

# METODO 1
diagonale_principale = 0
for i in range(N):
    for j in range(N):
        if i == j:
            diagonale_principale += matrice[i][j]

# METODO 2
diagonale_principale = 0
for i in range(N):
    diagonale_principale += matrice[i][i]

# METODO 1
diagonale_secondaria = 0
for i in range(N):
    for j in range(N):
        if j == N - 1 - i:
            diagonale_secondaria += matrice[i][j]

# METODO 2
diagonale_secondaria = 0
for i in range(N):
    diagonale_secondaria += matrice[i][N - 1 - i]

# OUTPUT
for i in range(N):
    print("Somma della riga " + str(i + 1) + ": " + str(somma_riga[i]))

for i in range(N):
    print("Somma della colonna " + str(i + 1) + ": " + str(somma_colonna[i]))

print("Somma diagonale principale: " + str(diagonale_principale))
print("Somma diagonale secondaria: " + str(diagonale_secondaria))