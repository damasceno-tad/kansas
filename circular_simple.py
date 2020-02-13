#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:50:41 2020

@author: taina
"""

#Create a star in a fixed position

import math

class Star:
    
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    
    def pos(self):
        return self.xpos, self.ypos
    
spica = Star(1, 0)

print(spica.pos())

#Create a body orbiting the star

class Body:
    
    def __init__(self, center_xpos, center_ypos, radius, perigee_argument):
        self.center_xpos = center_xpos
        self.center_ypos = center_ypos
        self.radius = radius
        self.perigee_argument = perigee_argument
        
    def pos_init(self):
        xpos = self.center_xpos +   \
               self.radius*math.cos(math.radians(self.perigee_argument))
               
        ypos = self.center_ypos +   \
               self.radius*math.sin(math.radians(self.perigee_argument))
        return xpos, ypos
    
tatooine = Body(*spica.pos(), 1, 10)


print(tatooine.pos_init())

#Circular orbit

#Plot the path between 2 dates