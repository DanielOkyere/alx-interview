#!/usr/bin/python3
"""Prime game """


def isWinner(x, nums):
    """Determines the winner for x rounds"""
    if x < 1 or not nums:
        return None
    m_win, n_win = 0, 0
    n = max(nums)
    primes = [True for _ in range(1, n+1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i+1, n+1, i):
            primes[j-1] = False

    for _, n in zip(range(x), nums):
        p_count = len(list(filter(lambda x: x, primes[0: n])))
        n_win += p_count % 2 == 0
        m_win += p_count % 2 == 1
    if m_win == n_win:
        return None
    return 'Maria' if m_win > n_win else 'Ben'
