# METODO 1
matrice = []
f = open("matrice.txt", "r")
for l in f:
    matrice.append([])
    riga = l.strip().split(" ")
    for i in range(len(riga)):
        matrice[-1].append(int(riga[i]))
N = len(matrice)
f.close()

# METODO 2
matrice = []
with open("matrice.txt", "r") as f:
    for l in f:
        matrice.append([])
        riga = l.strip().split(" ")
        for i in range(len(riga)):
            matrice[-1].append(int(riga[i]))
N = len(matrice)

# METODO 3
matrice = []
f = open("matrice.txt", "r").readlines()
for l in f:
    matrice.append([])
    riga = l.strip().split(" ")
    for i in range(len(riga)):
        matrice[-1].append(int(riga[i]))
N = len(matrice)

# METODO 4
matrice = []
f = open("matrice.txt", "r")
s = f.readline()
while s != "":
    matrice.append([])
    riga = s.strip().split(" ")
    for i in range(len(riga)):
        matrice[-1].append(int(riga[i]))
    s = f.readline()
N = len(matrice)

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