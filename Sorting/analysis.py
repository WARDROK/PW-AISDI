from sorts import (bubble_sort, selection_sort, insertion_sort,
                   merge_sort, quick_sort)
import time
import matplotlib.pyplot as plt
import os


data_sizes = list(range(1000, 10000+1, 1000))
sort_names = ["bubble sort", "selection sort", "insertion sort", "merge sort",
              "quick sort"]
data_filename = os.path.join(os.path.dirname(__file__), 'pan-tadeusz.txt')


def load_data():
    with open(data_filename, "r", encoding='utf8') as file:
        data = file.read().split(' ')
        return data


def measure_function(sorting_function, data):
    start = time.process_time()
    sorting_function(data)
    stop = time.process_time()
    return stop - start


def get_results_for_function(sorting_function, data):
    results = {}
    for size in data_sizes:
        results[size] = measure_function(sorting_function, data[:size])
    return results


def get_results(data):
    return {"bubble sort": get_results_for_function(bubble_sort, data),
            "selection sort": get_results_for_function(selection_sort, data),
            "insertion sort": get_results_for_function(insertion_sort, data),
            "merge sort": get_results_for_function(merge_sort, data),
            "quick sort": get_results_for_function(quick_sort, data)}


def generate_plot(results):
    for sort_name in sort_names:
        plt.plot(results[sort_name].keys(), results[sort_name].values())
    plt.legend(sort_names)
    plt.savefig("wykresy.png")


if __name__ == '__main__':
    data = load_data()
    results = get_results(data)
    generate_plot(results)
