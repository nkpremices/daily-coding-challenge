
def addUpTo(key, store):
    for _ in store:
        for __ in store:
            if _ == __:
                pass
            elif _ + __ == key:
                return True
            else:
                pass
    return False


print(addUpTo(25, [10, 15, 3, 7]))

print('--end--')
