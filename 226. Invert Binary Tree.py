class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(node):
    result = []

    if node:
        result.append(node.val)
        result += preorder(node.left)
        result += preorder(node.right)
    return result


def invert(root):
    if not root:
        return root
    temp_left = root.left
    root.left = invert(root.right)
    root.right = invert(temp_left)
    return root

def main():
    Tree = TreeNode(4)
    Tree.left = TreeNode(2)
    Tree.left.left = TreeNode(1)
    Tree.left.right = TreeNode(3)
    Tree.right = TreeNode(7)
    Tree.right.left = TreeNode(6)
    Tree.right.right = TreeNode(9)
    print(preorder(Tree))
    print(preorder(invert(Tree)))


main()