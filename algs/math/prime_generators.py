from algs.math.primality_check import is_prime


def generate_primes_upto(n):
    primes = [2, 3]
    i = 3
    while i <= n:
        i += 2
        if is_prime(i):
            primes.append(i)
    return primes
