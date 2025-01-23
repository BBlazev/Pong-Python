import pygame
import sys
from Settings import *
from Sprites import Player, Opponent, Ball
from GameManager import GameManager
from Menu import Menu


def initialize_game_objects():

    player = Player(PADDLE_1_IMAGE, SCREEN_WIDTH - 20, SCREEN_HEIGHT / 2, 5)
    opponent = Opponent(PADDLE_2_IMAGE, 20, SCREEN_HEIGHT / 2, 5)

    paddle_group = pygame.sprite.Group()
    paddle_group.add(player)
    paddle_group.add(opponent)

    ball = Ball(BALL_IMAGE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 4, 4, paddle_group)
    ball_group = pygame.sprite.GroupSingle()
    ball_group.add(ball)

    game_manager = GameManager(ball_group, paddle_group, FONT)

    return game_manager, paddle_group, ball_group, player, opponent


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pong")

    menu = Menu(screen, clock)
    menu.run()

    pygame.mixer.music.stop()

    game_manager, paddle_group, ball_group, player, opponent = initialize_game_objects()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.movement -= player.speed
                elif event.key == pygame.K_DOWN:
                    player.movement += player.speed
                elif event.key == pygame.K_m:
                    current_volume = pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(min(current_volume + 0.1, 1.0))
                elif event.key == pygame.K_n:
                    current_volume = pygame.mixer.music.get_volume()
                    pygame.mixer.music.set_volume(max(current_volume - 0.1, 0.0))

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.movement += player.speed
                elif event.key == pygame.K_DOWN:
                    player.movement -= player.speed

        screen.blit(BACKGROUND, (0, 0))

        game_manager.run(screen)

        pygame.display.flip()
        clock.tick(120)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
