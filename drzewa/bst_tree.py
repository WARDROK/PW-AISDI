class Node_BST():
    def __init__(self, key) -> None:
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.key = key


class Tree_BST():
    def __init__(self) -> None:
        self.root = None

    def compare_key(self, node: Node_BST, parent: Node_BST) -> None:
        # if node == parent -> parent.left_child = node
        if node.key <= parent.key:
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

    def insert(self, key) -> None:
        node = Node_BST(key)
        parent = self.root

        if parent is not None:
            self.compare_key(node, parent)
        else:
            self.root = node
            node.parent = parent

    def find(self, key) -> Node_BST:  # first node from top
        node = self.root
        if not node:
            return None
        while node.key != key:
            if key < node.key:
                node = node.left_child
            else:
                node = node.right_child
            if not node:
                return None
        return node

    def min_BST(self, root: Node_BST) -> Node_BST:
        node = root
        if not node:
            return node
        while node.left_child:
            node = node.left_child
        return node

    def max_BST(self, root: Node_BST) -> Node_BST:
        node = root
        if not node:
            return node
        while node.right_child:
            node = node.right_child
        return node

    def succesor_BST(self, node: Node_BST) -> Node_BST:
        if not node:
            return node
        if node.right_child:
            return self.min_BST(node.right_child)
        succesor = node.parent
        while succesor and node == succesor.right_child:
            node = succesor
            succesor = succesor.parent
        return succesor

    def delete_node(self, key):
        node = self.find(key)
        if not node:
            return "Not node with this key"

        if not node.left_child or not node.right_child:
            succesor = node
        else:
            succesor = self.succesor_BST(node)

        if succesor.left_child:
            child = succesor.left_child
        else:
            child = succesor.right_child

        if child:
            child.parent = succesor.parent

        if succesor.parent:
            if succesor == succesor.parent.left_child:
                succesor.parent.left_child = child
            else:
                succesor.parent.right_child = child
        else:
            self.root = node

        node.key = succesor.key
        succesor = None
