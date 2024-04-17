import random
import time
import matplotlib.pyplot as plt
from bst_tree import Tree_BST
from avl_tree import AVLTree


def tree_creation_time(generated_list, tree):
    start = time.time()
    for item in generated_list:
        tree.insert(item)
    end = time.time()
    return end - start


def generate_example_list(elements, start, end):
    return [random.randint(start, end) for _ in range(elements)]


def main():
    lists_size = list(range(10000, 1000000+1, 10000))

    avl_creation_score = []
    bst_creation_score = []

    for size in lists_size:
        bst_tree = Tree_BST()
        avl_tree = AVLTree()

        generated_list = generate_example_list(size, 1, 300000)

        time = tree_creation_time(generated_list, bst_tree)
        bst_creation_score.append(time)

        time = tree_creation_time(generated_list, avl_tree)
        avl_creation_score.append(time)




    plt.plot(lists_size, bst_creation_score,
             label="Czas tworzenia drzewa BST")
    plt.plot(lists_size, avl_creation_score,
             label="Czas tworzenia drzewa AVL")

    plt.xlabel("Rozmiar listy (N)")
    plt.ylabel("Czas (s)")
    plt.title("Wykres wydajności drzew")
    plt.legend()
    plt.savefig("wykres.pdf")
    plt.savefig("wykres.png")
    plt.show()


if __name__ == "__main__":
    main()