class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # A tree is unival if it is a leaf
    # A tree is unival if its left and right subtrees are unival


def isUnival(Node):
    if not Node:
        return False
    if Node.left and Node.left.value != Node.value or Node.right and Node.right.value != Node.value:
        return False
    if not Node.left and not Node.right:
        return True
    return isUnival(Node.left) and isUnival(Node.right)

# Check if Unival, use the properties that it is unival if leaf and if left and right subtrees
# are unival. Also check to make sure that the left and right values are equal to the node value to
# keep the recursing going


def unival(Node):
    count = 0

    def recurse(Node):
        nonlocal count
        if isUnival(Node):
            count += 1
        if Node.left:
            recurse(Node.left)
        if Node.right:
            recurse(Node.right)
    recurse(Node)
    return count

# call isUnival on all the nodes, recurse through the tree.


def main():
    root = Node(0)
    root.left = Node(1)
    root.right = Node(0)
    root.right.right = Node(0)
    root.right.left = Node(1)
    root.right.left.left = Node(1)
    root.right.left.right = Node(1)

    print(unival(root))


main()
