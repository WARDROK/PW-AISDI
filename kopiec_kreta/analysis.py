import random
import time
import matplotlib.pyplot as plt
from heap import Heap

heap2 = Heap()
heap5 = Heap([], 5)
heap7 = Heap([], 7)


def heap_creation_time(generated_list, heap: Heap):
    start = time.time()
    for item in generated_list:
        heap.insert(item)
    end = time.time()
    return end - start


def heap_delete_top_time(generated_list, heap: Heap):
    size = len(generated_list)
    start = time.time()
    for i in range(size):
        heap.delete_top()
    end = time.time()
    return end - start


def generate_example_list(elements, start, end):
    return [random.randint(start, end) for _ in range(elements)]


def main():
    lists_size = [10000, 20000, 30000, 40000, 50000,
                  60000, 70000, 80000, 90000, 100000]
    creation_time_scores_2 = []
    delete_top_time_scores_2 = []
    creation_time_scores_5 = []
    delete_top_time_scores_5 = []
    creation_time_scores_7 = []
    delete_top_time_scores_7 = []

    for size in lists_size:
        generated_list = generate_example_list(size, 1, 300000)

        time = heap_creation_time(generated_list, heap2)
        creation_time_scores_2.append(time)

        time = heap_delete_top_time(generated_list, heap2)
        delete_top_time_scores_2.append(time)

        time = heap_creation_time(generated_list, heap5)
        creation_time_scores_5.append(time)

        time = heap_delete_top_time(generated_list, heap5)
        delete_top_time_scores_5.append(time)

        time = heap_creation_time(generated_list, heap7)
        creation_time_scores_7.append(time)

        time = heap_delete_top_time(generated_list, heap7)
        delete_top_time_scores_7.append(time)

    plt.plot(lists_size, creation_time_scores_2,
             label="Czas tworzenia kopca 2")
    plt.plot(lists_size, delete_top_time_scores_2,
             label="Czas usuwania szczytu kopca 2")
    plt.plot(lists_size, creation_time_scores_5,
             label="Czas tworzenia kopca 5")
    plt.plot(lists_size, delete_top_time_scores_5,
             label="Czas usuwania szczytu kopca 5")
    plt.plot(lists_size, creation_time_scores_7,
             label="Czas tworzenia kopca 7")
    plt.plot(lists_size, delete_top_time_scores_7,
             label="Czas usuwania szczytu kopca 7")
    plt.xlabel("Rozmiar listy / Liczba operacji")
    plt.ylabel("Czas (s)")
    plt.title("Wykres wydajności kopców")
    plt.legend()
    plt.savefig("wykres.pdf")
    plt.savefig("wykres.png")
    plt.show()


if __name__ == "__main__":
    main()
