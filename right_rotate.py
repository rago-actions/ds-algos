def right_rotate(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]