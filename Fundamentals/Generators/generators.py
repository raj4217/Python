def sqr(num):
    for i in num:
        yield i * i


# res = sqr([1, 2, 3, 4, 5])

# print(res)
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))

res = (x*x for x in [1,2,3,4,5] )

for n in res:
    print(next(res))
