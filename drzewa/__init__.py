from bst_tree import Tree_BST


if __name__ == "__main__":
    tree = Tree_BST()
    tree.insert(4)
    tree.insert(3)
    tree.insert(5)
    tree.insert(2)
    tree.insert(8)
    tree.insert(7)
    tree.insert(9)

    tree.show_tree()

    print("------------")

    tree.delete_node(4)
    tree.show_tree()
