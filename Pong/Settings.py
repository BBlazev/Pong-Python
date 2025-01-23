# Settings.py
import pygame.font
pygame.init()
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

BACKGROUND = pygame.image.load("Assets/BackgroundGrid.png")
BG_COLOR = (255, 255, 255)
STRIP = (SCREEN_WIDTH//2 - 5, 0, 10, SCREEN_HEIGHT)

FONT_NAME = 'freesansbold.ttf'
FONT_SIZE = 32
FONT = pygame.font.Font(FONT_NAME,FONT_SIZE)
PADDLE_1_IMAGE = "Assets/Paddle_1.png"
PADDLE_2_IMAGE = "Assets/Paddle_2.png"
BALL_IMAGE = "Assets/Ball.png"
MENU_BACKGROUND_IMAGE = "Assets/BackgroundGrid.png"
CLICK_SOUND = "Assets/click.wav"
MENU_MUSIC = "Assets/menu_music.mp3"
