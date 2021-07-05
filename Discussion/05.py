from utils import tree, is_leave, branch, label


def closest_number(nums, target):
    """
    >>> closest_number([1, 4, 5, 6, 7], 2)
    1
    >>> closest_number([3, 1, 5, 6, 13], 4)
    3
    >>> closest_number([34, 102, 8, 5, 23], 25)
    23
    """
    return min(nums, key=lambda num: abs(num - target))


def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.

    >>> max_product([10, 3, 1, 9, 2])
    90
    >>> max_product([5, 10, 5, 10, 5])
    125
    >>> max_product([])
    1
    """
    return 1 if len(s) == 0 else s[0] if len(s) == 1 else max(
        max_product(s[1:]),
        s[0] * max_product(s[2:])
    )


def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs
    in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    length = len(s)
    for idx in range(length):
        if s[idx] == x:
            s.append(el)


def height(t):
    """ Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leave(t):
        return 0
    return max([height(c) for c in branch(t)] + [-1]) + 1


def max_path_sum(t):
    """Return the maximum path sum of the tree.

    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leave(t):
        return label(t)
    return label(t) + max([
        max_path_sum(b) for b in branch(t)
    ])


def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])]), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)
    """
    if label(tree) == x:
        return [x]
    for b in branch(tree):
        path = find_path(b, x)
        if path:
            return [label(tree)] + path