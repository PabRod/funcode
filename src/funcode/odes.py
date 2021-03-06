# ~\~ language=Python filename=src/funcode/odes.py
# ~\~ begin <<lit/index.md|odes>>[0]
import numpy as np

def exponential_decay(r = 1):
    """ Implementation of an exponential decay """    
    def f(y, t):
        return -r * y
    
    return f
# ~\~ end
# ~\~ begin <<lit/index.md|odes>>[1]
def harmonic_oscillator(omega_0, zeta = 0):
    """ Implementation of a harmonic oscillator with damping """
    def f(y, t):
        return np.r_[y[1], 
                     -2 * zeta * omega_0 * y[1] - omega_0**2 * y[0]]
    
    return f
# ~\~ end
