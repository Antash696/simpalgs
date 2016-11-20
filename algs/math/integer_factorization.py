def prime_factors(N):
    n = round(N ** 0.5) + 1
    i = 1
    factors = []
    while True:
        i += 1
        if N % i == 0:
            factors.append(i)
            N = N // i
            i = 1
            n = round(N ** 0.5) + 1
        if i > n:
            if N != 1:
                factors.append(N)
            break
    return factors
