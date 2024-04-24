from .avl_tree import AVLTree


def is_leaf(node):
    return node.left_child is None and node.right_child is None


def test_insert_and_search():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(7)
    assert tree.search(2).key == 2
    assert tree.search(2).parent.key == 5
    assert tree.search(5).parent is None


def test_search_not_in_tree():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(7)
    assert tree.search(6) is None
    assert tree.search(0) is None
    assert tree.search(-1) is None


def test_tree_balance_left_left():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(1)
    assert tree.root.value == 2
    assert tree.root.left_child.value == 1
    assert tree.root.right_child.value == 5
    assert tree.root.left_child.left_child is None
    assert tree.root.left_child.right_child is None
    assert tree.root.right_child.left_child is None
    assert tree.root.right_child.right_child is None

    assert tree.balance(tree.root) == 0
    assert tree.balance(tree.root.left_child) == 0
    assert tree.balance(tree.root.right_child) == 0


def test_tree_balance_left_left_big():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(6)
    tree.insert(2)
    tree.insert(4)
    tree.insert(1)

    assert tree.root.value == 3
    assert tree.root.left_child.value == 2
    assert tree.root.left_child.right_child is None
    assert tree.root.left_child.left_child.value == 1
    assert is_leaf(tree.root.left_child.left_child)
    assert tree.root.right_child.value == 5
    assert tree.root.right_child.left_child.value == 4
    assert is_leaf(tree.root.right_child.left_child)
    assert tree.root.right_child.right_child.value == 6
    assert is_leaf(tree.root.right_child.right_child)

    assert tree.root.bf == 0
    assert tree.root.left_child.bf == 1
    assert tree.root.left_child.left_child.bf == 0
    assert tree.root.right_child.bf == 0
    assert tree.root.right_child.left_child.bf == 0
    assert tree.root.right_child.right_child.bf == 0


def test_tree_balance_left_right():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(3)
    assert tree.root.value == 3
    assert tree.root.left_child.value == 2
    assert tree.root.right_child.value == 5
    assert tree.root.left_child.left_child is None
    assert tree.root.left_child.right_child is None
    assert tree.root.right_child.left_child is None
    assert tree.root.right_child.right_child is None

    assert tree.balance(tree.root) == 0
    assert tree.balance(tree.root.left_child) == 0
    assert tree.balance(tree.root.right_child) == 0


def test_tree_balance_left_right_big():
    tree = AVLTree()
    tree.insert(9)
    tree.insert(10)
    tree.insert(5)
    tree.insert(4)
    tree.insert(7)
    tree.insert(6)
    tree.insert(8)

    assert tree.root.value == 7
    assert tree.root.left_child.value == 5
    assert tree.root.left_child.left_child.value == 4
    assert tree.root.left_child.right_child.value == 6
    assert is_leaf(tree.root.left_child.left_child)
    assert is_leaf(tree.root.left_child.right_child)
    assert tree.root.right_child.value == 9
    assert tree.root.right_child.left_child.value == 8
    assert tree.root.right_child.right_child.value == 10
    assert is_leaf(tree.root.right_child.left_child)
    assert is_leaf(tree.root.right_child.right_child)

    assert tree.root.bf == 0
    assert tree.root.left_child.bf == 0
    assert tree.root.left_child.left_child.bf == 0
    assert tree.root.left_child.right_child.bf == 0
    assert tree.root.right_child.bf == 0
    assert tree.root.right_child.left_child.bf == 0
    assert tree.root.right_child.right_child.bf == 0


def test_tree_balance_left_right_big_reverse_last_inserts():
    tree = AVLTree()
    tree.insert(9)
    tree.insert(10)
    tree.insert(5)
    tree.insert(4)
    tree.insert(7)
    tree.insert(8)
    tree.insert(6)

    assert tree.root.value == 7
    assert tree.root.left_child.value == 5
    assert tree.root.left_child.left_child.value == 4
    assert tree.root.left_child.right_child.value == 6
    assert is_leaf(tree.root.left_child.left_child)
    assert is_leaf(tree.root.left_child.right_child)
    assert tree.root.right_child.value == 9
    assert tree.root.right_child.left_child.value == 8
    assert tree.root.right_child.right_child.value == 10
    assert is_leaf(tree.root.right_child.left_child)
    assert is_leaf(tree.root.right_child.right_child)

    assert tree.root.bf == 0
    assert tree.root.left_child.bf == 0
    assert tree.root.left_child.left_child.bf == 0
    assert tree.root.left_child.right_child.bf == 0
    assert tree.root.right_child.bf == 0
    assert tree.root.right_child.left_child.bf == 0
    assert tree.root.right_child.right_child.bf == 0


def test_tree_balance_right_right():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    assert tree.root.value == 6
    assert tree.root.left_child.value == 5
    assert tree.root.right_child.value == 7
    assert tree.root.left_child.left_child is None
    assert tree.root.left_child.right_child is None
    assert tree.root.right_child.left_child is None
    assert tree.root.right_child.right_child is None

    assert tree.balance(tree.root) == 0
    assert tree.balance(tree.root.left_child) == 0
    assert tree.balance(tree.root.right_child) == 0


def test_tree_balance_right_right_big():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(4)
    tree.insert(8)
    tree.insert(6)
    tree.insert(9)
    tree.insert(10)

    assert tree.root.value == 8
    assert tree.root.left_child.value == 5
    assert tree.root.left_child.left_child.value == 4
    assert tree.root.left_child.right_child.value == 6
    assert is_leaf(tree.root.left_child.left_child)
    assert is_leaf(tree.root.left_child.right_child)
    assert tree.root.right_child.value == 9
    assert tree.root.right_child.left_child is None
    assert tree.root.right_child.right_child.value == 10
    assert is_leaf(tree.root.right_child.right_child)

    assert tree.root.bf == 0
    assert tree.root.left_child.bf == 0
    assert tree.root.left_child.left_child.bf == 0
    assert tree.root.left_child.right_child.bf == 0
    assert tree.root.right_child.bf == -1
    assert tree.root.right_child.right_child.bf == 0


def test_tree_balance_right_left():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(7)
    tree.insert(6)
    assert tree.root.value == 6
    assert tree.root.left_child.value == 5
    assert tree.root.right_child.value == 7
    assert tree.root.left_child.left_child is None
    assert tree.root.left_child.right_child is None
    assert tree.root.right_child.left_child is None
    assert tree.root.right_child.right_child is None

    assert tree.root.bf == 0
    assert tree.root.left_child.bf == 0
    assert tree.root.right_child.bf == 0


def test_tree_balance_right_left_big():
    tree = AVLTree()
    tree.insert(2)
    tree.insert(1)
    tree.insert(6)
    tree.insert(7)
    tree.insert(4)
    tree.insert(3)
    tree.insert(5)

    assert tree.root.value == 4
    assert tree.root.left_child.value == 2
    assert tree.root.left_child.left_child.value == 1
    assert tree.root.left_child.right_child.value == 3
    assert is_leaf(tree.root.left_child.left_child)
    assert is_leaf(tree.root.left_child.right_child)
    assert tree.root.right_child.value == 6
    assert tree.root.right_child.left_child.value == 5
    assert tree.root.right_child.right_child.value == 7
    assert is_leaf(tree.root.right_child.left_child)
    assert is_leaf(tree.root.right_child.right_child)

    assert tree.root.bf == 0
    assert tree.root.left_child.bf == 0
    assert tree.root.left_child.left_child.bf == 0
    assert tree.root.left_child.right_child.bf == 0
    assert tree.root.right_child.bf == 0
    assert tree.root.right_child.left_child.bf == 0
    assert tree.root.right_child.right_child.bf == 0


def test_tree_balance_right_left_big_reverse_last_inserts():
    tree = AVLTree()
    tree.insert(2)
    tree.insert(1)
    tree.insert(6)
    tree.insert(7)
    tree.insert(4)
    tree.insert(5)
    tree.insert(3)

    assert tree.root.value == 4
    assert tree.root.left_child.value == 2
    assert tree.root.left_child.left_child.value == 1
    assert tree.root.left_child.right_child.value == 3
    assert is_leaf(tree.root.left_child.left_child)
    assert is_leaf(tree.root.left_child.right_child)
    assert tree.root.right_child.value == 6
    assert tree.root.right_child.left_child.value == 5
    assert tree.root.right_child.right_child.value == 7
    assert is_leaf(tree.root.right_child.left_child)
    assert is_leaf(tree.root.right_child.right_child)

    assert tree.root.bf == 0
    assert tree.root.left_child.bf == 0
    assert tree.root.left_child.left_child.bf == 0
    assert tree.root.left_child.right_child.bf == 0
    assert tree.root.right_child.bf == 0
    assert tree.root.right_child.left_child.bf == 0
    assert tree.root.right_child.right_child.bf == 0
