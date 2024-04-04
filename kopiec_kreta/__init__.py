from heap import Heap

import random


def generuj_liste_liczb_losowych(start, koniec, ilosc):
    """
    Generuje listę losowych liczb całkowitych w określonym zakresie.

    Parametry:
    start (int): Początek zakresu (włącznie).
    koniec (int): Koniec zakresu (wyłącznie).
    ilosc (int): Ilość liczb do wygenerowania.

    Zwraca:
    list: Lista losowych liczb całkowitych w zakresie [start, koniec).
    """
    return [random.randint(start, koniec-1) for _ in range(ilosc)]


# Przykład użycia:
start = 1
koniec = 20
ilosc = 20
lista_liczb_losowych = generuj_liste_liczb_losowych(start, koniec, ilosc)
print(lista_liczb_losowych)


if __name__ == "__main__":
    test_heap = Heap(lista_liczb_losowych, 4)
    test_heap.print()
