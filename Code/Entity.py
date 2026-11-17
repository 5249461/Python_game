import pygame
import random
from abc import ABC, abstractmethod

class Position:
    def __init__(self, screen_width, starting_pos = 1):
        self.positions = [screen_width / 4, screen_width/2, screen_width/4*3]
    
    def __contains__(self, item): 
        for pos in self.positions:
            if item == pos:
                return True
        return False
    def __getitem__(self, index):
        return self.positions[index]



class entity(ABC):
    def __init__(self, y, position: Position):
        self.location = position
        current_pos = 1
        self.current_pos = current_pos
        self.pos = pygame.Vector2(position[current_pos],y)
    @abstractmethod
    def process(self, screen):
        pass


class Player(entity):
    
    
    def process(self, screen): 

        self.pos.x = self.location[self.current_pos]
        pygame.draw.circle(screen, "red", self.pos, 40)

    def process_input(self, event):
            if event.key == pygame.K_a:
                self.left()
            if event.key == pygame.K_d:
                self.right()
    def left(self):
        self.current_pos = max(self.current_pos-1, 0)
    def right(self):
        self.current_pos = min(self.current_pos+1,2 )
    


class Enemy(entity):

    def process(self, screen):
        pygame.draw.circle(screen, "Blue", self.pos, 40)       
