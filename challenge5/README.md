##### This problem was asked by Jane Street.

# Challenge 5

### Question

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

```.env
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```

Implement `car` and `cdr`

### Solution

* Implement car and cdr using lambda functions returning the expected element
