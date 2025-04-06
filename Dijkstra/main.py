import sys
from heap import Heap, HeapEmptyError
import time


class Node:
    def __init__(self, index) -> None:
        self.index = index
        self.value = 0
        self.parent = None
        self.joker = False
        self.was_here = False


def read_board(file_path):
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f]


# nonessential
def convert(board):
    board_value = []
    for row in range(len(board)):
        line = []
        for column in range(len(board[0])):
            if board[row][column] == 'X' or board[row][column] == 'J':
                line.append(0)
            else:
                line.append(int(board[row][column]))
        board_value.append(line)
    return board_value


def make_node_board(board):
    board_value = []
    for row in range(len(board)):
        line = []
        for column in range(len(board[0])):
            node = Node((row, column))
            if board[row][column] == 'X':
                line.append(node)
            elif board[row][column] == 'J':
                node.joker = True
                line.append(node)
            else:
                node.value = int(board[row][column])
                line.append(node)
        board_value.append(line)
    return board_value


def dijkstra(node_board, start, end):
    heap = Heap()
    node_board[start[0]][start[1]].distance = -0
    heap.insert((-0, node_board[start[0]][start[1]], None))

    dist_to_goal = None

    parent = None

    while True:
        try:
            distance, node, parent = heap.get_top()
            distance *= -1
        except HeapEmptyError:
            break
        heap.delete_top()

        if node.was_here:
            continue
        node.was_here = True
        node.parent = parent

        i = node.index[0]
        j = node.index[1]

        if i == end[0] and j == end[1]:
            dist_to_goal = distance
            break

        parent = node

        if node.joker:
            if i+1 < len(node_board):
                heap.insert((-distance, node_board[i+1][j], parent))
            if i-1 >= 0:
                heap.insert((-distance, node_board[i-1][j], parent))
            if j+1 < len(node_board[0]):
                heap.insert((-distance, node_board[i][j+1], parent))
            if j-1 >= 0:
                heap.insert((-distance, node_board[i][j-1], parent))
        else:
            if i+1 < len(node_board):
                heap.insert((-distance-node_board[i+1][j].value, node_board[i+1][j], parent))  # noqa: E501
            if i-1 >= 0:
                heap.insert((-distance-node_board[i-1][j].value, node_board[i-1][j], parent))  # noqa: E501
            if j+1 < len(node_board[0]):
                heap.insert((-distance-node_board[i][j+1].value, node_board[i][j+1], parent))  # noqa: E501
            if j-1 >= 0:
                heap.insert((-distance-node_board[i][j-1].value, node_board[i][j-1], parent))  # noqa: E501

    return dist_to_goal


def main(file_path):
    board = read_board(file_path)

    # Find start and end 'X'
    x_positions = [(row, column) for row in range(len(board)) for column in range(len(board[0])) if board[row][column] == 'X']  # noqa: E501
    x_amount = len(x_positions)
    if x_amount < 2:
        print(f"Nie znaleziono wystarczającej liczby 'X' na planszy.\nPodano: {x_amount} Wymagano: 2")  # noqa: E501
        return
    elif x_amount > 2:
        print(f"Podano zbyt dużo 'X' na planszy.\nPodano: {x_amount} Wymagano: 2")  # noqa: E501
        return

    start, end = x_positions[0], x_positions[1]

    # board_value = convert(board)
    start_time = time.time()
    node_board = make_node_board(board)
    koniec = time.time()

    czas_wykonania = koniec - start_time
    print(f"Czas wykonania: {czas_wykonania} sekund")

    dist_to_goal = dijkstra(node_board, start, end)

    path = []
    i = end[0]
    j = end[1]
    while True:
        path.append((i, j))
        if node_board[i][j].parent:
            ip, jp = node_board[i][j].parent.index
        else:
            break
        i = ip
        j = jp

    print("Najlepsza ścieżka:")
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            if (i, j) in path:
                print(char, end='')
            else:
                print(' ', end='')
        print()
    print("Długość ścieżki: ", dist_to_goal)

    # rinting board
    # for row in board:
    #     print(row)

    # for row in board_value:
    #     print(row)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Proszę podać nazwę pliku jako argument.")
        sys.exit(1)
    main(sys.argv[1])
