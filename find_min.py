def find_minimum(arr):
    minimum = arr[0]
    # At every Index compare its value with minimum and if its less
    # then make that index value new minimum value
    for val in arr:
        if val < minimum:
            minimum = val

    return minimum