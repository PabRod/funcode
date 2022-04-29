from funcode import funcode
from funcode.odes import *

def test_exponential_decay():
    assert(exponential_decay(r = 2)(3, 0) == -6)

def test_harmonic_oscillator():
    result = harmonic_oscillator(omega_0 = 2, zeta = 1)([1, 0], 0)
    expected = [0, -4]
    assert(np.array_equiv(result, expected))