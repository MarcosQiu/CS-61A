class tree:
    def __init__(self, val, branches = []):
        self.val = val
        self.branches = branches


def is_leave(t):
    return len(branch(t)) == 0


def branch(t):
    return t.branches


def label(t):
    return t.val