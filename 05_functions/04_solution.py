# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math
def circle(radius):
        area =  math.pi * radius ** 2
        circumference = 2 * math.pi * radius
        return round (area, 2), round(circumference,2)

area, circumference = circle(3)

print( "Area: ",area, "circumference: ", circumference)