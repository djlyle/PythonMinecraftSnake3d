# File: snake3d.py
# Author: Daniel Lyle
# Date: 06/27/2017
#######################################
from vector3d import Vector3d
import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *

def collisionAt(mc, location):
    blockAtLoc = mc.getBlock(location.x, location.y, location.z)
    if(blockAtLoc == block.AIR.id):
        return False
    else:
        return True
       
class Snake3d:
    def __init__(self, mc, position, direction, length):
        self.mc = mc
        self.position = position
        if(not(direction in [0,1,2,3,4,5])):
           direction = 0
        self.directions = ["D","N","E","S","W","U"]
        #direction is one of six values: N,E,S,W,U,D
        self.direction = direction
        self.length = length
        self.tail = []
        x = self.position.x
        y = self.position.y
        z = self.position.z
        loc = Vector3d(x,y,z)
        self.tail.insert(0, loc)
          
    def draw(self):
        #self.mc.postToChat("Drawing segments of snake")
        for segment in self.tail:
            #self.mc.postToChat("Segment: "+str(segment.x)+","+str(segment.y)+","+str(segment.z))
            self.mc.setBlock(int(segment.x), int(segment.y), int(segment.z), block.DIAMOND_BLOCK.id)

    def erase(self):
        for segment in self.tail:
            self.mc.setBlock(int(segment.x), int(segment.y), int(segment.z), block.AIR.id)
            

    def get_next_loc(self):
        newLocation = self.tail[0].clone()
        #self.mc.postToChat("get_next_loc clone at:"+str(newLocation.x)+","+str(newLocation.y)+","+str(newLocation.z))
        if(self.directions[self.direction] == "U"):
            newLocation.y += 1
        elif(self.directions[self.direction] == "D"):
            newLocation.y -= 1
        elif(self.directions[self.direction] == "N"):
            newLocation.z += 1
        elif(self.directions[self.direction] == "S"):
            newLocation.z -= 1
        elif(self.directions[self.direction] == "E"):
            newLocation.x += 1
        elif(self.directions[self.direction] == "W"):
            newLocation.x -= 1
        return newLocation
    
    def move(self):
        #self.mc.postToChat("starting move")
        #newLocation = self.get_next_loc()
        bNoCollision = False
        for i in range(0,6):
            self.direction = i
            #self.mc.postToChat("direction: "+str(self.direction))
            newLocation = self.get_next_loc()
            #if(newLocation.y - self.tail[len(self.tail)-1].y < 2):
            #don't try to go higher than one above tip of tail
            if(False == collisionAt(self.mc, newLocation)):
                bNoCollision = True
                break
            
            

        self.mc.postToChat("newLocation: "+str(newLocation.x)+","+str(newLocation.y)+","+str(newLocation.z))
            
        if(bNoCollision):
            self.mc.postToChat("no collision")
            self.position = newLocation
            self.tail.insert(0,newLocation)
            self.mc.setBlock(int(newLocation.x), int(newLocation.y), int(newLocation.z), block.DIAMOND_BLOCK.id)
            #self.mc.postToChat("length of tail: "+str(len(self.tail)))
            if(len(self.tail) > self.length):
                lastSegment = self.tail[len(self.tail)-1]
                self.mc.setBlock(int(lastSegment.x), int(lastSegment.y), int(lastSegment.z), block.AIR.id)
                #remove the last segment
                self.tail.pop()
                
            
    def setPosition(self, position):
        self.position = position
