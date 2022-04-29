from funcode.funcode import solve
from funcode.integrators import *
import numpy as np

def test_solve_1d():
    f = lambda y, t : - 2 * y
    y_0 = 1
    t = np.linspace(0, 1, 1001)

    y = solve(f, y_0, t, forward_euler)
    
    f_exact = lambda t : np.exp(-2 * t)
    y_exact = f_exact(t)

    assert(np.allclose(y, y_exact, atol = 1e-3))

def test_solve_2d():
    f = lambda y, t : np.r_[y[0], -y[1]]
    y_0 = np.r_[1, 2]
    t = np.linspace(0, 1, 5001)

    y = solve(f, y_0, t, forward_euler)
    
    f_exact = lambda t : np.r_[np.exp(t), 2*np.exp(-t)]
    y_exact = list(map(f_exact, t))

    assert(np.allclose(y, y_exact, atol = 1e-3))