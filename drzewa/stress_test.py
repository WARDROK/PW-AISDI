from avl_tree import AVLTree
import random


def generate_example_list(elements, start, end):
    return [random.randint(start, end) for _ in range(elements)]


def try_find_some():
    n = 100
    while True:
        tree = AVLTree()
        arr = generate_example_list(n, 1, 10)
        print(arr)
        for item in arr:
            tree.insert(item)
            tree.search(item)


def sanbox():
    tree = AVLTree()
    arr = [2, 1, 10, 6, 10, 5, 2, 1]
    print(arr)
    for item in arr:
        print('add ', item)
        tree.insert(item)
        tree.search(item)
    print('end')


try_find_some()