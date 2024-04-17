class AVLNode:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left_child = None
        self.right_child = None
        self.bf = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def right_rotation(self, node):
        parent = node.parent
        child = node.right_child
        child2 = child.left_child
        if child2 is None:
            child2 = child.right_child

        node.parent = child
        child.left_child = node
        child.right_child = child2
        child.parent = parent
        node.right_child = None

        if parent is not None:
            if node is parent.left_child:
                parent.left_child = child
            else:
                parent.right_child = child
        else:
            self.root = child

        child2.bf = 0
        if node.left_child is not None:
            node.bf = -1
            child.bf = -1
        else:
            node.bf = 0
            child.bf = 0

    def left_rotation(self, node):
        parent = node.parent
        child = node.left_child
        child2 = child.left_child
        if child2 is None:
            child2 = child.right_child

        node.parent = child
        child.right_child = node
        child.left_child = child2
        child.parent = parent
        node.left_child = None

        if parent is not None:
            if node is parent.left_child:
                parent.left_child = child
            else:
                parent.right_child = child
        else:
            self.root = child

        child2.bf = 0
        if node.right_child is not None:
            node.bf = 1
            child.bf = 1
        else:
            node.bf = 0
            child.bf = 0

    def balance(self, node):
        if (node.bf > 1):
            self.right_rotation(node)
        elif (node.bf < -1):
            self.left_rotation(node)

    def update_parent_bf(self, parent, child_node):
        if parent.left_child is child_node:
            parent.bf -= 1
        elif parent.right_child is child_node:
            parent.bf += 1

        if (parent.bf < -1 or parent.bf > 1):
            self.balance(parent)

    def search(self, value):
        curr_node = self.root
        while curr_node is not None:
            if value == curr_node.value:
                return curr_node
            elif value < curr_node.value:
                curr_node = curr_node.left_child
            else:
                curr_node = curr_node.right_child
        return curr_node

    def insert(self, value):
        if self.root is None:
            new_node = AVLNode(value, None)
            self.root = new_node
            return
        curr_node = self.root
        while True:
            if value <= curr_node.value:
                if curr_node.left_child is not None:
                    curr_node = curr_node.left_child
                else:
                    new_node = AVLNode(value, curr_node)
                    curr_node.left_child = new_node
                    curr_node.bf -= 1
                    if (curr_node.bf == -1 and curr_node.parent is not None):
                        self.update_parent_bf(curr_node.parent, curr_node)
                    break
            else:
                if curr_node.right_child is not None:
                    curr_node = curr_node.right_child
                else:
                    new_node = AVLNode(value, curr_node)
                    curr_node.right_child = new_node
                    curr_node.bf += 1
                    if (curr_node.bf == 1 and curr_node.parent is not None):
                        self.update_parent_bf(curr_node.parent, curr_node)
                    break
