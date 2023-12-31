'''
Python program to create a class representing a Circle. Include
methods to calculate its area and perimeter.
'''

import math

class Circle:
    def __init__(self,radius):
        self.radius=radius
        
    def calculate_area(self):
        return math.pi*self.radius**2
        
    def calculate_perimeter(self):
        return 2*math.pi*self.radius


# Created the object of class Circle provided radius
r=float(input('Enter the radius '))
circle=Circle(r)

# Calculating the area using calculate_area function
area=circle.calculate_area()

# Calculating the perimeter using calculate_perimeter
perimeter=circle.calculate_perimeter()
print(area)
print(perimeter)