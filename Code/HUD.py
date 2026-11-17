import pygame

setmode: pygame.Surface 
font: pygame.font.Font
text: pygame.Surface

text_rect: pygame.Rect
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
PADDING = 25


class hud:
    def __init__(this, text: str):
        font = pygame.font.Font("freesansbold.ttf", 32)
        this.font = font
        text = font.render(text.rjust(6, "0"), True, white)
        this.text = text
        text_rect = text.get_rect()
        this.text_rect = text_rect
        this.text_rect.topleft = (PADDING, PADDING)

    def render(this, display: pygame.Surface):
        display.blit(this.text, this.text_rect)

    def update(this,text):
        this.text = this.font.render(text.rjust(6, "0"), True, white)
