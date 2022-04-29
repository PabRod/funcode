import numpy as np

def exponential_decay(r = 1):
    
    def f(y, t):
        return -r * y
    
    return f

def harmonic_oscillator(omega_0, zeta = 0):
    
    def f(y, t):
        return np.r_[y[1], 
                     -2 * zeta * omega_0 * y[1] - omega_0**2 * y[0]]
    
    return f