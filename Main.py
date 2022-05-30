class Node():
    def __init__(self, parent, left, right, value):
        self.parent = parent
        self.left = left
        self.right = right
        self.value = value
    def set_left(self):
        self.left = left
    def set_right(self):
        self.right = right
    def set_value(self, value):
        self.value = value


head = Node(None, None, None, 1)
left = Node(head, None, None, 2)
right = Node(head, None, None, 3)
left1 = Node(left, None, None, 4)
right1 = Node(left, None, None, 5)

head.set_left(left)
head.set_right(right)
left.set_left(left1)
left.set_right(right1)


