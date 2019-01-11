import pygame
from settings import Settings
from shikari import Shikari
import game_functions as gf
from pygame.sprite import Group
from ball import Ball
pygame.init()


def run_game():
    # Инициализация игры и создание объект экрана
    gs = Settings()
    screen = pygame.display.set_mode((gs.screen_width, gs.screen_height))
    pygame.display.set_caption("Shikari")

    # Создание игрока
    shikari = Shikari(screen)
    ball = Ball(gs, screen)

    # Создание группы хранения пуль
    balls = Group()

    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мышы
        gf.check_events(gs, screen, shikari, balls)
        shikari.update()
        gf.update_balls(gs, screen, ball, balls)
        ball.update()
        gf.update_screen(gs, screen, shikari, ball)


run_game()
