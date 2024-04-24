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

    def ll_rot(self, y, z):
        a = z.left_child
        b = z.right_child
        c = y.right_child
        p = y.parent

        if p is not None:
            if p.left_child is y:
                p.left_child = z
            else:
                p.right_child = z
        else:
            self.root = z
        z.parent = p

        z.left_child = a
        if a is not None:
            a.parent = z
        z.right_child = y
        if y is not None:
            y.parent = z
        y.left_child = b
        if b is not None:
            b.parent = y
        y.right_child = c
        if c is not None:
            c.parent = y

        z.bf = 0
        y.bf = 0

    def rr_rot(self, y, z):
        a = z.left_child
        p = y.parent

        if p is not None:
            if p.left_child is y:
                p.left_child = z
            else:
                p.right_child = z
        else:
            self.root = z
        z.parent = p

        z.left_child = y
        if y is not None:
            y.parent = z
        y.right_child = a
        if a is not None:
            a.parent = y

        z.bf = 0
        y.bf = 0

    def lr_rot(self, y, z, t):
        b = t.left_child
        c = t.right_child
        p = y.parent

        if p is not None:
            if p.left_child is y:
                p.left_child = t
            else:
                p.right_child = t
        else:
            self.root = t
        t.parent = p

        t.left_child = z
        if z is not None:
            z.parent = t
        z.right_child = b
        if b is not None:
            b.parent = z
        t.right_child = y
        if y is not None:
            y.parent = t
        y.left_child = c
        if c is not None:
            c.parent = y

        if t.bf == -1:
            z.bf = 1
            y.bf = 0
        elif t.bf == 1:
            z.bf = 0
            y.bf = -1
        else:
            z.bf = 0
            y.bf = 0
        t.bf = 0

    def rl_rot(self, y, z, t):
        b = t.left_child
        c = t.right_child
        p = y.parent

        if p is not None:
            if p.left_child is y:
                p.left_child = t
            else:
                p.right_child = t
        else:
            self.root = t
        t.parent = p

        t.left_child = y
        if y is not None:
            y.parent = t
        y.right_child = b
        if b is not None:
            b.parent = y
        t.right_child = z
        if z is not None:
            z.parent = t
        z.left_child = c
        if c is not None:
            c.parent = z

        if t.bf == -1:
            z.bf = 0
            y.bf = 1
        elif t.bf == 1:
            z.bf = -1
            y.bf = 0
        else:
            z.bf = 0
            y.bf = 0
        t.bf = 0

    def update_parent_bf(self, parent, child_node):
        prev_bf = parent.bf
        if parent.left_child is child_node:
            parent.bf += 1
        elif parent.right_child is child_node:
            parent.bf -= 1
        has_height_changed = abs(parent.bf) > abs(prev_bf)

        has_rotated = False
        if (parent.bf == 2 and child_node.bf == 1):
            has_rotated = True
            self.ll_rot(parent, child_node)
        elif (parent.bf == -2 and child_node.bf == -1):
            has_rotated = True
            self.rr_rot(parent, child_node)
        elif (parent.bf == 2 and child_node.bf == -1):
            has_rotated = True
            self.lr_rot(parent, child_node, child_node.right_child)
        elif (parent.bf == -2 and child_node.bf == 1):
            has_rotated = True
            self.rl_rot(parent, child_node, child_node.left_child)

        if (parent.parent is not None and has_height_changed
           and not has_rotated):
            self.update_parent_bf(parent.parent, parent)

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
                    self.update_parent_bf(curr_node, new_node)
                    break
            else:
                if curr_node.right_child is not None:
                    curr_node = curr_node.right_child
                else:
                    new_node = AVLNode(value, curr_node)
                    curr_node.right_child = new_node
                    self.update_parent_bf(curr_node, new_node)
                    break

    def inorder(self, node, show_bf=False, depth=0):
        if node:
            self.inorder(node.right_child, show_bf, depth + 1)
            if not show_bf:
                print("  " * depth + str(node.value))
            else:
                print("  " * depth + str(node.value) + "," + str(node.bf))
            self.inorder(node.left_child, show_bf, depth + 1)

    def show_tree(self, show_bf=False):
        self.inorder(self.root, show_bf, 0)


if __name__ == "__main__":
    tree = AVLTree()
    while True:
        x = int(input("Wartość: "))
        tree.insert(x)
        print("Drzewo: ")
        tree.show_tree(show_bf=True)