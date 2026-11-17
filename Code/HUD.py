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
    def __init__(self, start_text: str):
        font = pygame.font.Font("freesansbold.ttf", 32)
        self.font = font
        text = font.render(start_text.rjust(6, "0"), True, white)
        self.text = text
        text_rect = text.get_rect()
        self.text_rect = text_rect
        self.text_rect.topleft = (PADDING, PADDING)

    def render(self, display: pygame.Surface):
        display.blit(self.text, self.text_rect)

    def update(self,text):
        self.text = self.font.render(text.rjust(6, "0"), True, white)
