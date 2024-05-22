import sys


def get_moves_from_file(filename):
    moves = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            move = line.split(' ')
            moves.append(move)
    return moves


class TuringMachine:
    def __init__(self, tape, moves):
        self.tape = tape
        if len(self.tape) == 0:
            self.tape.append('_')
        self.moves = moves
        self.pointer = 0
        self.state = "init"
        self.ended = False
        self._load_data_structures()

    def get_all_states(self):
        all_states = []
        for move in self.moves:
            state = move[0]
            if move not in all_states:
                all_states.append(state)
        return all_states

    def _load_data_structures(self):
        all_states = self.get_all_states()
        self.state_symbol_instructions = {}
        for state in all_states:
            self.state_symbol_instructions[state] = {}

        for move in self.moves:
            state = move[0]
            symbol = move[1]
            new_instruction = (move[2], move[3], move[4])  # tuple (new_symbol, direction, new_state)
            self.state_symbol_instructions[state][symbol] = new_instruction

    def move(self):
        if self.ended:
            return
        symbol = self.tape[self.pointer]
        instruction = self.state_symbol_instructions[self.state][symbol]
        new_symbol, direction, new_state = instruction
        self.tape[self.pointer] = new_symbol
        self.state = new_state
        if direction == 'L':
            if self.pointer > 0:
                self.pointer -= 1
            else:
                self.tape.insert(0, '_')
        elif direction == 'R':
            self.pointer += 1
            if self.pointer >= len(self.tape):
                self.tape.append('_')
        if new_state.startswith('halt'):
            self.ended = True
        if self.tape[-1] == '_' and self.pointer != len(self.tape)-1:
            self.tape.pop()
        if self.tape[0] == '_' and self.pointer != 0:
            self.pointer -= 1
            self.tape.pop(0)

    def print(self):
        print(''.join(self.tape))
        if self.pointer-1 < 0:
            print('^', ' ', self.state)
        else:
            print((self.pointer-1) * ' ', '^', ' ', self.state)

    def simulate(self):
        while not self.ended:
            self.print()
            self.move()
        self.print()


def main():
    if len(sys.argv) != 3:
        print('Musisz podać plik z taśmą i plik z funkcją przejść')
        return
    tape = list(sys.argv[1])
    moves = get_moves_from_file(sys.argv[2])
    turing = TuringMachine(tape, moves)
    turing.simulate()


if __name__ == "__main__":
    main()
