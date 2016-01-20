def is_prime(p):
    if p % 2 == 0 and p != 2:
        return False
    for i in range(3, round(p ** 0.5) + 1, 2):
        if p % i == 0:
            return False
    return True
