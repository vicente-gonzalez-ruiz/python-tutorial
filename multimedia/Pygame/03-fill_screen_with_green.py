import pygame
import my_colors as color

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fill Screen with color green")

running = True
while running:
    screen.fill(color.green)
    pygame.display.update()
    event = pygame.event.wait()  # Wait for an (input) event
    if event.type == pygame.QUIT:
        running = False

pygame.quit()
print("Goodbye!")
