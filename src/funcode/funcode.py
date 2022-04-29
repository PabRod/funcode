from funcode.iterators import tabulate

def solve(f, y0, t, integrator):
    return tabulate(y0, t, integrator(f))