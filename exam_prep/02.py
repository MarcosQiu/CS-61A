def match_k(k):
    """
    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(211111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def match(n):
        prev = n % (10 ** k)
        while n > 0:
            if prev != n % (10 ** k):
                return False
            n = n // (10 ** k)
        return True
    return match

def chain_function():
    """
    >>> tester = chain_function()
    >>> x = tester(1)(2)(4)(5)
    3 1
    >>> x = x(2)
    6 2
    >>> x = x(8)
    3 3
    >>> x = x(3)(4)(5)
    9 4
    >>> x = x(9)
    6 5
    >>> x = x(10)
    >>> y = tester(4)(5)(8)
    6 1
    >>> y = y(2)(3)(10)
    9 2
    4 3
    """
    def g(x, y):
        def h(n):
            if n == x or x == 0:
                return g(n + 1, y)
            else:
                return print(x, y + 1) or g(n + 1, y + 1)
        return h
    return g(0, 0)

def cs61nay(combiner, n):
    """
    >>> f = cs61nay(lambda x, y: x * y, 3)
    >>> f(2)(3)(4)
    24
    >>> f(-1)(2)(3)
    -6
    >>> f = cs61nay(lambda x, y: x - y, 4)
    >>> f(1)(2)(-2)(-1)
    2
    >>> f = cs61nay(lambda x, y: x + y, 1)
    >>> f(61)
    61
    >>> f(2021)
    2021
    """
    if n == 1:
        return lambda x: x
    else:
        return lambda a: lambda b: cs61nay(combiner, n - 1)(combiner(a, b))

cs61NAY = lambda f, n: (n == 1 and (lambda x: x)) or (lambda a: lambda b: cs61NAY(f, n - 1)(f(a, b)))
cs61NAY.__name__ = "cs61NAY"
cs61NAY.__doc__ = """
    >>> f = cs61nay(lambda x, y: x * y, 3)
    >>> f(2)(3)(4)
    24
    >>> f(-1)(2)(3)
    -6
    >>> f = cs61nay(lambda x, y: x - y, 4)
    >>> f(1)(2)(-2)(-1)
    2
    >>> f = cs61nay(lambda x, y: x + y, 1)
    >>> f(61)
    61
    >>> f(2021)
    2021"""
