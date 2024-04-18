class AVLNode:
    def __init__(self, key, parent=None):
        self.key = key
        self.left_child = None
        self.right_child = None
        self.parent = parent
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left_child) - self.height(node.right_child)

    def rotate_right(self, y):
        x = y.left_child
        T2 = x.right_child

        x.right_child = y
        y.left_child = T2

        y.height = 1 + max(self.height(y.left_child),
                           self.height(y.right_child))
        x.height = 1 + max(self.height(x.left_child),
                           self.height(x.right_child))

        return x

    def rotate_left(self, x):
        y = x.right_child
        T2 = y.left_child

        y.left_child = x
        x.right_child = T2

        x.height = 1 + max(self.height(x.left_child),
                           self.height(x.right_child))
        y.height = 1 + max(self.height(y.left_child),
                           self.height(y.right_child))

        return y

    def insert(self, key):
        self.root = self._insert(self.root, None, key)

    def _insert(self, root, parent, key):
        if not root:
            return AVLNode(key, parent)

        if key < root.key:
            root.left_child = self._insert(root.left_child, root, key)
        else:
            root.right_child = self._insert(root.right_child, root, key)

        root.height = 1 + max(self.height(root.left_child),
                              self.height(root.right_child))

        balance = self.balance(root)

        # Left Left
        if balance > 1 and key < root.left_child.key:
            return self.rotate_right(root)

        # Right Right
        if balance < -1 and key > root.right_child.key:
            return self.rotate_left(root)

        # Left Right
        if balance > 1 and key > root.left_child.key:
            root.left_child = self.rotate_left(root.left_child)
            return self.rotate_right(root)

        # Right Left
        if balance < -1 and key < root.right_child.key:
            root.right_child = self.rotate_right(root.right_child)
            return self.rotate_left(root)

        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if not root or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left_child, key)
        return self._search(root.right_child, key)

    def inorder(self, node, depth=0):
        if node:
            self.inorder(node.right_child, depth + 1)
            print("  " * depth + str(node.key))
            self.inorder(node.left_child, depth + 1)

    def show_tree(self):
        self.inorder(self.root)


if __name__ == "__main__":
    avl_tree = AVLTree()
    keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    for key in keys:
        avl_tree.insert(key)

    print("\nAVL Tree:")
    avl_tree.show_tree()
