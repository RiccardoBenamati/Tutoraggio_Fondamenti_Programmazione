N = int(input("Inserisci un numero positivo: "))
# trovare K
K = 0
somma = 0
while somma <= N:
    K += 1
    somma += K

# se N=20 -> somma = 21 & K = 6
somma = somma - K
print(somma)

K = K - 1
print(K)