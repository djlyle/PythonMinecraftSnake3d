# File: terraform.py
# Author: Daniel Lyle
# Date 10/23/2017
############################
import mcpi.block as block
from collections import deque
from collections import namedtuple
from random import randint

def terraform(mc):
    #Set upper blocks to air
    mc.setBlocks(-128,1,-128,128,128,128,block.AIR)
    #Set lower half of world to dirt with a layer of grass
    mc.setBlocks(-128,-1,-128,128,-128,128,block.DIRT)
    mc.setBlocks(-128,0,-128,128,0,128,block.GRASS)
    #randomly pick 10 points to create lakes
    lake_seeds = deque([])
    LakeSeed = namedtuple('LakeSeed','x y z gs')
    for i in range(10):
        x = randint(-128,128)
        y = 0
        z = randint(-128,128)
        
        #growth strength for current lake seed 
        gs = randint(1,30)
        #named tuple
        lake_seed = LakeSeed(x, y, z, gs)
        lake_seeds.append(lake_seed)

    while(len(lake_seeds) > 0):
        lake_seed = lake_seeds.popleft()

        #set lake_seed to water
        mc.setBlock(int(lake_seed.x),int(lake_seed.y), int(lake_seed.z), block.WATER.id)

        #try to grow +x
        rval = randint(1,lake_seed.gs)
        if(rval > 1):
            new_seed = LakeSeed(lake_seed.x+1,lake_seed.y,lake_seed.z,lake_seed.gs - 1)
            lake_seeds.append(new_seed)
            
        #try to grow -x
        rval = randint(1,lake_seed.gs)
        if(rval > 1):
            new_seed = LakeSeed(lake_seed.x - 1,lake_seed.y,lake_seed.z,lake_seed.gs - 1)
            lake_seeds.append(new_seed)

        #try to grow -y
        rval = randint(1,lake_seed.gs)
        if(rval > 1):
            new_seed = LakeSeed(lake_seed.x,lake_seed.y - 1,lake_seed.z,lake_seed.gs - 1)
            lake_seeds.append(new_seed)
        #try to grow +z
        rval = randint(1,lake_seed.gs)
        if(rval > 1):
            new_seed = LakeSeed(lake_seed.x,lake_seed.y,lake_seed.z + 1,lake_seed.gs - 1)
            lake_seeds.append(new_seed)
        #try to grow -z
        rval = randint(1,lake_seed.gs)
        if(rval > 1):
            new_seed = LakeSeed(lake_seed.x,lake_seed.y,lake_seed.z - 1,lake_seed.gs - 1)
            lake_seeds.append(new_seed)
        
