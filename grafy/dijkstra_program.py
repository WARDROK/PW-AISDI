from indirect_dijkstra import IndirectDijkstraSolver
import time
'''
J112J
12X21
J041J
12X11
J111J

1X
J0
1X

1X
J9
1X

1X0
J90
1X1

'''

if __name__ == "__main__":
    solver = IndirectDijkstraSolver()
    solver.load_data()
    start_time = time.time()
    dist = solver.solve()
    koniec = time.time()
    czas_wykonania = koniec - start_time
    print(f"Czas wykonania: {czas_wykonania} sekund")
    solver.print_path()
