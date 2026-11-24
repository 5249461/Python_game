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
        step = 1
        self.step = step
        self.pos = pygame.Vector2(Position.get(step), 810)
        self.interp = interp()
    def left(self):
        if self.step == 0:
            return
        self.step -= 1
        self.interp.set(Position.get(self.step), self.pos.x)
    def right(self):
        if self.step == 2:
            return
        self.step +=1
        self.interp.set(Position.get(self.step), self.pos.x)

    




class Player:
    def __init__(self): 
        self.pos = Position()

    def process(self, screen,dt ):
        self.pos.pos = self.get_pos(dt)
        pygame.draw.circle(screen, "red", self.pos.pos, 40)

    def process_input(self, event):
            if event.key == pygame.K_a:
                self.pos.left()
            if event.key == pygame.K_d:
                self.pos.right()
    def get_pos(self,dt ) -> pygame.Vector2:
        if self.pos.interp.interping:
            return pygame.Vector2(self.pos.interp.tick(dt), self.pos.pos.y)
        
        return self.pos.pos
        
    


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
