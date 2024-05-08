from grafy import IndirectDijkstraSolver

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
    dist = solver.solve()
    solver.print_path()