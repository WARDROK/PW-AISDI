def bubble_sort(tab):
    for i in range(len(tab)):
        for j in range(len(tab)-1):
            if tab[j] > tab[j + 1]:
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
    return tab


def selection_sort(tab):
    for i in range(len(tab)):
        min_index = i
        for j in range(len(tab) - i):
            if tab[min_index] > tab[i + j]:
                min_index = i + j
        tab[i], tab[min_index] = tab[min_index], tab[i]
    return tab


def insertion_sort(tab):
    for i in range(len(tab)):
        for j in range(i):
            if tab[i] < tab[i - j - 1]:
                tab[i], tab[i - j - 1] = tab[i - j - 1], tab[i]
            else:
                continue
    return tab


def merge_sort(tab_in):
    tab = tab_in
    n = len(tab)
    if (n == 1):
        return tab
    split_at = n//2
    sorted1 = merge_sort(tab[:split_at])
    sorted2 = merge_sort(tab[split_at:])
    len1 = len(sorted1)
    len2 = len(sorted2)
    tab = []
    i = 0
    j = 0
    while (i < len1 or j < len2):
        if i >= len1 or j >= len2:
            if j >= len2:
                tab.append(sorted1[i])
                i += 1
            else:
                tab.append(sorted2[j])
                j += 1
        else:
            if sorted1[i] <= sorted2[j]:
                tab.append(sorted1[i])
                i += 1
            else:
                tab.append(sorted2[j])
                j += 1
    return tab


def quick_sort(tab):
    copy_tab = tab
    quick_sort_range(copy_tab, 0, len(tab)-1)
    return copy_tab


def quick_sort_range(tab, left, right):
    if (left == right):
        return
    pivot = tab[(left+right)//2]
    i = left
    j = right
    while (i <= j):
        while (i <= right and tab[i] < pivot):
            i += 1
        while (j >= left and tab[j] > pivot):
            j -= 1
        if (i <= j):
            tab[i], tab[j] = tab[j], tab[i]
            i += 1
            j -= 1
        else:
            break
    i = min(i, right)
    j = max(j, left)
    quick_sort_range(tab, left, j)
    quick_sort_range(tab, i, right)
