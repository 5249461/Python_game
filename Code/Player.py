import pygame


class Position:
    def __init__(this, screen_width):
        this.positions = [screen_width / 4, screen_width/2, screen_width/4*3]
        this.projected_pos = 1

    def left(this):
        this.projected_pos = max(this.projected_pos -1, 0)
    def right(this):
        this.projected_pos = min(this.projected_pos +1,2)


class Player:
    
    def __init__(this, y:int, current_location: Position):
        this.location = current_location
        this.player_pos = pygame.Vector2(current_location.positions[current_location.projected_pos],y)


        


