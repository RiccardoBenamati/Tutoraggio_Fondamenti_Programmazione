N = int(input("Inserire N: "))

for i in range(N):
    for j in range(N):
        if i == 0:
            print(j + 1, end="\t")
        elif j == N - 1:
            print(N + i, end="\t")
        elif i == N - 1:
            print(3 * N - 2 - j, end="\t")
        elif j == 0:
            print(4 * N - 3 - i, end="\t")
        else:
            print("*", end="\t")
    print()