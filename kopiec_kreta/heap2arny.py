from math import ceil


class Heap2:
    def __init__(self, tab=None):
        self.tab = [0]
        if tab is not None:
            for val in tab:
                self.insert(val)

    def insert(self, val):
        self.tab.append(val)
        last_element = len(self.tab)-1
        self._repair_top(last_element)

    def delete_top(self):
        if len(self.tab) == 1:
            raise HeapEmptyError()
        top_val = self.tab[1]
        last_element = len(self.tab)-1
        self.tab[1] = self.tab[last_element]
        self.tab.pop()
        self._repair_down(1)
        return top_val  # why return?, jeśli tylko do testów to warto zmienić testy

    def get_top(self):
        if len(self.tab) == 1:
            raise HeapEmptyError()
        return self.tab[1]

    def print(self):
        next_break = 1
        for k, val in enumerate(self.tab):
            if k == 0:  # added
                continue  # added
            print(val, end=' ')
            if k % 2 == 1:  # added
                print(end=' ')  # added
            if k == next_break:
                print()
                next_break = 2*k+1

    def _repair_down(self, k):
        if k >= len(self.tab):
            return
        children = self._get_children_list(k)
        max_ind = k
        for child in children:
            if child >= len(self.tab):
                break
            if self.tab[max_ind] < self.tab[child]:
                max_ind = child
        if (k != max_ind):
            self._swap(k, max_ind)
            self._repair_down(max_ind)

    def _repair_top(self, k):
        if (k == 1):
            return
        parent = self._get_parent(k)
        if (self.tab[parent] < self.tab[k]):
            self._swap(parent, k)
            self._repair_top(parent)

    def _get_children_list(self, k):
        return [2*k, 2*k+1]

    def _get_parent(self, k):
        if (k % 2 == 1):
            k -= 1
        return ceil(k/2)

    def _swap(self, i, j):
        self.tab[i], self.tab[j] = self.tab[j], self.tab[i]


class HeapEmptyError(Exception):
    def __init__(self):
        self.message = "Heap is empty"
