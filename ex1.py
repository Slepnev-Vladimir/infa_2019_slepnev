'''
название файла ex1 ни о чем не говорит, поэтому нужен док-стринг, из которого будет понятно, о чем прога
'''
M = []  # не понятно, что за переменная. Надо называть понятно, типо found_primes
i = 2   # что это такое тоже не ясно

while i < 1000:
    """
    для таких целей есть цикл
    for i in range(1000):
        ...
    """

    j = 2  # что это за переменная. Нужны понятные названия
    p = 0  # и это

    # по смыслу это функция is_prime(i).
    # Если оформить в функцию, то можно будет написать гораздо более красиво и читаемо. Подумай как.
    while j < i:  # проверку можно сделать эффективнее чем на O(X)
        if i % j == 0:
            p = 1

        j += 1

    if p == 0:
        M.append(i)

    i += 1

print(M)

# оценка - 5/10
