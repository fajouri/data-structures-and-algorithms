from dataclasses import dataclass
@dataclass
class Node:
    key: int
    left: object = None
    right: object = None
    height: int = 1

def h(node):
    return node.height if node else 0

def update(node):
    node.height = 1 + max(h(node.left), h(node.right))

def bf(node):
    return h(node.left) - h(node.right)

def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    update(y)
    update(x)
    return x

def rotate_left(x):
    # TODO: mirror rotate_right; preserve middle subtree
    raise NotImplementedError

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root
    update(root)
    # TODO: classify and repair LL, RR, LR, RL; return new root
    return root

def inorder(root):
    return inorder(root.left) + [root.key] + inorder(root.right) if root else []

def validate(root, lo=float('-inf'), hi=float('inf')):
    if root is None:
        return 0
    assert lo < root.key < hi, 'BST ordering'
    a = validate(root.left, lo, root.key)
    b = validate(root.right, root.key, hi)
    assert root.height == 1 + max(a,b), 'stale height'
    assert abs(a-b) <= 1, 'AVL balance'
    return root.height

def build(keys):
    root = None
    for key in keys:
        root = insert(root, key)
    return root

if __name__ == '__main__':
    y = Node(30, Node(20, Node(10)))
    update(y.left); update(y)
    root = rotate_right(y)
    assert inorder(root) == [10,20,30]
    assert validate(root) == 2
    print('Right rotation demo passed; student TODOs remain.')
