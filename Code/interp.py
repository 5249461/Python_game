import pygame

class interp:
    def __init__(self):
        self.old = 0.
        self.new = 0.
        self.i = 0.
        self.interping = False
    
    def set(self, old:float, new:float): 
        self.old = old
        self.new = new
        self.i = 0
        self.interping = True

    def tick(self, dt) -> float:
        self.i += dt
        if self.i >= 1:
            return self.new
        return pygame.math.lerp(self.old, self.new, self.i)

