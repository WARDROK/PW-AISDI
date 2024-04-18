from bst_tree import Tree_BST


def test_insert_and_find():
    tree = Tree_BST()
    tree.insert(5)
    tree.insert(2)
    tree.insert(7)
    assert tree.find(2).key == 2
    assert tree.find(2).parent.key == 5
    assert tree.find(5).parent is None


def test_find_not_in_tree():
    tree = Tree_BST()
    tree.insert(5)
    tree.insert(2)
    tree.insert(7)
    assert tree.find(6) is None
    assert tree.find(0) is None
    assert tree.find(-1) is None


def test_delete():
    tree = Tree_BST()
    tree.insert(5)
    tree.insert(2)
    tree.insert(7)
    assert tree.find(7)
    tree.delete_node(7)
    assert tree.find(7) is None
