import sys
import pygame
from ball import Ball
from random import randint


def check_events(settings, screen, shikari, ball):
    """
    Обрабатывает событий
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, shikari, ball)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, shikari)


def check_keydown_events(event, settings, screen, shikari, ball):
    """
    Обработка нажатий клавиш
    """
    # Для текущего проекта движения право-лево заглушены
    if event.key == pygame.K_RIGHT:
        shikari.moving_right = True
    elif event.key == pygame.K_LEFT:
        shikari.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, shikari):
    """
    Обработка отпуска клавиш
    """
    if event.key == pygame.K_RIGHT:
        shikari.moving_right = False
    elif event.key == pygame.K_LEFT:
        shikari.moving_left = False


def update_screen(settings, screen, shikari, balls):
    # Перерисовка при каждом цикле
    screen.fill(settings.bg_color)
    balls.draw(screen)
    shikari.blitme()
    # Отобрвжение последнего прорисованного экрана.
    pygame.display.flip()


def update_balls(settings, screen, balls):
    """Обновление позиции мяча и уничтожение старых мячей.
    """
    balls.update()
    scr_rect = screen.get_rect()
    # Удаление мяча, вышедшего за край экрана.
    for ball in balls.copy():
        if ball.rect.bottom >= scr_rect.bottom:
            balls.remove(ball)
            print(len(ball))
            create_ball(settings, screen, balls)


def create_ball(settings, screen, balls):
    """Создание мяча.
    """
    ball = Ball(settings, screen)
    r_num = randint(10, 1000)
    ball.x = ball.width + r_num
    ball.y = ball.height
    balls.add(ball)
