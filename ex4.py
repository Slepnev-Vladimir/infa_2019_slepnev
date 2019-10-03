sp = {'q' : 1, 'w' : 2, 'e' : 3, 'r' : 4}
a = 3

M = []

for key in sp:
    if sp[key] <= a:
        M.append(key)

print(M)
