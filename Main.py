# Example file showing a circle moving on screen
import pygame
import Code.Entity as entity
import Code.HUD as HUD

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920 , 1080))
clock = pygame.time.Clock()
running = True
dt = 0
score = 0
position = entity.Position(screen.get_width())
print(pygame.key.get_repeat())
player = entity.Player(screen.get_height() / 4 *3, entity.Position(screen.get_width()) )
entities = [player, entity.Enemy(screen.get_height()/2, position)] 
hud = HUD.hud(str(score))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False
            player.process_input(event)


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    for current_entity in entities:
        current_entity.process(screen)
    
    hud.render(screen)
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    score += int(1000*dt)
    hud.update(str(score))

pygame.quit()
