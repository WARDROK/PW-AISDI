from sortowanie.sorts import merge_sort

def test_merge_sort():
    tab = [1, 3, 1, 2]
    tab_sorted = merge_sort(tab)
    assert tab_sorted == [1, 1, 2, 3]
