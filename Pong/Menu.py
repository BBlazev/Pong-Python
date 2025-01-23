
import pygame, sys
from Settings import *
from Sprites import Player, Opponent, Ball
from GameManager import GameManager

class Button:
    def __init__(self, text, x, y, width, height, callback, font, screen):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = '#04d9ff'
        self.callback = callback
        self.hover_color = '#0288d1'
        self.font = font
        self.screen = screen
        self.text_surf = self.font.render(self.text, True, 'white')
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.text_surf, self.text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()

class Menu:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.running = True
        self.font = pygame.font.Font("freesansbold.ttf", 50)
        self.buttons = []
        self.setup_buttons()
        self.load_assets()

    def load_assets(self):
        pygame.mixer.init()
        try:
            self.click_sound = pygame.mixer.Sound(CLICK_SOUND)
            self.click_sound.set_volume(0.3)
            pygame.mixer.music.load(MENU_MUSIC)
            pygame.mixer.music.play(-1)
        except pygame.error as e:
            print(f"Error loading sound: {e}")

        try:
            self.background_image = pygame.image.load(MENU_BACKGROUND_IMAGE)
        except pygame.error as e:
            print(f"Error loading background image: {e}")
            self.background_image = None

    def setup_buttons(self):
        button_width = 200
        button_height = 50
        start_button = Button(
            'Start Game',
            SCREEN_WIDTH//2 - button_width//2,
            SCREEN_HEIGHT//2 - 60,
            button_width,
            button_height,
            self.start_game,
            self.font,
            self.screen
        )
        quit_button = Button(
            'Quit',
            SCREEN_WIDTH//2 - button_width//2,
            SCREEN_HEIGHT//2 + 10,
            button_width,
            button_height,
            self.quit_game,
            self.font,
            self.screen
        )
        self.buttons.extend([start_button, quit_button])

    def start_game(self):
        pygame.mixer.Sound.play(self.click_sound)
        self.running = False

    def quit_game(self):
        pygame.mixer.Sound.play(self.click_sound)
        pygame.quit()
        sys.exit()

    def draw(self):
        if self.background_image:
            self.screen.blit(self.background_image, (0, 0))
        else:
            self.screen.fill(BACKGROUND)

        for button in self.buttons:
            button.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for button in self.buttons:
                button.handle_event(event)

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
