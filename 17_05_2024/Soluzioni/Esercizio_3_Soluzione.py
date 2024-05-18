N = int(input("Inserire la dimensione della matrice: "))

matrice = []
for i in range(N):
    matrice.append([])
    for j in range(N):
        numero = int(input("Inserire l'elemento " + str(j + 1) + " della riga " + str(i + 1) + ": "))
        # matrice[-1].append(numero)
        matrice[i].append(numero)

somma_righe = []
for i in range(N):
    somma_righe.append(0)
    for j in range(N):
        somma_righe[i] += matrice[i][j]
for i in range(N):
    print("Somma riga " + str(i + 1) + ": " + str(somma_righe[i]))
print()

somma_colonne = []
for i in range(N):
    for j in range(N):
        if i == 0:
            somma_colonne.append(matrice[i][j])
        else:
            somma_colonne[j] += matrice[i][j]
for i in range(N):
    print("Somma colonne " + str(i + 1) + ": " + str(somma_colonne[i]))
print()

# METODO 1
somma_diagonale_principale = 0
for i in range(N):
    for j in range(N):
        if i == j:
            somma_diagonale_principale += matrice[i][j]
print("Somma diagonale principale: " + str(somma_diagonale_principale))
print()

# METODO 2
somma_diagonale_principale = 0
for i in range(N):
    somma_diagonale_principale += matrice[i][i]
print("Somma diagonale principale: " + str(somma_diagonale_principale))
print()

# METODO 1
somma_diagonale_secondaria = 0
for i in range(N):
    for j in range(N):
        if i == N - j - 1:
            somma_diagonale_secondaria += matrice[i][j]
print("Somma diagonale secondaria: " + str(somma_diagonale_secondaria))
print()

# METODO 2
somma_diagonale_secondaria = 0
for i in range(N):
    somma_diagonale_secondaria += matrice[i][N - i - 1]
print("Somma diagonale secondaria: " + str(somma_diagonale_secondaria))
print()
