# simple strategy

factorial_memo = {}


def factorial(k):

    if k < 2:
        return 1

    if not k in factorial_memo:
        factorial_memo[k] = k * factorial(k - 1)

    return factorial_memo[k]


# making a class
class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]


def factorial(k):
    if k < 2:
        return 1
    return k * factorial(k - 1)


factorial = Memoize(factorial)
