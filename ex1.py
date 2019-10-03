M = []
i = 2

while i < 1000:
    j = 2
    p = 0

    while j < i:
        if i % j == 0:
            p = 1

        j += 1

    if p == 0:
        M.append(i)

    i += 1

print(M)

