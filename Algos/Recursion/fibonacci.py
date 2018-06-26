# using recursion
def fibo1(n):
    if n == 0 or n == 1:
        return n
    return fibo1(n - 1) + fibo1(n - 2)


# using memoization
# n = 5
# cache = [None] * (n + 1)
cache = {}


def fibo2(n):
    if n == 0 or n == 1:
        return n

    # if len(cache)!=None:
    #     return cache[n]

    if n in cache.keys():
        return cache[n]

    cache[n] = fibo2(n - 1) + fibo2(n - 2)
    return cache[n]


# using iteration
def fibo3(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a


print(fibo2(10))
