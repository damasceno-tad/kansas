#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:50:41 2020

@authors: taina loves roncha
"""

# Create a star in a fixed position

import math

class Star:

    def __init__(self, name, xpos, ypos):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos

    def __repr__(self):
        return 'Star(\'{}\', {}, {})'.format(self.name, self.xpos, self.ypos)

    def __str__(self):
        return 'Star {} -- Position ({}, {})'.format(self.name, self.xpos, self.ypos)

    def pos(self):
        return self.xpos, self.ypos

spica = Star('Spica', 1, 0)

print(spica.pos())
print(spica)
print(str(spica))
print(repr(spica))

# Create a body orbiting the star

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
