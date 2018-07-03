'''
Decorators allows us to wrap a function in another function
most common uses of decorators are logging, timing


Below eg is for timing
'''
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'{func.__name__} took {(time.time()-start)*1000} milli-seconds')
        return result
    return wrapper


@timeit
def square(num):
    result = []
    for n in num:
        result.append(n * 2)
    return result


@timeit
def cube(num):
    result = []
    for n in num:
        result.append(n ** 3)
    return result


array = range(1, 1000000)

out_sq = square(array)
out_cu = cube(array)
