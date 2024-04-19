# METODO 1
# INPUT
while True:
    T = input("Inserisci una temperatura in Celsius: ")
    T = float(T)  # la stringa inserita diventa un numero
    if T < -273.15:
        # OUTPUT
        print("ATTENZIONE: è stata una temperatura sbagliata!")
        break   # comando che fa uscire dal ciclo while ma NON termina da solo il programma
    else:
        F = 9/5 * T + 32
        K = T + 273.15
        print("Fahrenheit: " + str(F))
        print("Kelvin: " + str(K))
        print()

# METODO 2
T = input("Inserisci una temperatura in Celsius: ")
T = float(T)  # la stringa inserita diventa un numero
while T >= -273.15:
    F = 9 / 5 * T + 32
    K = T + 273.15
    print("Fahrenheit: " + str(F))
    print("Kelvin: " + str(K))
    print()
    T = input("Inserisci una temperatura in Celsius: ")
    T = float(T)  # la stringa inserita diventa un numero
print("ATTENZIONE: è stata una temperatura sbagliata!")