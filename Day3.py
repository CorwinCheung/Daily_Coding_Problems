class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Think about how you want to represent the tree, how are you going to be able to tell leaf nodes apart
# val NULL NULL, in our case
# use spaces to split and traverse in the deserializing

def serialize(node):
    def encode(node):
        if not node:
            ans.append("NULL")
            return
        if node.val:
            ans.append(node.val)
        encode(node.left)
        encode(node.right)
    ans = []
    encode(node)
    return " ".join(ans)

# cleaner to not use global variables
# Runs in O(N) with O(N) space


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
    print(serialize(node))
    print(deserialize(serialize(node)))
    assert deserialize(serialize(node)).left.left.val == 'left.left'


main()
