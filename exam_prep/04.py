from utils import tree, is_leave, branch, label


def sum_tree(t):
    """
    Add all elements in a tree.

    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    if t is None:
        return 0
    return label(t) + sum([sum_tree(b) for b in branch(t)])


def balanced(t):
    """
    Checks if each branch has same sum of all elements,
    and each branch is balanced.

    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(t, [t, tree(1)])
    >>> balanced(t)
    False
    """
    if is_leave(t):
        return True
    sums = [sum_tree(b) for b in branch(t)]
    # if all children don't have equal sum, then just return False
    for i in range(len(sums) - 1):
        if sums[i] != sums[i + 1]:
            return False

    # Check each branch by itself is balanced
    for b in branch(t):
        if not balanced(b):
            return False

    return True


def prune_tree(t, predicate):
    """
    Returns a new tree where any branch that has the predicate of the label
    of the branch returns True has its branches pruned.

    >>> sum_tree(prune_tree(test_tree, lambda x: x > 10))
    45
    >>> prune_tree(test_tree, lambda x: x > 10) == test_tree
    True
    """
    if is_leave(t) or predicate(label(t)):
        return tree(label(t))
    return tree(label(t), [prune_tree(b, predicate) for b in branch(t)])


test_tree = tree(
    1,
    [
        tree(
            2,
            [
                tree(
                    4,
                    [
                        tree(8),
                        tree(9)
                    ]
                ),
                tree(5)
            ]
        ),
        tree(
            3,
            [
                tree(6),
                tree(7)
            ]
        )
    ]
)


def closest(t):
    """
    Return the smallest difference between an entry and the sum of the
    root entries of its branches.

    >>> t = tree(8, [tree(4), tree(3)])
    >>> closest(t)
    1
    >>> closest(tree(5, [t]))
    1
    >>> closest(tree(10, [tree(2), t]))
    0
    >>> closest(tree(3))
    3
    >>> closest(tree(8, [tree(3, [tree(1, [tree(5)])])]))
    2
    >>> sum([])
    0
    """
    diff = abs(label(t) - sum([label(b) for b in branch(t)]))
    return min([diff].extend([closest(b) for b in branch(t)]))

