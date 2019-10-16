# the program seaches for primes up to 1000

found_primes = [2]


def check_prime(number):
    flag = 0

    for divider in range(0, len(found_primes)):
        if number % found_primes[divider] == 0:
            flag = 1

    if flag == 0:
        found_primes.append(number)


for number in range(3, 1000, 2):
    check_prime(number)

print(found_primes)
