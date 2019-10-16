# the program contains a function which makes sorting a choice

sort_array = [-1, 5, 4, 3, 2, 1, 10, 420, 30, 0]


def min_coord(array):
    """finds the coordinate of the minimum element"""
    min_coord = 0

    for coord in range(0, len(array)):
        if array[coord] < array[min_coord]:
            min_coord = coord

    return(min_coord)


def sorting(sort_array):
    for coord_1 in range(0, len(sort_array)):
        coord_2 = min_coord(sort_array[coord_1:]) + coord_1

        if sort_array[coord_1] > sort_array[coord_2]:
            sort_array[coord_1], sort_array[coord_2] = sort_array[coord_2], sort_array[coord_1]

    return(sort_array)


print(sorting(sort_array))
