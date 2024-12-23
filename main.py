import pygame
from Tamagotchi import Tamagotchi

WIDTH, HEIGHT = 400, 450
pygame.display.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tamagotchi")
clock = pygame.time.Clock()

background_color = (200, 180, 170)
tamagotchi = Tamagotchi()

FONT = pygame.font.SysFont("Comic Sans", 20)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
RED = (255,0,0)

def set_color(level):
    if level > 70:
        return GREEN
    if 30 <= level <=70:
        return YELLOW
    return RED

game_over = False
while game_over != True:
    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
        elif event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if feed_btn.collidepoint(event.pos):
                tamagotchi.feed()
            elif pet_btn.collidepoint(event.pos):
                tamagotchi.pet()

    tamagotchi.update()
    screen.fill(background_color)

    hunger_color = set_color(tamagotchi.hunger)
    pygame.draw.rect(screen, BLACK, pygame.Rect(50, 50, tamagotchi.hunger * 2, 20))
    hunger_text = FONT.render("Hunger",True,BLACK)
    screen.blit(hunger_text, (50, 20))

    hapiness_color = set_color(tamagotchi.happiness)
    pygame.draw.rect(screen, BLACK, pygame.Rect(50, 100, tamagotchi.happiness * 2, 20))
    happiness_text = FONT.render("Happiness",True,BLACK)
    screen.blit(happiness_text, (50, 70))

    feed_btn = pygame.Rect(225, 300, 150, 50)
    pet_btn = pygame.Rect(25, 300, 150, 50)
    pygame.draw.rect(screen, WHITE, feed_btn, 3)
    pygame.draw.rect(screen, WHITE, pet_btn, 3)

    feed_text = FONT.render("Feed", True, BLACK)
    pet_text = FONT.render("Pet", True, BLACK)

    screen.blit(feed_text, (50, 300))
    screen.blit(pet_text, (250, 300))



pygame.quit()