f = open("testo.txt", "r")
w = open("output.txt", "w")
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
                w.write("A")
                print("A", end="")
            elif ii == "b":
                cont_b += 1
                contatori[1] += 1
                w.write("B")
                print("B", end="")
            else:
                w.write(ii)
                print(ii, end="")
        w.write(" ")
        print(" ", end="")
    w.write("\n")
    print()
f.close()
w.close()
print("A: " + str(cont_a))
print("B: " + str(cont_b))
print("A: " + str(contatori[0]))
print("B: " + str(contatori[1]))
print()

# metodo 2
cont_a = 0
cont_b = 0
contatori = [0, 0]
with open("output.txt", "w") as w:
    with open("testo.txt", "r") as f:
        for l in f:
            for i in l.strip().split(" "):
                for ii in i:
                    if ii == "a":
                        cont_a += 1
                        contatori[0] += 1
                        w.write("A")
                        print("A", end="")
                    elif ii == "b":
                        cont_b += 1
                        contatori[1] += 1
                        w.write("B")
                        print("B", end="")
                    else:
                        w.write(ii)
                        print(ii, end="")
                w.write(" ")
                print(" ", end="")
            w.write("\n")
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
w = open("output.txt", "w")
for l in f:
    for i in l.strip():
        if i == "a":
            cont_a += 1
            contatori[0] += 1
            w.write("A")
            print("A", end="")
        elif i == "b":
            cont_b += 1
            contatori[1] += 1
            w.write("B")
            print("B", end="")
        else:
            w.write(i)
            print(i, end="")
    w.write("\n")
    print()
w.close()
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
w = open("output.txt", "w")
s = f.readline()
while s != "":
    for i in s.strip():
        if i == "a":
            cont_a += 1
            contatori[0] += 1
            w.write("A")
            print("A", end="")
        elif i == "b":
            cont_b += 1
            contatori[1] += 1
            w.write("B")
            print("B", end="")
        else:
            w.write(i)
            print(i, end="")
    w.write("\n")
    print()
    s = f.readline()
print("A: " + str(cont_a))
print("B: " + str(cont_b))
print("A: " + str(contatori[0]))
print("B: " + str(contatori[1]))
f.close()
w.close()
