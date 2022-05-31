class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# for chars
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

# for numbers
# a = Node(5)
# b = Node(11)
# c = Node(3)
# d = Node(4)
# e = Node(15)
# f = Node(12)

# assign
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f


def depth_first_values(root):
    if root is None:
        return []
    values = []
    stack = [root]
    while stack:
        current = stack.pop()
        values.append(current.val)
        if current.left is not None:
            stack.append(current.left)
        if current.right is not None:
            stack.append(current.right)
    return values


def depth_first_values_rec(root):
    if root is None:
        return []
    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)
    return [root.val, *left_values, *right_values]


from collections import deque


def breadth_first_values(root):
    if root is None:
        return []
    values = []
    queue = deque([root])
    while queue:
        current = queue.popleft()
        values.append(current.val)
        if current.right:
            queue.append(current.right)
        if current.left:
            queue.append(current.left)
    return values


def tree_sum_rec(root):
    if root is None:
        return 0
    return root.val + tree_sum(root.left) + tree_sum(root.right)


def tree_sum_breadth_first(root):
    if root is None:
        return 0

    total_sum = 0
    queue = deque([root])
    while queue:
        current = queue.popleft()
        total_sum += current.val

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)
    return total_sum


def tree_sum_depth_first(root):
    if root is None:
        return []
    total_sum = 0
    stack = [root]
    while stack:
        current = stack.pop()
        total_sum += current.val
        if current.left is not None:
            stack.append(current.left)
        if current.right is not None:
            stack.append(current.right)
    return total_sum


def tree_includes_breadth_first(root, target):
    if root is None:
        return False

    queue = deque([root])
    while queue:
        current = queue.popleft()
        if current.val == target:
            return True

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return False


def tree_includes_rec(root, target):
    if root is None:
        return False

    if root.val == target:
        return True

    return tree_includes_rec(root.left, target) or tree_includes_rec(root.right, target)


def tree_min_value(root):
    if root is None:
        return None

    smallest = float("inf")
    stack = [root]

    while stack:
        current = stack.pop()
        if current.val < smallest:
            smallest = current.val

        if current.left is not None:
            stack.append(current.left)

        if current.right is not None:
            stack.append(current.right)

    return smallest


def tree_min_values_rec(root):
    if root is None:
        return float("inf")

    min_left = tree_min_values_rec(root.left)
    min_right = tree_min_values_rec(root.right)
    return min(root.val, min_left, min_right)


def max_path_sum(root):
    if root is None:
        return float("-inf")
    if root.left is None and root.right is None:
        return root.val

    max_left = max_path_sum(root.left)
    max_right = max_path_sum(root.right)

    return root.val + max(max_left, max_right)
