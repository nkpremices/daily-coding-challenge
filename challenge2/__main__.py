
def array_builder(store):
    temp = []
    for _ in store:
        product = 1
        for __ in store:
            if _ == __:
                pass
            else:
                product *= __
        temp.append(product)
    return temp


if __name__ == "__main__":
    print(array_builder([3, 2, 1]))
    print('--end--')
