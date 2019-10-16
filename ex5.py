# the program contains a function that displays
# a list of unique elements from this array


array = [1, 1, 1, 2, 3, 3, 4, 153, 153, 44]


def list_set(array):
    return(list(set(array)))


print(list_set(array))
