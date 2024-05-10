a = [-5, 4, 7, -1, 10, 21, 9, -7]
b = [4, -1, 9, -7]
i = 0
j = 0
while j < len(b) and i < len(a):
    if b[j] == a[i]:
        i = i + 1
        j = j + 1
    else:
        i = i + 1

if j == len(b):
    print(True)
else:
    print(False)