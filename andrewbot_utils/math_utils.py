#!/usr/bin/env python
import math

def translate_point_to_twist(x, y):
    """
    Translate point (x, y) to twist (linear movement, angular movement)
    If angle > 45:
        return linear_movement, 0
    else:
        return 0, angular_movement
    """
    magnitude, direction, quadrant = calculate_quadrant_properties(x, y)
    direction_degrees = math.degrees(direction)

    if direction_degrees > 45:
        if quadrant in [1, 2]:
            return magnitude, 0
        else:
            return -magnitude, 0

    else:
        if quadrant in [1, 4]:
            return 0, -magnitude
        else:
            return 0, magnitude
    return 0.0, 0.0

def calculate_quadrant_properties(x,y, magnitude_max=1.0):
    """
    Analyze point and return quadrant, magnitude and direction
    
    PS4 input 
    left       -1, 0
    right       1, 0
    advanced    0, 1
    forward     0,-1
    
    Quadrants
    2 | 1
    -----
    3 | 4

    
    :return: magnitude [0 - 1]
             direction [0 - PI/2]
             quadrante [1 - 4]
    """
    if x>0: # right
        quadrant = 1 if y>=0 else 4
    else:  # left
        quadrant = 2 if y>=0 else 3
            
    magnitude = math.sqrt(math.pow(x,2) + math.pow(y,2))
    
    try:
        direction = abs(math.atan(y/x))
    except ZeroDivisionError:
        direction = math.pi/2
                
    return min(magnitude, magnitude_max), direction, quadrant

def map_values(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def constrain(x, in_min, in_max):
    if x<in_min:
        return in_min
    elif x>in_max:
        return in_max
    return x

