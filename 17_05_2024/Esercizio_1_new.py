# METODO 1
contatore_a = 0
contatore_b = 0
f = open("testo.txt", "r")
for riga in f:
    for lettera in riga.strip():
        if lettera == "a":
            contatore_a += 1
            print("A", end="")
        elif lettera == "b":
            contatore_b += 1
            print("B", end="")
        else:
            print(lettera, end="")
    print()
f.close()
print("Le 'a' sono: " + str(contatore_a))
print("Le 'b' sono: " + str(contatore_b))

print("\n----------------------------------\n")

# METODO 2
contatore = [0, 0]
f = open("testo.txt", "r")
for riga in f:
    for lettera in riga.strip():
        if lettera == "a":
            contatore[0] += 1
            print("A", end="")
        elif lettera == "b":
            contatore[1] += 1
            print("B", end="")
        else:
            print(lettera, end="")
    print()
f.close()
print("Le 'a' sono: " + str(contatore[0]))
print("Le 'b' sono: " + str(contatore[1]))