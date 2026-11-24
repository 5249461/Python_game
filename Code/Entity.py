import pygame
import random
from abc import ABC, abstractmethod
from Code.interp import interp

class Position:
    positions = [480, 960, 1440]

    @staticmethod
    def get(index: int) -> int:
        return Position.positions[index]

    def __init__(self) -> None:
        self.pos = pygame.Vector2(Position.get(1), 810)
        self.interp = interp()
    def left(self):
        if self.pos == 0:
            return
        self.interp.set(self.pos, self.pos-1)
        self.pos -=1
    def right(self):
        if self.pos == 2:
            return
        self.interp.set(, self.pos+1)
        self.pos +=1

    




class Player:
    def __init__(self): 
        self.pos = Position()

    def process(self, screen,dt ):
        pygame.draw.circle(screen, "red", self.get_pos(dt), 40)

    def process_input(self, event):
            if event.key == pygame.K_a:
                self.left()
            if event.key == pygame.K_d:
                self.right()
    def left(self):
        self.pos.left()
    def right(self):
        self.pos.right()
    def get_pos(self,dt ) -> pygame.Vector2:
        if self.pos.interp.interping:
            return pygame.Vector2(Position.get(self.pos.pos), self.pos.y)
        return pygame.Vector2(self.pos.interp.tick(dt))
        
    


class Enemy():
    
    def __init__(self):
        self.pos = pygame.Vector2(Position.get(random.randint(0,2)), -200)


class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.spawn_timer = 1
        self.enemy_speed = 10

    def process(self, screen, dt):
        for enemy in self.enemies:
            enemy.pos.y += self.enemy_speed
            pygame.draw.circle(screen, "Blue", enemy.pos, 40)
            if enemy.pos.y >= 2000:
                self.enemies.remove(enemy)
        self.spawn_timer -= dt
        if self.spawn_timer <= 0:
            self.spawn_timer = 1
            self.enemies.append(Enemy())
