---
title: Solving ordinary differential equations
subtitle: with functional programming 
author: Pablo Rodríguez
---

# The problem

All ordinary differential equations are created equal:

$$
\frac{d \vec y}{dt} = \vec f(\vec y, t)
$$

This is the same to saying that the only possible difference between ordinary differential equations is the function $\vec f$.
That is, all the properties of the dynamical system are coded in that function.

The vector notation allows for using the same formula for different number of dimensions, such as:

$$
\frac{dy}{dt} = f(y, t)
$$

or:

$$
\begin{cases}
\frac{du}{dt} = f(u, v, t) \\
\frac{dv}{dt} = g(u, v, t)
\end{cases}
$$

### Higher order differential equations

Higher order differential equations can also be adapted to our formula by using the trick of introducing new variables.
We can illustrate this with an example.
Consider the equation below:

$$
\frac{d^2y}{dt^2} = f(\frac{dy}{dt}, y, t)
$$

if we define:

$$
\omega \equiv \frac{dy}{dt}
$$

we can rewrite our equation as a first-order equation:

$$
\frac{d \omega}{dt} = f(\omega, y, t)
$$

Putting all together, we end up with a two-dimensional first order equation:

$$
\begin{cases}
\frac{dy}{dt} = \omega \\
\frac{d\omega}{dt} = f(\omega, y, t)
\end{cases}
$$


## Examples

### Exponential decay

#### Formula

$$
f(y, t) = -r y
$$

#### Implementation

```{.python file=src/funcode/odes.py #odes}
import numpy as np

def exponential_decay(r = 1):
    """ Implementation of an exponential decay """    
    def f(y, t):
        return -r * y
    
    return f
```

### Harmonic oscillator

#### Formula

$$
\begin{cases}
\frac{d\theta}{dt} = \omega \\
\frac{d\omega}{dt} = -2 \zeta \omega_0 \omega - \omega_0^2 \theta
\end{cases}
$$


#### Implementation

```{.python file=src/funcode/odes.py #odes}
def harmonic_oscillator(omega_0, zeta = 0):
    """ Implementation of a harmonic oscillator with damping """
    def f(y, t):
        return np.r_[y[1], 
                     -2 * zeta * omega_0 * y[1] - omega_0**2 * y[0]]
    
    return f
```
# Solving a differential equation

The purpose of any method for solving an ordinary differential equation is to forecast the future.
More technically, the purpose is to take an initial state $\vec y_0, t_0$ and a future time $t_1$, and return the state $\vec y_1$ corresponding to the new time:

$$
\lbrace \vec y_0, t_0, t_1; \vec f \rbrace \longrightarrow \vec y_1
$$

Our approach consists on building an `integrator` method that actually performs this operation.
`integrator` has to be a functional, in the sense that its input has to be the function $f$:

$$
(\vec y_0, t_0, t_1) \xrightarrow {integrator(\vec f)} \vec y_1
$$

## Analytical example: one-dimensional state-independent differential equation

A one-dimensional state-independent differential equation can obtain by making:

$$
f(y, t) = F(t)
$$

the differential equation can be rewritten as:

$$
dy = F(t) dt
$$

and solved by direct integration:

$$
(y_0, t_0, t_1) \xrightarrow {integrator(F)} y_1 = y_0 + \int_{t_0}^{t_1}  F(s) ds
$$

## Numerical example: Euler integration

Euler's integration method is the most basic numerical method for approximating a future state $y_1$.
It takes advantage of the fact that a derivative can be approximated by a non-infinitesimal ratio of variation, i.e.:

$$
\frac{d\vec y}{dt} \approx \frac{\Delta \vec y}{\Delta t}
$$

and thus:

$$
\Delta \vec y \approx \vec f(\vec y, t) \Delta t
$$

We can thus write:

$$
(\vec y_0, t_0, t_1) \xrightarrow {integrator(\vec f)} \vec y_1 \approx \vec y_0 + (t_1 - t_0) \cdot \vec f(\vec y_0, t_0) 
$$

## Implementation

```{.python file=src/funcode/integrators.py #integrators}
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
```

```{.python file=src/funcode/integrators.py #integrators}
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
```

## Iterate

Numerical integrators are usually applied iteratively:

$$
\vec y_n = \vec y_{n-1} + integrator(\vec y_{n-1}, t_{n-1}, t_n)
$$

The code below takes care of this in a practical way:

```{.python file=src/funcode/iterators.py #iterators}
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
```

Now we are ready to solve:

```{.python file=src/funcode/funcode.py}
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
```