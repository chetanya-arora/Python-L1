ex = ["axa", "xyz", "gg", "x", "yyy"]


def count_number_of_strings(lst):
    count = 0
    for item in lst:
        if len(item) >= 2:
            if item[0] == item[-1]:
                count += 1
    return count


print(count_number_of_strings(ex))