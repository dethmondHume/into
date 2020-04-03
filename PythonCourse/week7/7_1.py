import math

class Sphere:
    radius = None
    x = None
    y = None
    z = None
    
    def __init__(self, radius=1.0, x=0.0, y=0.0, z=0.0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z
        
    def get_volume(self):
        return 4.0 / 3.0 * math.pi * (self.radius ** 3)
    
    def get_square(self):
        return 4.0 * math.pi * (self.radius ** 2)
    
    def get_radius(self):
        return self.radius

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, radius=1.0):
        self.radius = radius

    def set_center(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        if (x < self.x + self.radius) and (x > self.x - self.radius) and (y < self.y + self.radius) and (y > self.y - self.radius) and (z < self.z + self.radius) and (z > self.z - self.radius):#TODO
            return True
        else:
            return False
