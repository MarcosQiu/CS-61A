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