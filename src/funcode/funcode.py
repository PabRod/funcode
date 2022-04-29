from funcode.iterators import tabulate

def solve(f, y0, t, integrator):
    """ Solve and ODE
    Using the given initial condition, time points, and integrator.
    
    Parameters
    ----------
    f : function
        Function to solve.
    
    y0 : array_like
        Initial condition.
        
    t : array_like
        Time points.
    """
    return tabulate(y0, t, integrator(f))