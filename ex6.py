M1 = [1, 2, 3, 4, 5, 6, 153]
M2 = [3, 4, 5, 6, 7, 8, 9]
M3 = []
i = 0

while i < len(M1):
    j = 0
    p = 0

    while j < len(M2):
        if M1[i] == M2[j]:
            p = 1

        j += 1

    if p == 0:
        M3.append(M1[i])

    i += 1

print(M3)