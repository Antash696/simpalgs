from algs.math.primality_check import is_prime


def generate_primes_upto(n):
    primes = [2, 3]
    i = 3
    while i <= n:
        i += 2
        if is_prime(i):
            primes.append(i)
    return primes


def sieve(N):
    composite = set()
    primes = []
    for i in range(2, N+1):
        if i not in composite:
            primes.append(i)
            composite.update(range(i*i, N+1, i))
    return primes
