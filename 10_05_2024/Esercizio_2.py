a = [-5, 4, 7, -1, 10, 21, 9]
b = [4, -1, 9, -7]
i = 0
j = 0
while i < len(a) and j < len(b):
    if a[i] == b[j]:
        i += 1
        j += 1
    else:
        i += 1
if j == len(b):
    print(True)
else:
    print(False)