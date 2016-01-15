# Algorithms generating Collatz sequence using memoization


# algorithm returning length of Collatz sequence
def collatz_length(start, memo):
    """memo has to be initialized with dict {2: 1}"""
    n = start
    seq_l = 0
    while n > 1:
        if memo.get(n, False):
            if n != start:
                memo[start] = memo[n] + seq_l
            return memo[n] + seq_l
        if n % 2 == 0:
            n = n // 2
            seq_l += 1
        else:
            n = (n*3 + 1) // 2  # n*3+1 always returns even value so we "skip" it.
            seq_l += 2


# algorithm returning whole Collatz sequence
# TODO
