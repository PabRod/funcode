def forward_euler(f):
    
    def updater(y_0, t_0, t_1):
        y_1 = y_0 + (t_1 - t_0) * f(y_0, t_0)
        return y_1
    
    return updater

def predcorr_euler(f):
    
    def updater(y_0, t_0, t_1):
        y_a = forward_euler(f)(y_0, t_0, t_1)
        y_1 = y_0 + (t_1 - t_0) / 2 * (f(y_0, t_0) + f(y_a, t_0))
        return y_1
    
    return updater