from bst_tree import Tree_BST


def test_insert_and_search():
    tree = Tree_BST()
    tree.insert(5)
    tree.insert(2)
    tree.insert(7)
    assert tree.search(2).key == 2
    assert tree.search(2).parent.key == 5
    assert tree.search(5).parent is None


def test_search_not_in_tree():
    tree = Tree_BST()
    tree.insert(5)
    tree.insert(2)
    tree.insert(7)
    assert tree.search(6) is None
    assert tree.search(0) is None
    assert tree.search(-1) is None


def test_remove():
    tree = Tree_BST()
    tree.insert(5)
    tree.insert(2)
    tree.insert(7)
    assert tree.search(7)
    tree.remove(7)
    assert tree.search(7) is None
