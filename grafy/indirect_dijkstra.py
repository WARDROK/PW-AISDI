from heap import Heap, HeapEmptyError


class IndirectDijkstraSolver:

    def __init__(self):
        self.n_rows = 0
        self.m_columns = 0
        self.table = []
        self.raw_map = []
        self.start_found = False
        self.start_i = 0
        self.start_j = 0
        self.end_i = 0
        self.end_j = 0
        self.heap = Heap()

    def load_data(self):
        while True:
            line = input().strip()
            if line == "":
                return
            line_converted = []
            line_raw = []
            for ind, char in enumerate(line):
                if char == 'J':
                    value = 0
                elif char == 'X':
                    value = 0
                    if not self.start_found:
                        self.start_i = len(self.table)
                        self.start_j = ind
                        self.start_found = True
                    else:
                        self.end_i = len(self.table)
                        self.end_j = ind
                else:
                    value = int(char)
                line_converted.append(value)
                line_raw.append(char)
            self.m_columns = len(line_converted)
            self.table.append(line_converted)
            self.raw_map.append(line_raw)
            self.n_rows = len(self.table)

    def solve(self):
        self.heap = Heap()
        self.heap.insert((-0, self.start_i, self.start_j, (None, None)))
        self.parents = []
        was_here = []
        for i in range(self.n_rows):
            was_here_row = []
            parents_row = []
            for j in range(self.m_columns):
                was_here_row.append(False)
                parents_row.append((None, None))
            was_here.append(was_here_row)
            self.parents.append(parents_row)

        self.dist_to_goal = None
        while True:
            try:
                dist, i, j, parent = self.heap.get_top()
                dist *= -1
            except HeapEmptyError:
                break
            self.heap.delete_top()

            if was_here[i][j]:
                continue
            was_here[i][j] = True
            self.parents[i][j] = parent
            if i == self.end_i and j == self.end_j:
                self.dist_to_goal = dist
                break

            if i+1 < self.n_rows:
                self.heap.insert((-dist-self.table[i+1][j], i+1, j, (i, j)))
            if i-1 >= 0:
                self.heap.insert((-dist-self.table[i-1][j], i-1, j, (i, j)))
            if j+1 < self.m_columns:
                self.heap.insert((-dist-self.table[i][j+1], i, j+1, (i, j)))
            if j-1 >= 0:
                self.heap.insert((-dist-self.table[i][j-1], i, j-1, (i, j)))

        return self.dist_to_goal

    def print_path(self):
        path = []
        i = self.end_i
        j = self.end_j
        while True:
            path.append((i, j))
            ip, jp = self.parents[i][j]
            if ip is None or jp is None:
                break
            i = ip
            j = jp

        print("Najlepsza ścieżka:")
        for i, row in enumerate(self.raw_map):
            for j, char in enumerate(row):
                if (i, j) in path:
                    print(char, end='')
                else:
                    print(' ', end='')
            print()
        print("Długość ścieżki: ", self.dist_to_goal)
