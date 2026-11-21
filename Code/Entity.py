import pygame
import random
from abc import ABC, abstractmethod

class Position:
    positions = [480, 960, 1440]
    @staticmethod
    def get(index: int) -> int:
        return Position.positions[index]




class Player:
    def __init__(self, screen: pygame.Surface):
        self.pos = pygame.Vector2(Position.get(1), (screen.get_height()/4) * 3)
        self.current_pos = 1
    def process(self, screen): 
        self.pos.x = Position.get(self.current_pos)
        # self.pos.x = Position.get(location)
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
