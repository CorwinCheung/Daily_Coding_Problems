class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


total_string = ""


def serialize(node):
    global total_string
    if not node:
        total_string += "NULL "
        return
    if node.val:
        total_string += node.val + " "

    serialize(node.left)
    serialize(node.right)
    return total_string


def deserialize(string):
    def traverse(items):
        val = items.pop(0)
        if val == "NULL":
            return
        node = Node(val)
        node.left = traverse(items)
        node.right = traverse(items)
        return node
    return traverse(string.split())


def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    serialize(node)
    print(total_string)
    assert deserialize(serialize(node)).left.left.val == 'left.left'


main()
