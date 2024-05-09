import sys
from heap import Heap, HeapEmptyError


class Node:
    def __init__(self, index) -> None:
        self.distance = float("inf")
        self.index = index
        self.value = 0
        self.parent = None
        self.joker = False
        self.was_here = False


def read_board(file_path):
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f]


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
    heap.insert(node_board[start[0]][start[1]])

    dist_to_goal = None

    parent = None

    while True:
        try:
            node = heap.get_top()
            node.distance *= -1
        except HeapEmptyError:
            break
        heap.delete_top()

        if node.was_here:
            continue
        node.was_here = True
        node.parent = parent
        if node.index[0] == end[0] and node.index[1] == end[1]:
            dist_to_goal = node.distance
            break
        
        i = node.index[0]
        j = node.index[1]

        parent = node
        if i+1 < len(node_board):
            node_board[i+1][j].distance = -node.distance-node_board[i+1][j].value
            heap.insert((node_board[i+1][j]))
        if i-1 >= 0:
            node_board[i-1][j].distance = -node.distance-node_board[i-1][j].value
            heap.insert((node_board[i-1][j]))
        if j+1 < len(node_board[0]):
            node_board[i][j+1].distance = -node.distance-node_board[i][j+1].value
            heap.insert((node_board[i][j+1]))
        if j-1 >= 0:
            node_board[i][j-1].distance = -node.distance-node_board[i][j-1].value
            heap.insert((node_board[i][j-1]))

    return dist_to_goal

def main(file_path):
    board = read_board(file_path)

    # Find start and end 'X'
    x_positions = [(row, column) for row in range(len(board)) for column in range(len(board[0])) if board[row][column] == 'X']  # noqa: E501
    if len(x_positions) < 2:
        print("Nie znaleziono wystarczającej liczby 'X' na planszy.")
        return

    start, end = x_positions[0], x_positions[1]

    board_value = convert(board)

    node_board = make_node_board(board)

    print(dijkstra(node_board, start, end))

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

    

    # Wypisz planszę z ukrytymi polami
    for row in board:
        print(row)

    for row in board_value:
        print(row)


if __name__ == '__main__':
    # if len(sys.argv) < 2:
    #     print("Proszę podać nazwę pliku jako argument.")
    #     sys.exit(1)
    # main(sys.argv[1])
    main("grafy2/graf1.txt")