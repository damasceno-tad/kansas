import numpy as np
from scipy.integrate import odeint


def twoBody(y, t, mu):
    """
    Two Body function returns the derivative of the state space variables.
INPUTS:
    --- t ---
        A scalar time value.

    --- y ---
        A 6x1 array of the state space of a particle in 3D space
OUTPUTS:
    --- ydot ---
        The derivative of y for the two-body problem

"""

    r = np.sqrt(y[0]**2 + y[1]**2 + y[2]**2)

    ydot = np.empty((6,))

    ydot[0] = y[3]
    ydot[1] = y[4]
    ydot[2] = y[5]
    ydot[3] = (-mu/(r**3))*y[0]
    ydot[4] = (-mu/(r**3))*y[1]
    ydot[5] = (-mu/(r**3))*y[2]

    return ydot


# In m and m/s
# first three are the (x, y, z) position
# second three are the velocities in those same directions respectively
Y0 = np.array([-5614924.5443320004,
               -2014046.755686,
               2471050.0114869997,
               -673.03650300000004,
               582.41158099999996,
               1247.7034980000001])

mu = 3.986004418 * 10**14

solution = odeint(twoBody, Y0, np.linspace(0., 351., 100), args=(mu, ))
