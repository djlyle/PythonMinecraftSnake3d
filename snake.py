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
mc.player.setPos(95,10,83)

#Post message to minecraft
mc.postToChat("Minecraft snake 3d")
snakes = []
for i in range(0,5):
    pos = Vector3d(95-i*5,5,83+i*5)
    snake = Snake3d(pos,"W",10,6)
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
    
    
