
import pygame
from Settings import *
from Sprites import Player, Opponent, Ball

class GameManager:
    def __init__(self, ball_group, paddle_group, font):
        self.player_score = 0
        self.opponent_score = 0
        self.ball_group = ball_group
        self.paddle_group = paddle_group
        self.font = font

    def run(self, screen):
        self.paddle_group.draw(screen)
        self.ball_group.draw(screen)

        self.paddle_group.update(self.ball_group)
        self.ball_group.update()

        self.reset_ball()
        self.draw_score(screen)

    def reset_ball(self):
        if self.ball_group.sprite.rect.right >= SCREEN_WIDTH:
            self.opponent_score += 1
            self.ball_group.sprite.reset_ball()
        if self.ball_group.sprite.rect.left <= 0:
            self.player_score += 1
            self.ball_group.sprite.reset_ball()

    def draw_score(self, screen):
        player_score_surf = self.font.render(str(self.player_score), True, '#04d9ff')
        opponent_score_surf = self.font.render(str(self.opponent_score), True, '#04d9ff')

        player_score_rect = player_score_surf.get_rect(midleft=(SCREEN_WIDTH / 2 + 40, SCREEN_HEIGHT / 2))
        opponent_score_rect = opponent_score_surf.get_rect(midright=(SCREEN_WIDTH / 2 - 40, SCREEN_HEIGHT / 2))

        screen.blit(player_score_surf, player_score_rect)
        screen.blit(opponent_score_surf, opponent_score_rect)
