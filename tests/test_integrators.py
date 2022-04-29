from funcode.integrators import *
import numpy as np

def test_forward_euler():
    
    def f(y, t):
        return np.r_[y[1], -y[0]]

    result = forward_euler(f)([1, 0], 0, 1)
    expected = np.r_[1, -1]

    assert(np.array_equiv(result, expected))

def test_predcorr_euler():
    
    def f(y, t):
        return np.r_[y[1], -y[0]]

    result = predcorr_euler(f)([1, 0], 0, 1)
    expected = np.r_[0.5, -1]

    assert(np.array_equiv(result, expected))