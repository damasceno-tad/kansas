#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:50:41 2020

@author: taina
"""

#Create a star in a fixed position

import math
import matplotlib.pyplot as plt

class Star:
    
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    
    def pos(self):
        return [self.xpos, self.ypos]
    
spica = Star(1, 0)
print(spica.pos())


#Create a body orbiting the star

class Body:
    
    def __init__(self, center_pos, radius, perigee_argument, \
                 period, time_on_perigee):
        
        
        self.center_xpos = center_pos[0]
        self.center_ypos = center_pos[1]
        self.radius = radius
        self.perigee_argument = perigee_argument #in DEGREES
        self.period = period  
        self.time_on_perigee= time_on_perigee #must use same units as period
        
        self.orbit = plt.Circle((self.center_xpos, self.center_ypos), \
                                self.radius, fill = False)
        
            
    def pos_angle(self, angle_deg):
        xpos = self.center_xpos +   \
               self.radius*math.cos(math.radians(angle_deg))
        ypos = self.center_ypos +   \
               self.radius*math.sin(math.radians(angle_deg))
        return [xpos, ypos]

    def pos_init(self):
        [xpos, ypos] = self.pos_angle(self.perigee_argument)
        return [xpos, ypos]
    
    def pos_time(self, time):
        run_time = time - self.time_on_perigee
        angle_time_deg = math.degrees(2*math.pi*(run_time / (self.period)))
        [xpos_time, ypos_time] = self.pos_angle(angle_time_deg)
        return [xpos_time, ypos_time]
        

# Creating planet: Tatooine, centered on Spica, radius 0.3
                 # perigee at 0 deg, period of 1 "year"
                 # passing its perigee at time 0 "year"
                 
tatooine = Body(spica.pos(), 0.3, 0, 1, 0)
#print(tatooine.pos_init())

## Parte de plot - Roncha pode brincar depois
'''
plt.plot(spica.xpos, spica.ypos, 'xr')
plt.grid(True)

ax = plt.gca()
ax.add_patch(tatooine.orbit)
plt.axis('scaled')
plt.show()
'''

##### Circular orbit
# First: evaluate the body position in a given time
# DONE basic calling body.pos_time(time) will return list with [xpos, ypos]

#Plot the path between 2 dates
# TO DO