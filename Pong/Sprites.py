
import pygame
import random
from Settings import *

class Block(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos):
        super().__init__()
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(center=(x_pos, y_pos))

class Player(Block):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__(path, x_pos, y_pos)
        self.speed = speed
        self.movement = 0

    def screen_col(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def update(self, ball_group=None):
        self.rect.y += self.movement
        self.screen_col()

class Opponent(Block):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__(path, x_pos, y_pos)
        self.speed = speed

    def screen_col(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def update(self, ball_group):
        if self.rect.centery < ball_group.sprite.rect.centery:
            self.rect.y += self.speed
        elif self.rect.centery > ball_group.sprite.rect.centery:
            self.rect.y -= self.speed
        self.screen_col()

class Ball(Block):
    def __init__(self, path, x_pos, y_pos, speed_x, speed_y, paddles):
        super().__init__(path, x_pos, y_pos)
        self.speed_x = speed_x * random.choice((1, -1))
        self.speed_y = speed_y * random.choice((1, -1))
        self.paddles = paddles
        self.active = True
        self.score_time = 0

    def update(self):
        if self.active:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.collisions()
        else:
            self.restart()

    def collisions(self):
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1

        collided_paddles = pygame.sprite.spritecollide(self, self.paddles, False)
        if collided_paddles:
            collision_paddle = collided_paddles[0].rect

            if abs(self.rect.right - collision_paddle.left) < 10 and self.speed_x > 0:
                self.speed_x *= -1
            if abs(self.rect.left - collision_paddle.right) < 10 and self.speed_x < 0:
                self.speed_x *= -1

            if abs(self.rect.top - collision_paddle.bottom) < 10 and self.speed_y < 0:
                self.rect.top = collision_paddle.bottom
                self.speed_y *= -1
            if abs(self.rect.bottom - collision_paddle.top) < 10 and self.speed_y > 0:
                self.rect.bottom = collision_paddle.top
                self.speed_y *= -1

    def reset_ball(self):
        self.active = False
        self.speed_x *= random.choice((-1, 1))
        self.speed_y *= random.choice((-1, 1))
        self.score_time = pygame.time.get_ticks()
        self.rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def restart(self):
        current_time = pygame.time.get_ticks()
        countdown = 3
        elapsed = current_time - self.score_time

        if elapsed <= 700:
            countdown = 3
        elif 700 < elapsed <= 1400:
            countdown = 2
        elif 1400 < elapsed <= 2100:
            countdown = 1
        elif elapsed >= 2100:
            self.active = True

        if not self.active:
            timer = FONT.render(str(countdown), True, '#04d9ff')
            timer_rect = timer.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
            pygame.display.get_surface().blit(timer, timer_rect)
