class Node_BST():
    def __init__(self, key) -> None:
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.key = key


class Tree_BST():
    def __init__(self) -> None:
        self.root = None

    def compare_key(self, node: Node_BST, parent: Node_BST):
        if node.key <= parent.key:  # if node == parent -> parent.left_child = node
            if parent.left_child is None:
                parent.left_child = node
                node.parent = parent
            else:
                parent = parent.left_child
                self.compare_key(node, parent)
        else:
            if parent.right_child is None:
                parent.right_child = node
                node.parent = parent
            else:
                parent = parent.right_child
                self.compare_key(node, parent)

    def insert(self, key):
        node = Node_BST(key)
        parent = self.root

        if parent is not None:
            self.compare_key(node, parent)
        else:
            self.root = node
            node.parent = parent
