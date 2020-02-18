#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:15:44 2020

@author: taina
"""

#Home - equivalent to main, where the objects can be created

from circular_simple import Star, Body
import matplotlib.pyplot as plt

# Creating star: spica, centered on xpos = 1, ypos = 0


spica = Star('Spica', 1, 0)

print(spica.pos())
print(spica)
print(str(spica))
print(repr(spica))

# Creating planet: Tatooine, centered on Spica, radius 0.3
                 # perigee at 0 deg, period of 1 "year"
                 # passing its perigee at time 0 "year"

tatooine = Body(spica.pos(), 0.3, 0, 1, 0)


# Plotting everything
plt.plot(spica.xpos, spica.ypos, 'xr')
plt.grid(True)

ax = plt.gca()
ax.add_patch(tatooine.orbit)
plt.axis('scaled')
plt.show() 