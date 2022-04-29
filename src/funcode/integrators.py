def forward_euler(f):
    """ Forward Euler method
    
    Parameters
    ----------
    f : function
        Function to solve.
    """
    
    def updater(y_0, t_0, t_1):
        """ Implementation of a single step in the forward Euler method. """
        y_1 = y_0 + (t_1 - t_0) * f(y_0, t_0)
        return y_1
    
    return updater

def predcorr_euler(f):
    """ Prediction-correction Euler method
    
    Parameters
    ----------
    f : function
        Function to solve.
    """
    
    def updater(y_0, t_0, t_1):
        """ Implementation of a single step in the prediction-correction Euler method. """
        y_a = forward_euler(f)(y_0, t_0, t_1)
        y_1 = y_0 + (t_1 - t_0) / 2 * (f(y_0, t_0) + f(y_a, t_0))
        return y_1
    
    return updater