def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True


def is_prime2(p):
    if p % 2 == 0 and p != 2:
        return False
    for i in range(3, round(p ** 0.5) + 1, 2):
        if p % i == 0:
            return False
    return True
