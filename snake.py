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
mc.player.setPos(100,10,104)

#Post message to minecraft
mc.postToChat("Minecraft snake 3d")

pos = Vector3d(100,0,100)
snake = Snake3d(mc,pos,"W",10)
snake.draw()
while True:
    snake.move()
    time.sleep(0.2)
    
