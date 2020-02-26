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

# Creating planet: Tatooine, centered on Spica
                 # radius 0.3, perigee at 0 deg,
                 # period of 1 "year", on perigee at time 0 "year"
                 # created at time 0 "year"

tatooine = Body('Tatooine', spica, 0.3, 0, 1, 0, 0)

# Creating moon: Titan, centered on Tatooine
                 # radius 0.1, perigee at 0 deg,
                 # period of 0.5 "year", on perigee at time 0 "year"
                 # created at same time as parent

titan = Body('Titan', tatooine,  0.1, 0, 0.5, 0, tatooine.time)



print('\nChecking tree ============================'  )
print(titan.name)
print(titan)
print(titan.parent)
print(titan.parent.parent)
print(titan.parent.parent.pos())



# Evaluating number of full laps between 2 dates
# print('\n--------- Testing laps --------')
# print(tatooine.path_part_laps(0, 0.5))
# print(tatooine.path_part_laps(0, 0.99999))
# print(tatooine.path_part_laps(0, 1))
# print(tatooine.path_part_laps(0, 1.0))
# print(tatooine.path_part_laps(0, 1.00001))
# print(tatooine.path_part_laps(3, 8))
# print(tatooine.path_part_laps(3, 8.00001))      

# # Evaluating angles
# print('\n---------- Testing angles ------')
# print(tatooine.path_angle_deg(0, 0.5))
# print(tatooine.path_angle_deg(0, 0.99999))
# print(tatooine.path_angle_deg(0, 1))
# print(tatooine.path_angle_deg(0, 1.0))
# print(tatooine.path_angle_deg(0, 1.00001))
# print(tatooine.path_angle_deg(3, 8))
# print(tatooine.path_angle_deg(3, 8.00001))   

      
# Plotting everything
plt.plot(spica.xpos, spica.ypos, '*r')
plt.grid(True)
ax = plt.gca()

# Ok, very important stuff here:
# When Titan has its position requested at a given TIME, as below,
# It sets this TIME up to all the parent elements on the tree
# With this TIME set for everyone, all the orbits are calculated top-bottom
# Finally reaching Titan again.
# In summary, any pos_time request will update all the times and orbits on the tree

titan_pos = titan.pos_time(0)
tatooine_pos = tatooine.pos_time(tatooine.time)

plt.plot(tatooine_pos[0],tatooine_pos[1], 'bo')
plt.plot(titan_pos[0],titan_pos[1], 'sm')

ax.add_patch(tatooine.orbit)
ax.add_patch(titan.orbit)

plt.axis('scaled')
plt.show() 