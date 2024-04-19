import time

N = 10000
# METODO ESTESO
inizio = time.time()
for i in range(N + 1):
    for j in range(N + 1):
        somma = i + j
        if somma == N:
            print("(" + str(i) + "; " + str(j) + ")", end=", ")
fine = time.time()
print("Tempo metodo esteso: " + str(fine - inizio))

print()
# METODO PIU' EFFICIENTE
inizio = time.time()
for i in range(N + 1):
    for j in range(i, N + 1):
        somma = i + j
        if somma == N:
            print("(" + str(i) + "; " + str(j) + ")", end=", ")
fine = time.time()
print("Tempo metodo efficiente: " + str(fine - inizio))