from utils import tree, label, branch, is_leave


def primary_stress(t):
    """
    Returns a STRING corresponding to the stressed part of the word represented by the input tree.
    >>> word = tree("", [tree("w", [tree("s", [tree("min")]), tree("w", [tree("ne")])]), tree("s", [tree("s", [tree("so")]), tree("w", [tree("ta")])])])
    >>> primary_stress(word)
    'so'
    >>> phrase = tree("", [tree("s", [tree("s", [tree("law")]), tree("w", [tree("degree")])]), tree("w", [tree("requirement")])])
    >>> primary_stress(phrase)
    'law'
    """
    def helper(t, num_s):
        if is_leave(t):
            return [label(t), num_s]
        if label(t) == 's':
            num_s += 1
        return max([helper(b, num_s) for b in branch(t)], key=lambda x:x[1])
    return helper(t, 0)[0]


def siblings(t):
    """Return a list of the labels of all nodes that have siblings in t.

    >>> a = tree(4, [tree(5), tree(6), tree(7, [tree(8)])])
    >>> siblings(tree(1, [tree(3, [a]), tree(9, [tree(10)])]))
    [3, 9, 5, 6, 7]
    """
    result = [label(b) for b in branch(t) if len(branch(t)) > 1]
    for b in branch(t):
        result.extend(siblings(b))
    return result