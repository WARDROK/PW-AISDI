from .sorts import (bubble_sort, insertion_sort,
                    selection_sort, merge_sort,
                    quick_sort)


def test_bubble_sort():
    tab = [1, 3, 1, 2]
    tab_sorted = bubble_sort(tab)
    assert tab_sorted == [1, 1, 2, 3]


def test_bubble_sort_strings():
    tab = ['a', 'c', 'a', 'b']
    tab_sorted = bubble_sort(tab)
    assert tab_sorted == ['a', 'a', 'b', 'c']


def test_selection_sort():
    tab = [1, 3, 1, 2]
    tab_sorted = selection_sort(tab)
    assert tab_sorted == [1, 1, 2, 3]


def test_selection_sort_strings():
    tab = ['a', 'c', 'a', 'b']
    tab_sorted = selection_sort(tab)
    assert tab_sorted == ['a', 'a', 'b', 'c']


def test_insertion_sort():
    tab = [1, 3, 1, 2]
    tab_sorted = insertion_sort(tab)
    assert tab_sorted == [1, 1, 2, 3]


def test_insertion_sort_strings():
    tab = ['a', 'c', 'a', 'b']
    tab_sorted = insertion_sort(tab)
    assert tab_sorted == ['a', 'a', 'b', 'c']


def test_merge_sort():
    tab = [1, 3, 1, 2]
    tab_sorted = merge_sort(tab)
    assert tab_sorted == [1, 1, 2, 3]


def test_merge_sort_strings():
    tab = ['a', 'c', 'a', 'b']
    tab_sorted = merge_sort(tab)
    assert tab_sorted == ['a', 'a', 'b', 'c']


def test_quick_sort():
    tab = [1, 3, 1, 2]
    tab_sorted = quick_sort(tab)
    assert tab_sorted == [1, 1, 2, 3]


def test_quick_sort_strings():
    tab = ['a', 'c', 'a', 'b']
    tab_sorted = quick_sort(tab)
    assert tab_sorted == ['a', 'a', 'b', 'c']
