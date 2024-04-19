N = 10
iterazione = 0

T = input("Inserisci una temperatura in Celsius: ")
T = float(T)  # la stringa inserita diventa un numero
while T >= -273.15 and iterazione < N:
    iterazione += 1
    print("Iterazione: " + str(iterazione))
    F = 9 / 5 * T + 32
    K = T + 273.15
    print("Fahrenheit: " + str(F))
    print("Kelvin: " + str(K))
    print()
    T = input("Inserisci una temperatura in Celsius: ")
    T = float(T)  # la stringa inserita diventa un numero
print("ATTENZIONE: è stata una temperatura sbagliata oppure ne sono state inserite troppe!")