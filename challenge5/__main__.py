def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(construct):
    return construct(lambda a, b: a)


def cdr(construct):
    return construct(lambda a, b: b)


if __name__ == "__main__":
    print(car(cons(3, 4)))
    print(cdr(cons(3, 4)))
    print('----end----')
