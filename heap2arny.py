class Heap2:

    def __init__(self, tab=None, arny = 2) -> None:
        self.tab = [None]
        self.tab += tab
        self.arny = arny

    def sort(self):
        tab = self.tab
        arny = self.arny
        for i in range(len(tab)):
            parent = i + 1
            k = arny*parent
            if (k + arny) < len(tab):
                children = [tab[k + 1], tab[k + 2]]
            elif (k + arny - 1) < len(tab):
                children = [tab[k + 1]]
            else:
                continue
            max_child = max(children)
            max_child_index = tab.index(max_child)
            if tab[max_child_index] > tab[parent]:
                tab[parent], tab[max_child_index] = tab[max_child_index], tab[parent]
        self.tab = tab

    def insert(self, val):
        pass

    def delete_top(self):
        pass

    def print(self):
        print(self.tab)


