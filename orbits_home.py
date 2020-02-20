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


# Evaluating number of full laps between 2 dates
print('\n--------- Testing laps --------')
print(tatooine.path_part_laps(0, 0.5))
print(tatooine.path_part_laps(0, 0.99999))
print(tatooine.path_part_laps(0, 1))
print(tatooine.path_part_laps(0, 1.0))
print(tatooine.path_part_laps(0, 1.00001))
print(tatooine.path_part_laps(3, 8))
print(tatooine.path_part_laps(3, 8.00001))      

# Evaluating angles
print('\n---------- Testing angles ------')
print(tatooine.path_angle_deg(0, 0.5))
print(tatooine.path_angle_deg(0, 0.99999))
print(tatooine.path_angle_deg(0, 1))
print(tatooine.path_angle_deg(0, 1.0))
print(tatooine.path_angle_deg(0, 1.00001))
print(tatooine.path_angle_deg(3, 8))
print(tatooine.path_angle_deg(3, 8.00001))   

      
# Plotting everything
plt.plot(spica.xpos, spica.ypos, 'xr')
plt.grid(True)

ax = plt.gca()
ax.add_patch(tatooine.orbit)
plt.axis('scaled')
plt.show() 