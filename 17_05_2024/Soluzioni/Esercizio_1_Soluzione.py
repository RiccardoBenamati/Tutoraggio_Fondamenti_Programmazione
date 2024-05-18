f = open("testo.txt", "r")
cont_a = 0
cont_b = 0
contatori = [0, 0]
# metodo 1
for l in f:
    for i in l.strip().split(" "):
        for ii in i:
            if ii == "a":
                cont_a += 1
                contatori[0] += 1
                print("A", end="")
            elif ii == "b":
                cont_b += 1
                contatori[1] += 1
                print("B", end="")
            else:
                print(ii, end="")
        print(" ", end="")
    print()
f.close()
print("A: " + str(cont_a))
print("B: " + str(cont_b))
print("A: " + str(contatori[0]))
print("B: " + str(contatori[1]))
print()

# metodo 2
cont_a = 0
cont_b = 0
contatori = [0, 0]
with open("testo.txt", "r") as f:
    for l in f:
        for i in l.strip().split(" "):
            for ii in i:
                if ii == "a":
                    cont_a += 1
                    contatori[0] += 1
                    print("A", end="")
                elif ii == "b":
                    cont_b += 1
                    contatori[1] += 1
                    print("B", end="")
                else:
                    print(ii, end="")
            print(" ", end="")
        print()
print("A: " + str(cont_a))
print("B: " + str(cont_b))
print("A: " + str(contatori[0]))
print("B: " + str(contatori[1]))
print()

# metodo 3
cont_a = 0
cont_b = 0
contatori = [0, 0]
f = open("testo.txt", "r").readlines()
for l in f:
    for i in l.strip():
        if i == "a":
            cont_a += 1
            contatori[0] += 1
            print("A", end="")
        elif i == "b":
            cont_b += 1
            contatori[1] += 1
            print("B", end="")
        else:
            print(i, end="")
    print()
print("A: " + str(cont_a))
print("B: " + str(cont_b))
print("A: " + str(contatori[0]))
print("B: " + str(contatori[1]))
print()

# metodo 4
cont_a = 0
cont_b = 0
contatori = [0, 0]
f = open("testo.txt", "r")
s = f.readline()
while s != "":
    for i in s.strip():
        if i == "a":
            cont_a += 1
            contatori[0] += 1
            print("A", end="")
        elif i == "b":
            cont_b += 1
            contatori[1] += 1
            print("B", end="")
        else:
            print(i, end="")
    print()
    s = f.readline()
f.close()
print("A: " + str(cont_a))
print("B: " + str(cont_b))
print("A: " + str(contatori[0]))
print("B: " + str(contatori[1]))