N = int(input("Inserire un numero N: "))
# Metodo 1
var = 0
for i in range(N):
    for j in range(N):
        if j == 0 or j == N - 1:
            var += 1
            print(var, end="\t")
        else:
            print("*", end="\t")
    print()

print()
# Metodo 2
var = 1
for i in range(N):
    for j in range(N):
        if j == 0:
            print(i + var, end="\t")
            var += 1
        elif j == N - 1:
            print(i + var, end="\t")
        else:
            print("*", end="\t")
    print()