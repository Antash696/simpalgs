""" Algorithms generating Collatz sequence """


def collatz_length(start, memo):
    """ Algorithm returning length of Collatz sequence
            starting from a given integer.
        Uses memoization of previously computed lenghts.
        MEMO has to be initialized with dict {2: 1}"""
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
            n = (n * 3 + 1) // 2  # returns even value so -> // 2 skip's it.
            seq_l += 2


def collatz_seq(start):
    """ Algorithm returning whole Collatz sequence
        starting from a given interger. """
    n = start
    seq = [start]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            seq.append(n)
        else:
            n = (n * 3 + 1) // 2
            seq.extend([n * 2, n])
    return seq
