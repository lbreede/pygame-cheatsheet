import pygame, sys
from constants import *
from debug import debug


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((200, 30, 30))
        self.rect = self.image.get_rect(center=(400, 400))

        # Health
        self.health_current = 500
        self.health_target = 500
        self.health_max = 1000

    def take_damage(self, amount):
        if self.health_target > 0:
            self.health_target -= amount
        if self.health_target < 0:
            self.health_target = 0

    def heal(self, amount):
        if self.health_target < self.health_max:
            self.health_target += amount
        if self.health_target > self.health_max:
            self.health_target = self.health_max

    def health_update(self):
        if self.health_current < self.health_target:
            self.health_current += HEALTH_CHANGE_SPEED
            if self.health_current > self.health_target:
                self.health_current = self.health_target

        elif self.health_current > self.health_target:
            self.health_current -= HEALTH_CHANGE_SPEED
            if self.health_current < self.health_target:
                self.health_current = self.health_target

    def health_bar(self):
        width_current = self.health_current * HEALTH_BAR_WIDTH_MULT
        width_target = self.health_target * HEALTH_BAR_WIDTH_MULT
        width_max = self.health_max * HEALTH_BAR_WIDTH_MULT

        rect_target = pygame.Rect(10, 10, width_target, 25)

        if self.health_current == self.health_target:
            width_transition = 0
            x_transition = 0
            color_transition = RED
        elif self.health_current < self.health_target:
            width_transition = width_target - width_current
            x_transition = rect_target.right - width_transition
            color_transition = GREEN
        elif self.health_current > self.health_target:
            width_transition = width_current - width_target
            x_transition = rect_target.right
            color_transition = ORANGE

        rect_transition = pygame.Rect(x_transition, 10, width_transition, 25)
        pygame.draw.rect(screen, RED, rect_target)
        pygame.draw.rect(screen, color_transition, rect_transition)
        pygame.draw.rect(screen, WHITE, (10, 10, width_max, 25), 4)

    def update(self):
        self.health_update()
        self.health_bar()


pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
player = pygame.sprite.GroupSingle(Player())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.sprite.heal(200)
            if event.key == pygame.K_DOWN:
                player.sprite.take_damage(200)

    screen.fill((30, 30, 30))
    # debug(player.sprite.health_current, y=45, x=10)
    player.draw(screen)
    player.update()
    pygame.display.update()
    clock.tick(60)
