# File: vector3d.py
# Author: Daniel Lyle
# Date: 06/27/2017
#################################

class Vector3d:
        def __init__(self, x=0, y=0, z=0):
                self.x = x
                self.y = y
                self.z = z

        def __iadd__(self, other):
                self.x += other.x
                self.y += other.y
                self.z += other.z
                return self
        
        def __isub__(self, other):
                self.x -= other.x
                self.y -= other.y
                self.z -= other.z
                return self
        
        def __imul__(self, k):
                self.x *= k
                self.y *= k
                self.z *= k
                return self

        def magnitude(self):
                return (self.x * self.x + self.y * self.y + self.z * self.z) ** 0.5

        def normalize(self):
                m = self.magnitude()
                self.x /= m
                self.y /= m
                self.z /= m

        def dot_product(self, other):
                return self.x * other.x + self.y * self.y + self.z * self.z 

        def clone(self):
                return Vector3d(self.x,self.y,self.z)
        
