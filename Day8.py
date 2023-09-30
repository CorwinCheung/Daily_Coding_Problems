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
# This solution unfortunately runs in O(N^2) time complexity because
# For each of the nodes it will be checking the whole subtree


def efficient_helper(Node):
    if Node is None:
        return 0, True
    left_count, is_left_unival = efficient_helper(Node.left)
    right_count, is_right_unival = efficient_helper(Node.right)
    total = right_count + left_count

    if is_left_unival and is_right_unival:
        if Node.left != None and Node.left.value != Node.value:
            return total, False
        if Node.right != None and Node.right.value != Node.value:
            return total, False
        return total + 1, True

    return total, False


def efficient_unival(Node):
    count, _ = efficient_helper(Node)
    return count

# therefore to solve this problem efficiently, we will need to maintain a count
# parameter to pass through so we can evaluate the number of univals in a tree in one pass
#This is an O(n) solution


def main():
    root = Node(0)
    root.left = Node(1)
    root.right = Node(0)
    root.right.right = Node(0)
    root.right.left = Node(1)
    root.right.left.left = Node(1)
    root.right.left.right = Node(1)

    print(unival(root))
    print(efficient_unival(root))


main()
