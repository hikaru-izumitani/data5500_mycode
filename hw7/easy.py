from print_tree import display

class Node:
    def __init__(self, key: int | float):
        self.key = key
        self.left = None
        self.right = None
        self.counter = 1
    
def insert(node: Node, key: int | float) -> Node:
    if not isinstance(key, (int,float)):
        print("the key should be a number (int or float)")
        return node
    if node is None:
        return Node(key)
    if node.key == key:
        node.counter += 1
    elif node.key < key:
        node.right = insert(node.right, key)
    else: # node.key > key
        node.left = insert(node.left, key)
    return node


if __name__ == "__main__":
    root = None
    keys = [22,35,38,29,19]
    for i in range(len(keys)):
        root = insert(root, keys[i])
    display(root)