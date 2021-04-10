def keep_ints(cond, n):
    """
    >>> def is_even(x):
    ...    return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    for i in range(1, n + 1):
        if cond(i):
            print(i)


def make_keeper(n):
    """
    >>> def is_even(x):
    ...    return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def do_keep(cond):
        for i in range(1, n + 1):
            if cond(i):
                print(i)
    return do_keep


def make_keeper_redux(n):
    """
    >>> def multiple_of_4(x):
    ...    return x % 4 == 0
    >>> def ends_with_1(x):
    ...    return x % 10 == 1
    >>> k = make_keeper_redux(11)(multiple_of_4)
    4
    8
    >>> k = k(ends_with_1)
    1
    11
    """
    def do_keep(cond):
        for i in range(1, n + 1):
            if cond(i):
                print(i)
        return make_keeper_redux(n)
    return do_keep


def print_delayed(x):
    """
    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4
    """
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print


def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g = g("first")("second")("third")
    first
    done
    done
    """
    def inner_print(x):
        if n <= 0:
            print("done")
        else:
            print(x)
        return print_n(n - 1)
    return inner_print