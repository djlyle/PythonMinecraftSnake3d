# File: snake.py
# Author: Daniel Lyle
# Date: 06/27/2017
####################################
from vector3d import Vector3d
from snake3d import Snake3d
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

  
mc = minecraft.Minecraft.create()
mc.player.setPos(0,10,0)

#Create landscape
# Set upper half to air
mc.setBlocks(-128,1,-128,128,128,128,block.AIR)
# Set lower half of world to dirt with a layer of grass
mc.setBlocks(-128,-1,-128,128,-128,128,block.DIRT)
mc.setBlocks(-128,0,-128,128,0,128,block.GRASS)

#Post message to minecraft
mc.postToChat("Minecraft snake 3d")
snakes = []


goal = Vector3d(50,5,50)
for i in range(0,50):
    mc.setBlock(int(goal.x),int(goal.y+i), int(goal.z), block.WOOL.id, 5)
for i in range(0,5):
    pos = Vector3d(i*5,1,i*5)
    standoff_distance = 10+i*2
    snake = Snake3d(pos,"W",10,6)
    snake.setGoalPosition(goal,standoff_distance)
    snakes.append(snake) 
    #Have the snake object run in the background
    snake.daemon
    #The threading.Thread start method
    #will invoke the snake's run method
    snake.start()
#snake.draw()
    
#Loop until Ctrl+C is pressed
try:
    while True:
        #do nothing
        pass
except KeyboardInterrupt:
    print("stopped")
finally:
    #stop all the snakes (instances of Threads)
    for snake in snakes:
        snake.stop()
    
    
