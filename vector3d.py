# File: vector3d.py
# Author: Daniel Lyle
# Date: 06/27/2017
#################################

import math

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

        def __eq__(self, other):
                if(other == None):
                        return False
                else:
                        return ((self.x == other.x) and (self.y == other.y) and (self.z == other.z))

        def __ne__(self, other):
                if(other == None):
                        return True
                else:
                        return ((self.x != other.x) or (self.y != other.y) or (self.z != other.z))
        
        def distance(self, other):
                return math.sqrt(math.pow(self.x - other.x,2) + math.pow(self.y - other.y, 2) + math.pow(self.z - other.z, 2)) 

        def taxicab_distance(self, other):
                return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)
        
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
        
