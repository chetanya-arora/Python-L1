ex = ["mix", "xyz", "apple", "xanadu", "aardvark"]


def sort_the_list(lst):
    strings_without_x = []
    strings_with_x = []
    new_list = []
    for item in lst:
        if item[0] == "x":
            strings_with_x.append(item)
        else:
            strings_without_x.append(item)

    new_list = sorted(strings_with_x) + sorted(strings_without_x)
    return new_list


print(sort_the_list(ex))