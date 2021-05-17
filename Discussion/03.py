def merge(n1, n2):
    """
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge(21, 31)
    3211
    """
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    if n1 % 10 < n2 % 10:
        return 10 * merge(n1 // 10, n2) + n1 % 10
    return 10 * merge(n1, n2 // 10) + n2 % 10

def is_prime(n):
    """
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(n, k):
        if n == k:
            return True
        return n % k != 0 and helper(n , k + 1)
    return helper(n, 2)

def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    def helper(x, y, result):
        if y == 0:
            return result
        return helper(x, y - 1, result + x)
    return helper(m, n, 0)

def hailstone(n):
    """
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n != 1:
        if n % 2 == 0:
            return 1 + hailstone(n // 2)
        else:
            return 1 + hailstone(n * 3 + 1)
    else:
        return 1