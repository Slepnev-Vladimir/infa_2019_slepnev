# the program contains a function
# that subtracts one list from another

list_1 = [1, 2, 3, 4, 5, 6, 153]
list_2 = [3, 4, 5, 6, 7, 8, 9]


def difference(list_1, list_2):
    return(list(set(list_1) - set(list_2)))


print(difference(list_1, list_2))
