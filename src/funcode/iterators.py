def tabulate(y_0, t, integrator):
    y = [y_0]
    for i in range(1, t.size):
        y.append(integrator(y[i-1], t[i-1], t[i]))
    
    return y
