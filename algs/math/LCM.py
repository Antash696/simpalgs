from GCD import GCD


def LCM(x, y):  # for multiple x, y use recursion.
    return x * y // GCD(x, y)

