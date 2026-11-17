# Example file showing a circle moving on screen
import pygame
import Code.Player as player
import Code.HUD as HUD

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920 , 1080))
clock = pygame.time.Clock()
running = True
dt = 0
score = 0

print(pygame.key.get_repeat())
player = player.Player(screen.get_height() / 4 *3, player.Position(screen.get_width()) )
hud = HUD.hud(str(Score))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.location.left()
            if event.key == pygame.K_d:
                player.location.right()
            if event.key == pygame.K_x:
                running = False
            if event.key == pygame.K_y:
                text = hud.update("y")

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player.player_pos, 40)

    hud.render(screen)
    

    player.player_pos.x = player.location.positions[player.location.projected_pos]
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    score += dt

pygame.quit()