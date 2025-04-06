import random
import time
import matplotlib.pyplot as plt
from bst_tree import Tree_BST
from avl_tree import AVLTree
import gc


def measure_insertion_time(tree, numbers):
    start_time = time.time()
    for num in numbers:
        tree.insert(num)
    return time.time() - start_time


def measure_search_time(tree, numbers):
    start_time = time.time()
    for num in numbers:
        tree.search(num)
    return time.time() - start_time


def measure_removal_time(tree, numbers, n):
    start_time = time.time()
    for i in range(n):
        tree.remove(numbers[i])
    return time.time() - start_time


def plot_performance(x_values, y_values_bst, y_values_avl, title, filename):
    plt.plot(x_values, y_values_bst, marker='o', label='BST')
    plt.plot(x_values, y_values_avl, marker='o', label='AVL')
    plt.xlabel('Number of Elements')
    plt.ylabel('Time (s)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.close()


def plot_removal_performance(x_values, y_values_bst, title, filename):
    plt.plot(x_values, y_values_bst, marker='o', label='BST')
    plt.xlabel('Number of Elements Removed')
    plt.ylabel('Time (s)')
    plt.title(title)
    plt.grid(True)
    plt.savefig(filename)
    plt.close()


if __name__ == "__main__":
    gc.disable()
    bst_insertion_times = []
    bst_search_times = []
    bst_removal_times = []
    avl_insertion_times = []
    avl_search_times = []
    test_case = random.sample(range(30000), 10000)
    elements_range = range(1000, 11000, 1000)

    for n in elements_range:
        numbers = test_case[:n]

        bst = Tree_BST()
        avl = AVLTree()

        bst_insertion_time = measure_insertion_time(bst, numbers)
        bst_search_time = measure_search_time(bst, numbers)
        bst_removal_time = measure_removal_time(bst, numbers, n)

        avl_insertion_time = measure_insertion_time(avl, numbers)
        avl_search_time = measure_search_time(avl, numbers)

        bst_insertion_times.append(bst_insertion_time)
        bst_search_times.append(bst_search_time)
        bst_removal_times.append(bst_removal_time)
        avl_insertion_times.append(avl_insertion_time)
        avl_search_times.append(avl_search_time)

    plot_performance(elements_range, bst_insertion_times, avl_insertion_times,
                     'Insertion Time Comparison', 'insertion.png')
    plot_performance(elements_range, bst_search_times, avl_search_times,
                     'Search Time Comparison', 'search.png')
    plot_removal_performance(elements_range, bst_removal_times,
                             'BST Removal Time', 'removal.png')
