#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:50:41 2020

@authors: taina loves roncha
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
    
    def path_full_laps(self, time_init, time_end):
        path_time = time_end - time_init
        laps_float = path_time / float(self.period)
        full_laps = math.floor(laps_float)
        return full_laps
    
    def path_part_laps(self, time_init, time_end):
        path_time = time_end - time_init
        laps_float = path_time / float(self.period)
        part_laps = laps_float - self.path_full_laps(time_init, time_end)
        return part_laps
    
    def path_angle_deg(self, time_init, time_end):
        part_laps = self.path_part_laps(time_init, time_end)
        angle = math.degrees( part_laps * 2 * math.pi )
        return angle
        

##### Circular orbit
# First: evaluate the body position in a given time
# DONE basic calling body.pos_time(time) will return list with [xpos, ypos]

# Plot the path between 2 dates
# DONE Body now evaluates full and partial laps, and also the angle (0-360 º)

# DONE:        
# - path_angle_deg and path_*_laps return undesirable residuals,
# - Migrate from math no numpy?
#   > Actually not - using numpy gives the same precision.
#   > A larger workaround would be needed to get rid of the residuals
#   > I'm leaving it AS IS      
#   > and HERE is the another comment to diverge on purpose. This line was
#   > was added after the first HERE. Let's see where the rebase places it     
       
# TO DO:        
# - center_pos fixed on Body __init__ prevents multiple inheritance:
#        For example, a moon orbiting a planet orbiting a star can only have its position
#        calculated regarding the planet (fixed).
#        
#        In reality, the planet should have its position calculated for a given time,
#        and the moon ORBIT should be recalculated with respect to the planet new position, 
#        and only then, the moon position should be calculated

# - Maybe change the Star class to FixedBody
# - Implement a FixedBody - Bodies tree        

#Circular orbit

#Plot the path between 2 dates
