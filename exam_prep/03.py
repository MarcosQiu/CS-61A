def is_palindrome(s):
    """
    >>> is_palindrome("tenet")
    True
    >>> is_palindrome("tenets")
    False
    >>> is_palindrome("raincar")
    False
    >>> is_palindrome("")
    True
    >>> is_palindrome("a")
    True
    >>> is_palindrome("ab")
    False
    """
    if len(s) < 2:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

def greatest_pal(s):
    """
    >>> greatest_pal("tenet")
    'tenet'
    >>> greatest_pal("tenets")
    'tenet'
    >>> greatest_pal("stennet")
    'tennet'
    >>> greatest_pal("25 racecars")
    'racecar'
    >>> greatest_pal("abc")
    'a'
    >>> greatest_pal("")
    ''
    """
    if is_palindrome(s):
        return s
    left, right = greatest_pal(s[1:]), greatest_pal(s[:-1])
    if len(left) > len(right):
        return left
    return right

def greatest_pal_2(s):
    """
    >>> greatest_pal_2("tenet")
    'tenet'
    >>> greatest_pal_2("tenets")
    'tenet'
    >>> greatest_pal_2("stennet")
    'tennet'
    >>> greatest_pal_2("25 racecars")
    'racecar'
    >>> greatest_pal_2("abc")
    'a'
    >>> greatest_pal_2("")
    ''
    """
    def helper(a, b, c):
        if a > len(s):
            return c
        elif a + b > len(s):
            return helper(a + 1, 0, c)
        elif a > len(c) and is_palindrome(s[b:b + a]):
            c = s[b:b + a]
        return helper(a, b + 1, c)
    return helper(1, 0, "")

def greatest_pal_3(s):
    """
    >>> greatest_pal_3("tenet")
    'tenet'
    >>> greatest_pal_3("tenets")
    'tenet'
    >>> greatest_pal_3("stennet")
    'tennet'
    >>> greatest_pal_3("25 racecars")
    'racecar'
    >>> greatest_pal_3("abc")
    'a'
    >>> greatest_pal_3("")
    ''
    """
    def helper(a, b):
        if a + b > len(s):
            return helper(a - 1, 0)
        elif is_palindrome(s[b:b + a]):
            return s[b:b + a]
        return helper(a, b + 1)
    return helper(len(s), 0)

def greatest_pal_4(s):
    """
    >>> greatest_pal_4("tenet")
    'tenet'
    >>> greatest_pal_4("tenets")
    'tenet'
    >>> greatest_pal_4("stennet")
    'tennet'
    >>> greatest_pal_4("25 racecars")
    'racecar'
    >>> greatest_pal_4("abc")
    'a'
    >>> greatest_pal_4("")
    ''
    """
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return max(greatest_pal_4(s[:-1]), greatest_pal_4(s[1:]), key=len)
    return s