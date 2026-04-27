#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912
height = float(input("Enter the height:"))
radius = float(input("Enter the radius:"))
import math
slant_height = math.hypot(height, radius)
surface_area = math.pi * radius * (radius + slant_height)
print(f"The surface area of the cone is {surface_area}.")