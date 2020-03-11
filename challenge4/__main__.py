
def get_lowest_positive_integer(store: list):
    # get rid of all negative numbers then sort the list
    dump = [_ for _ in store if _ > 0]
    dump.sort()

    # create a list full of all integer up to the highest
    dump_filled = [_ for _ in range(1, dump[-1] + 1)]

    # Return the highest + 1 if the length is the same
    if len(dump) == len(dump_filled):
        return dump[-1] + 1

    # Otherwise, find the difference then sort it
    diff = [_ for _ in dump_filled if _ not in dump]
    diff.sort()

    # Return the first item of the difference
    return diff[0]


if __name__ == "__main__":
    print(get_lowest_positive_integer([3, 4, -1, 1]))
    print(get_lowest_positive_integer([1, 2, 0]))
    print('----end----')
