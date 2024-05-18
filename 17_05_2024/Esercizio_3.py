N = int(input("Inserire la dimensione della matrice: "))

matrice = []
for i in range(N):
    matrice.append([])
    for j in range(N):
        numero = int(input("Inserire un numero per la riga " +
                           str(i + 1) + " e la colonna " + str(j + 1) + ": "))
        matrice[i].append(numero)
for i in range(N):
    print(matrice[i])

"""N = 3
matrice = [
    [5, 7, 3],
    [8, 2, 4],
    [9, 1, 5]
]"""

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