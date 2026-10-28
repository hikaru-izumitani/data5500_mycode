"""
After I wrote hard_pre.py by myself, I asked chatGPT because I was confused and pondered which node I should delete.

ChatGPT URL
https://chatgpt.com/share/6ae207a7-fcac-83e8-9c2b-ae35e6286d57

"""

from easy import Node, insert
from medium import search_key
from print_tree import display

AFTER_DELETION = "After deletion"

def delete_all(node: Node, key: int | float) -> (Node | None):
    """Remove a node completely, ignoring its counter."""
    if node is None:
        return None

    if key < node.key:
        node.left = delete_all(node.left, key)

    elif key > node.key:
        node.right = delete_all(node.right, key)

    else:
        # The successor has no left child
        if node.left is None:
            return node.right

        if node.right is None:
            return node.left

    return node


def delete_node(root: Node, key: int | float) -> (Node | None):
    if not isinstance(key, (int, float)):
        raise TypeError("the key should be a number (int or float)")

    if root is None:
        return None

    if key < root.key:
        root.left = delete_node(root.left, key)

    elif key > root.key:
        root.right = delete_node(root.right, key)

    else:
        # Handle duplicate keys
        if root.counter > 1:
            root.counter -= 1
            return root

        # Case 1: No children
        if root.left is None and root.right is None:
            return None

        # Case 2: One child
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        # Case 3: Two children
        successor = root.right

        while successor.left is not None:
            successor = successor.left

        root.key = successor.key
        root.counter = successor.counter

        # Remove the successor completely
        root.right = delete_all(root.right, successor.key)

    return root


if __name__ == "__main__":
    root = None

    keys = [22, 33, 54, 2, 3, 45, 3, 6, 3, 1, 93, 45, 101, 77]
    print("### Making BST ###")
    for i in range(len(keys)):
        root = insert(root, keys[i])
    display(root)

    target = 6

    print("-" * 30)
    print("Before deletion")
    print("-" * 30)
    print(f"Keys: {keys}")
    print(f"Is {target} in BST? The Answer: {search_key(root, target)}")
    print("")
    print("#" * 30)

    print("### [Case 1] Delete a Node, which has no child ###")
    print("#" * 30)
    # IMPORTANT: save the returned root
    root = delete_node(root, target)
    print(f"{target} is deleted")

    print()
    print("-" * 30)
    print(AFTER_DELETION)
    print("-" * 30)
    display(root)
    print(f"Is {target} in BST? The Answer: {search_key(root, target)}")

    target = 33
    print("### [Case 2] Delete a Node, which has a child ###")
    print("#" * 30)
    # IMPORTANT: save the returned root
    root = delete_node(root, target)
    print(f"{target} is deleted")

    print()
    print("-" * 30)
    print(AFTER_DELETION)
    print("-" * 30)
    display(root)
    print(f"Is {target} in BST? The Answer: {search_key(root, target)}")

    target = 54
    print("### [Case 3] Delete a Node, which has two children ###")
    print("#" * 30)
    # IMPORTANT: save the returned root
    root = delete_node(root, target)
    print(f"{target} is deleted")

    print()
    print("-" * 30)
    print(AFTER_DELETION)
    print("-" * 30)
    display(root)
    print(f"Is {target} in BST? The Answer: {search_key(root, target)}")
