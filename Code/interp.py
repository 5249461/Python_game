import pygame

class interp:
    def __init__(self):
        self.old = 0.
        self.new = 0.
        self.i = 0.
        self.interping = False
    
    def set(self, new:float, old:float): 
        self.old = old
        self.new = new
        self.i = 0
        self.interping = True

    def tick(self, dt) -> float:
        self.i += dt*3
        if self.i >= 1:
            self.interping = False
            return self.new
        return pygame.math.lerp(self.old, self.new, self.i)

