import random

list_numero = []
random.seed(1) # per mantenere i numeri generati sempre uguali durante le varie iterazioni
N = random.randint(1, 10)
print(N)
iterazioni = int(input("Inserire un numero: "))
i = 0
while i < iterazioni:
    i += 1
    if N % 2 == 0:
        N = N / 2
    else:
        N = N * 3 + 1
    list_numero.append(N)
print(list_numero)
