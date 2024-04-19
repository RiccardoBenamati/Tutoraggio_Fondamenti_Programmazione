N = 5
numeri = []
for i in range(N):
    n = int(input("Inserire un numero: "))
    numeri.append(n)

# METODO 1
for i in numeri:
    for j in range(i):
        print("*", end="")
    print()


# METODO 2
for i in range(0, len(numeri), 1):
    for j in range(numeri[i]):
        print("*", end="")
    print()
