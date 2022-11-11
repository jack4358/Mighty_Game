import pygame
import sys
import time

pygame.init()

#screen = pygame.display.set_mode((400, 400))
#pygame.display.set_caption("This is my game")
#screen.fill((0, 0, 255))
water_image = pygame.image.load('Graphics/water_image.png')
water_rect = water_image.get_rect()
tile_size = water_rect.width
screen = pygame.display.set_mode((384, 384))
pygame.display.set_caption("This is my game")
screen.fill((0, 0, 255))


#print(water_rect)
#screen.blit(water_image,(168, 168))

screen_rect = screen.get_rect()
screen.blit(water_image, screen_rect.center)

rows = screen_rect.height/tile_size
cols = screen_rect.width/tile_size

for x in range(int(rows)):
    for y in range(int(cols)):
        screen.blit(water_image, (x*water_rect.height, y*water_rect.width))

while True:
    print("---------check for new events---------")
    recent_events = pygame.event.get()
    print("---------done checking for events---------")
    for event in recent_events:
        if event.type == pygame.QUIT:
            print("Haha I will never quit")
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                screen.fill((255, 0, 0))
            elif event.key == pygame.K_g:
                screen.fill((0, 255, 0))
            elif event.key == pygame.K_b:
                screen.fill((0, 0, 255))
    pygame.display.flip()
    time.sleep(1)
