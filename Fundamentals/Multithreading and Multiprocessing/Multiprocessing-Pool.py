from multiprocessing import Pool


def func(n):
    return n * n


if __name__ == "__main__":
    p = Pool(processes=3)
    result = p.map(func, [1, 2, 3, 4, 5])
    for n in result:
        print(n)
