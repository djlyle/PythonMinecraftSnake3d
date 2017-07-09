# File: snake3d.py
# Author: Daniel Lyle
# Date: 06/27/2017
#######################################
from vector3d import Vector3d
import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *
import time
import threading
       
class Snake3d(threading.Thread):
    def __init__(self, position, direction, length, health):
        self.position = position
        self.block_id = block.WOOL.id
        self.wool_color = 14
        self.directions = ["D","N","E","S","W","U"]
        if direction in self.directions:
            self.direction = self.directions.index(direction)
        else:
            self.direction = 0

        #The snake's initial heading is set to be the same as its
        #initial direction.
        #The snake's current direction may change to avoid obstacles
        #but it's heading (general direction of travel)
        #will change less often
        self.heading = self.direction
        self.length = length
        self.health = health
        self.tail = []
        x = self.position.x
        y = self.position.y
        z = self.position.z
        loc = Vector3d(x,y,z)
        self.tail.insert(0, loc)
        threading.Thread.__init__(self)

    def collisionAt(self, location):
        blockAtLoc = self.mc.getBlock(location.x, location.y, location.z)
        if(blockAtLoc == block.AIR.id):
            #self.mc.postToChat("no collision")
            return False
        else:
            #self.mc.postToChat("collision")
            return True
        
    def draw(self):
        #self.mc.postToChat("Drawing segments of snake")
        for segment in self.tail:
            #self.mc.postToChat("Segment: "+str(segment.x)+","+str(segment.y)+","+str(segment.z))
            self.mc.setBlock(int(segment.x), int(segment.y), int(segment.z), self.block_id, self.wool_color)

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
        self.direction = 0 #Try going down first
        newLocation = self.get_next_loc()
        bCollision = self.collisionAt(newLocation)
        if(True == bCollision):
            self.direction = self.heading
            newLocation = self.get_next_loc()
            bCollision = self.collisionAt(newLocation)        
            if(True == bCollision):
                for i in range(1,6):
                    if(i == self.heading):
                        continue
                    self.direction = i
                    #self.mc.postToChat("direction: "+str(self.direction))
                    newLocation = self.get_next_loc()
                    bCollision = self.collisionAt(newLocation)      
                    if(False == bCollision):
                        break
                    
        #self.mc.postToChat("newLocation: "+str(newLocation.x)+","+str(newLocation.y)+","+str(newLocation.z))
            
        if(not(bCollision)):
            #self.mc.postToChat("no collision")
            self.position = newLocation
            self.tail.insert(0,newLocation)
            self.mc.setBlock(int(newLocation.x), int(newLocation.y), int(newLocation.z), self.block_id, self.wool_color)
            #self.mc.postToChat("length of tail: "+str(len(self.tail)))
            if(len(self.tail) > self.length):
                lastSegment = self.tail[len(self.tail)-1]
                self.mc.setBlock(int(lastSegment.x), int(lastSegment.y), int(lastSegment.z), block.AIR.id)
                #remove the last segment
                self.tail.pop()
                
            
    def setPosition(self, position):
        self.position = position

    def setHeading(self, newHeading):
        self.heading = newHeading

    def update(self):
        #TODO: maintain or change state based on current conditions
        pass
    
    def stop(self):
        self.running = False
        
    def run(self):
        self.mc = minecraft.Minecraft.create()
        self.running = True
        self.draw()
        while(self.running):
            self.update()
            self.move()
            time.sleep(0.1)
        self.erase()
            
