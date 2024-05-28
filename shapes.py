import math

class Shape: 
        
    def calculate_area(self):
        pass
    
    def calculate_parameter(self):
        pass
    
class Rectangle(Shape):
    
    def __init__(self, length, height):
        self.length=length
        self.height=height
        
    def calculate_area(self):
        return self.length*self.height
    
    def calculate_parameter(self):
        return 2*(self.length+self.height)
    
class Circle(Shape):
    
    def __init__(self, radius):
        self.radius=radius
        
    def calculate_area(self):
        return math.pi*self.radius**2
    
    def calculate_circumference(self):
        return 2*math.pi*self.radius 
        
    def calculate_diameter(self):
        return 2*self.radius
    
    