import time


def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)


def memo_fib(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = memo_fib(n-1, memo) + memo_fib(n-2, memo)
    return memo[n]


numbers = list(range(36))
fib_times = []
memo_fib_times = []
for n in numbers:
    start = time.time()
    fib(n)
    end = time.time()
    fib_times.append(end-start)
    start = time.time()
    memo_fib(n)
    end = time.time()
    memo_fib_times.append(end-start)