# File: snakeStates.py
# Author: Daniel Lyle
# Date: 07/08/2017
#
#############################

class SnakeState():
    def enter(self, snake):
        pass
    
    def update(self, snake):
        pass

class SnakeStateNormal(SnakeState):
    def __init__(self):
        self.last_position = None
        
    def enter(self, snake):
        snake.speed = 1
        snake.setWoolColor(12)
        
    def update(self, snake):
        goalPos = snake.getGoalPosition()
        if(goalPos != None):
            return SnakeStateSeekingGoal()
        snakePos = snake.getPosition()
        if(snakePos == self.last_position):
            return SnakeStateSleeping()
        self.last_position = snakePos
        return self

class SnakeStateCircleGoal(SnakeState):
    def __init__(self):
       pass
    
    def enter(self, snake):
        snake.speed = 1
        snake.setWoolColor(2)
        
    def update(self, snake):
        snakePos = snake.getPosition()
        goalPos = snake.getGoalPosition()
        standoff_dist = snake.getGoalStandoffDistance()
        xDiff = goalPos.x - snakePos.x
        zDiff = goalPos.z - snakePos.z

        #Switch state if neither x or z difference is at
        #standoff_dist
        if((abs(xDiff) != standoff_dist) and
           (abs(zDiff) != standoff_dist)):
            return SnakeStateSeekingGoal()
        
        heading = snake.getHeading()
        #1---2
        #-   -
        #- x -
        #-   -
        #4---3
        if((xDiff == standoff_dist) and
           (zDiff == -standoff_dist)):
                #at a NW corner 
                snake.setHeading("E")
        elif((xDiff == -standoff_dist) and
             (zDiff == -standoff_dist)):
                #at a NE corner
                snake.setHeading("S")
        elif((xDiff == -standoff_dist) and
             (zDiff == standoff_dist)):
                #at a SE corner
                snake.setHeading("W")
        elif((xDiff == standoff_dist) and
             (zDiff == standoff_dist)):
                #at a SW corner
                snake.setHeading("N")
        return self

class SnakeStateSeekingGoal(SnakeState):
    def __init__(self):
        pass
    def enter(self, snake):
        snake.speed = 1
        snake.setWoolColor(1)
        print("seeking goal")
        
    def update(self, snake):
        snakePos = snake.getPosition()
        goalPos = snake.getGoalPosition()
        standoff_dist = snake.getGoalStandoffDistance()
        xDiff = goalPos.x - snakePos.x
        zDiff = goalPos.z - snakePos.z
        if((abs(xDiff) == standoff_dist) and
           (abs(zDiff) == standoff_dist)):
            return SnakeStateCircleGoal()
        if(abs(xDiff) > standoff_dist):
            if(xDiff > 0):
                snake.setHeading("E")
            else:
                snake.setHeading("W")
        elif(abs(zDiff) > standoff_dist):
            if(zDiff > 0):
                snake.setHeading("N")
            else:
                snake.setHeading("S")
        elif(abs(xDiff) < standoff_dist):
            if(xDiff > 0):
                snake.setHeading("W")
            else:
                snake.setHeading("E")
        elif(abs(zDiff) < standoff_dist):
            if(zDiff > 0):
                snake.setHeading("S")
            else:
                snake.setHeading("N")
        return self
    
class SnakeStateSleeping(SnakeState):
    def __init__(self):
        self.time_asleep = 0
        
    def enter(self, snake):
        snake.speed = 0
        snake.setWoolColor(9)
        
    def update(self, snake):
        if(self.time_asleep > 10):
            return SnakeStateNormal()
        self.time_asleep += 1
        return self
        
    
    
