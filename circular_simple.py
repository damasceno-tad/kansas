#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:50:41 2020

@author: taina
"""

import math
import matplotlib.pyplot as plt


# Create a star in a fixed position

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
        return [self.xpos, self.ypos]
    

# Create a body orbiting the star

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
        

##### Circular orbit
# First: evaluate the body position in a given time
# DONE basic calling body.pos_time(time) will return list with [xpos, ypos]

#Plot the path between 2 dates
# TO DO