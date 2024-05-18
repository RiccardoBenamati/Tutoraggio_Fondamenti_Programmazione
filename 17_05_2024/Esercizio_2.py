# METODO 1
contatore_a = 0
contatore_b = 0
f = open("testo.txt", "r")
w = open("output.txt", "w")
for riga in f:
    for lettera in riga.strip():
        if lettera == "a":
            contatore_a += 1
            print("A", end="")
            w.write("A")
        elif lettera == "b":
            contatore_b += 1
            print("B", end="")
            w.write("B")
        else:
            print(lettera, end="")
            w.write(lettera)
    print()
    w.write("\n")
f.close()
w.close()
print("Le 'a' sono: " + str(contatore_a))
print("Le 'b' sono: " + str(contatore_b))

print("\n---------------------------------------------------\n")

# METODO 2
contatore_a = 0
contatore_b = 0
with open("testo.txt", "r") as f:
    with open("output.txt", "w") as w:
        for riga in f:
            for lettera in riga.strip():
                if lettera == "a":
                    print("A", end="")
                    contatore_a += 1
                    w.write("A")
                elif lettera == "b":
                    print("B", end="")
                    contatore_b += 1
                    w.write("B")
                else:
                    print(lettera, end="")
                    w.write(lettera)
            print()
            w.write("\n")
print("Le 'a' sono: " + str(contatore_a))
print("Le 'b' sono: " + str(contatore_b))

print("\n---------------------------------------------------\n")

# METODO 3
contatore_a = 0
contatore_b = 0
f = open("testo.txt", "r").readlines()
w = open("output.txt", "w")
for riga in f:
    for lettera in riga.strip():
        if lettera == "a":
            print("A", end="")
            contatore_a += 1
            w.write("A")
        elif lettera == "b":
            print("B", end="")
            contatore_b += 1
            w.write("B")
        else:
            print(lettera, end="")
            w.write(lettera)
    print()
    w.write("\n")
w.close()
print("Le 'a' sono: " + str(contatore_a))
print("Le 'b' sono: " + str(contatore_b))

print("\n---------------------------------------------------\n")

# METODO 4
contatore_a = 0
contatore_b = 0
f = open("testo.txt", "r")
w = open("output.txt", "w")
s = f.readline()
while s != "":
    for lettera in s.strip():
        if lettera == "a":
            print("A", end="")
            contatore_a += 1
            w.write("A")
        elif lettera == "b":
            print("B", end="")
            contatore_b += 1
            w.write("B")
        else:
            print(lettera, end="")
            w.write(lettera)
    print()
    w.write("\n")
    s = f.readline()
f.close()
w.close()
print("Le 'a' sono: " + str(contatore_a))
print("Le 'b' sono: " + str(contatore_b))