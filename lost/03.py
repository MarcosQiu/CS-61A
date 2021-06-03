def multiadder(n):
    """
    >>> f = multiadder(3)
    >>> f(5)(6)(7)
    18
    >>> multiadder(1)(5)
    5
    >>> multiadder(2)(5)(6)
    11
    >>> multiadder(4)(5)(6)(7)(8)
    26
    """
    assert n > 0
    if n == 1:
        return lambda x: x
    else:
        return lambda x: lambda y: multiadder(n - 1)(x + y)
        