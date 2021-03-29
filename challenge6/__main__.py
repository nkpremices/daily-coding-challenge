import math


def find_min(a, b):
    if a <= b:
        return a
    else:
        return b


def find_min_coins(c, sum):
    size = len(c)

    arr = [[0] * (sum + 1) for x in range(size + 1)]

    for i in range(size + 1):
        arr[i][0] = 0

    for j in range(sum + 1):
        arr[0][j] = math.inf

    for i in range(1, size + 1):
        for j in range(1, sum + 1):
            if c[i - 1] > j:
                arr[i][j] = arr[i - 1][j]
            else:
                arr[i][j] = find_min(1 + arr[i][j - c[i - 1]], arr[i - 1][j])

    return arr[size][sum]


if __name__ == "__main__":
    coins = [5, 7, 8, 9]
    s = 49
    print("At least %s coins are required to make a sum of %s"
          % (find_min_coins(coins, s), s))
