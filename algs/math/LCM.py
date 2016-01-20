from GCD import GCD


def LCM(x, y):  # for multiple x, y use recursion.
    return x * y // GCD(x, y)


def LCM2(x, y):
    lcm = x
    while lcm % y != 0:
        lcm += x
    return lcm
