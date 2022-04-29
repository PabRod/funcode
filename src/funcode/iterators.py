def tabulate(y_0, t, integrator):
    """ Iterates the integrator function over the time interval t
    and returns the result as a list.

    Parameters
    ----------
    y_0 : array_like
        Initial condition.

    t : array_like
        Time points.

    integrator : function
        Integrator function.
    """
    y = [y_0]
    for i in range(1, t.size):
        y.append(integrator(y[i-1], t[i-1], t[i]))
    
    return y
