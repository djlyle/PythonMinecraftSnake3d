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
        snakePos = snake.getPosition()
        if(snakePos == self.last_position):
            return SnakeStateSleeping()
        self.last_position = snakePos
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
        
    
    
