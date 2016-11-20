def GCD(x, y):  # Euclidean Algorithm
    if x == y:
        return x
    if x > y:
        x, y = y, x
    while x != 0:
        x, y = y % x, x
    return y
