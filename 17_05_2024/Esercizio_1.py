# METODO 1
f = open("testo.txt", "r")
for l in f:
    stringa_senza_a_capo = l.strip()
    for lettera in stringa_senza_a_capo:
        if lettera == "a":
            print("A", end="")
        elif lettera == "b":
            print("B", end="")
        else:
            print(lettera, end="")
    print() # comando presente per la funzione strip alla riga 4 che toglie a capo alla riga
f.close()

# METODO 2
with open("testo.txt", "r") as f:
    for l in f:
        stringa_senza_a_capo = l.strip()
        for lettera in stringa_senza_a_capo:
            if lettera == "a":
                print("A", end="")
            elif lettera == "b":
                print("B", end="")
            else:
                print(lettera, end="")
        print()