N = int(input("Inserire la dimensione della matrice: "))

for i in range(N):
    for j in range(N):
        if i == 0:
            print(j + 1, end="\t")
        elif i == N - 1:
            print(3 * N - j - 2, end="\t")
        else:
            if j == 0:
                print(4 * N - i - 3, end="\t")
            elif j == N - 1:
                print(N + i, end="\t")
            else:
                print("*", end="\t")
    print()