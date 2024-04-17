from avl_tree import AVLTree


def test_insert_and_search():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(7)
    assert tree.search(2).value == 2
    assert tree.search(2).parent.value == 5
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

    assert tree.root.bf == 0
    assert tree.root.left_child.bf == 0
    assert tree.root.right_child.bf == 0


def test_tree_balance_left_right():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(2)
    tree.insert(3)
    assert tree.root.value == 2
    assert tree.root.left_child.value == 3
    assert tree.root.right_child.value == 5

    assert tree.root.bf == 0
    assert tree.root.left_child.bf == 0
    assert tree.root.right_child.bf == 0


def test_tree_balance_right_right():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    assert tree.root.value == 6
    assert tree.root.left_child.value == 5
    assert tree.root.right_child.value == 7

    assert tree.root.bf == 0
    assert tree.root.left_child.bf == 0
    assert tree.root.right_child.bf == 0


def test_tree_balance_right_left():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(7)
    tree.insert(6)
    assert tree.root.value == 7
    assert tree.root.left_child.value == 5
    assert tree.root.right_child.value == 6

    assert tree.root.bf == 0
    assert tree.root.left_child.bf == 0
    assert tree.root.right_child.bf == 0