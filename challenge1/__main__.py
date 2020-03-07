def add_up_to(key, store):
    for _ in store:
        for __ in store:
            if _ == __:
                pass
            elif _ + __ == key:
                return True
            else:
                pass
    return False


if __name__ == "__main__":
    print(add_up_to(25, [10, 15, 3, 7]))
    print('--end--')
