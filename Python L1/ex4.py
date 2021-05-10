ex = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]


def last(x):
    return x[-1]


def sort_the_list(lst):
    return sorted(lst, key=last)


print(sort_the_list(ex))