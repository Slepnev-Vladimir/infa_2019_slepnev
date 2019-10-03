M = [5, 4, 3, 2, 1, 10, 420, 30, 0]
i = 0

while i < 9:
    j = i
    p = i

    while j < 9:
        if M[j] < M[p]:
            p = j

        j += 1

    if M[p] < M[i]:
        a = M[i]
        M[i] = M[p]
        M[p] = a

    i += 1

print(M)
