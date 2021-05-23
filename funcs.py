# -*- coding: utf-8 -*-
"""
Created on Sat May 22 21:20:43 2021

@author: user
"""

import numpy as np

class Drone:
    def __init__(self, x, y, max_capacity, max_power, starting_power, charge_rate, discharge_rate):
        self.x = x
        self.y = y
        self.max_capacity = max_capacity
        self.max_power = max_power
        self.power = starting_power
        self.charge_rate = charge_rate
        self.discharge_rate = discharge_rate
        pass
    
    def consume_power(self):
        self.power = max(self.power - self.discharge_rate, 0)
    
    def charge_power(self):
        self.power = max(self.power + self.charge_rate, self.max_power)
    
    def get_capacity():
        return self.capacity
    
    def get_location(self)
        return (self.x, self.y)
        pass
    
    def set_location(self, x, y):
        self.x = x
        self.y = y
        
    def get_power():
        pass
    
    def take_step():
        current = np.array(self.get_location())
        target = np.array(self.get_current_target())
        normed_dist = np.linalg.norm(target - current)
        if normed_dist > 1:
            current = current + (target - current)/np.linalg.norm(target-current)/np.linalg.norm(target-current)
        else:
            current = current + (target - current)
            
        self.set_location(current[0], current[1])
        
        if normed_dist != 0:
            self.consume_power()
    
    def set_current_target(self, x, y):
        self.target_x = x
        self.target_y = y
        
    def get_current_target(self):
        return (self.target_x, self.target_y)
    
class Customer:
    def __init__(self, x, y, name):
        '''
        Inputs
            name: String
            x: x-coordinate of home
            y: y-coordinate of home
        
        '''
        self.name = name
        self.x = x
        self.y = y
    
    def get_location(self):
        return (self.x, self.y)
    
    def check_valid(self, bounds):
        pass
    
    def create_order(self):
        pass
    
    def get_current_order(self):
        pass
    
    
class Retailer:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        
    def get_location(self):
        return (self.x, self.y)
        
class DronePort:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fleet = []
    
    def get_location(self):
        return (self.x, self.y)
    
    def create_fleet(self, drone_list)
        for d in drone_list:
            self.add_to_fleet(d)
            
    def add_to_fleet(self, drone):
        self.fleet.append(drone)
        
    def charge_fleet(self):
        pass
    
    
def get_distance(point_A, point_B):
    return np.linalg.norm(np.array(point_A.get_distance)-np.array(point_B.get_distance))
    