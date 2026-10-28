from easy import Node, insert
from print_tree import display
def search_key(node: Node, key: int | float) -> bool:
    if not isinstance(key, (int, float)):
        print("the key should be a number (int or float)")
        return False
    
    if node is None:
        return False
    
    elif node.key == key:
        return True
    
    elif node.key <= key:
        return search_key(node.right, key)
    
    else: #node.key > key
        return search_key(node.left, key)
    

if __name__ == "__main__":
    root = None
    keys = [22, 33,54,2,3,45,3,6,3,1,93,45]
    print(f"Keys: {keys}")
    print("### Making BST ###")
    for i in range(len(keys)):
        root = insert(root, keys[i])
    display(root)

    print("-" * 30)
    print("result")
    print("-" * 30)
    target = 45
    print("")
    print(f"Is {target} in BST? The Answer: {search_key(root, target)}")