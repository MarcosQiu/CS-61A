def is_prime(n):
    """
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def order_digits(x):
    """
    >>> order_digits(5)
    True
    >>> order_digits(11)
    True
    >>> order_digits(123)
    True
    >>> order_digits(1357)
    True
    >>> order_digits(21)
    False
    >>> result = order_digits(1375)
    >>> result
    False
    """
    def helper(num, prev):
        if num < 10:
            return num <= prev
        num, remain = num // 10, num % 10
        if remain > prev:
            return False
        return helper(num, remain)
    return helper(x, 10)


def rect(area, perimeter):
    """
    >>> rect(10, 14)
    5
    >>> rect(5, 12)
    5
    >>> rect(25, 20)
    5
    >>> rect(25, 25)
    False
    >>> rect(25, 29)
    False
    >>> rect(100, 50)
    20
    """
    side = 1
    while side * side <= area:
        other = round(perimeter // 2 - side)
        if side * other == area and (side + other) * 2 == perimeter:
            return other
        side = side + 1
    return False