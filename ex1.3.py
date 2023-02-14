def mem_func(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = mem_func(n-1, memo) + mem_func(n-2, memo)
    return memo[n]