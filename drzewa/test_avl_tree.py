from avl_tree import AVLTree


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
    assert tree.root.key == 2
    assert tree.root.left_child.key == 1
    assert tree.root.right_child.key == 5

    assert tree.balance(tree.root) == 0
    assert tree.balance(tree.root.left_child) == 0
    assert tree.balance(tree.root.right_child) == 0


def test_tree_balance_left_right():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(3)
    assert tree.root.key == 3
    assert tree.root.left_child.key == 2
    assert tree.root.right_child.key == 5

    assert tree.balance(tree.root) == 0
    assert tree.balance(tree.root.left_child) == 0
    assert tree.balance(tree.root.right_child) == 0


def test_tree_balance_right_right():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    assert tree.root.key == 6
    assert tree.root.left_child.key == 5
    assert tree.root.right_child.key == 7

    assert tree.balance(tree.root) == 0
    assert tree.balance(tree.root.left_child) == 0
    assert tree.balance(tree.root.right_child) == 0


def test_tree_balance_right_left():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(7)
    tree.insert(6)
    assert tree.root.key == 6
    assert tree.root.left_child.key == 5
    assert tree.root.right_child.key == 7

    assert tree.balance(tree.root) == 0
    assert tree.balance(tree.root.left_child) == 0
    assert tree.balance(tree.root.right_child) == 0
