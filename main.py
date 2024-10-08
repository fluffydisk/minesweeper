import pygame
from ui import start_screen, play_screen, reload_screen, game_end
from utils import SCREEN_WIDTH, SCREEN_HEIGHT, running, rect1_status, rect2_status, SCREEN_TYPE,\
    mouse_pos_on_game_x,mouse_pos_on_game_y, reload, clicked_areas, bomb_area_cordinates, first_click,\
    game_finished
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mayin Tarlasi-Giris Ekrani")
pygame.display.set_icon(pygame.image.load("images/minesweeper.jpg"))


start_screen(screen, rect1_status, rect2_status)
remaining_flags=15

while running:
    left_mouse_clicked = False
    right_mouse_clicked = False
    reloading_in_progress = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                left_mouse_clicked = True
            if event.button==3:
                right_mouse_clicked=True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            reload=True
            reloading_in_progress = True

    mouse_pos = pygame.mouse.get_pos()

    if SCREEN_TYPE=="STARTING":
        button_positions1, button_positions2=start_screen(screen, rect1_status, rect2_status)

        if button_positions1.collidepoint(mouse_pos):
            if left_mouse_clicked:
                rect1_status="CLICKED"
                SCREEN_TYPE="GAME"
                left_mouse_clicked = False

            else:
                rect1_status = "ON_BUTTON"
        else:
            rect1_status = "NOT_COLLIDED"

        if button_positions2.collidepoint(mouse_pos):
            if left_mouse_clicked:
                rect2_status="CLICKED"
            else:
                rect2_status = "ON_BUTTON"
        else:
            rect2_status = "NOT_COLLIDED"
    if SCREEN_TYPE=="GAME":
        if SCREEN_TYPE == "GAME":
            pygame.display.set_caption("Mayin Tarlasi-Oyun Ekrani")
            if reload:
                first_click, remaining_flags = reload_screen(clicked_areas, bomb_area_cordinates, first_click, remaining_flags)
                SCREEN_TYPE = "STARTING"
                reload = False
            first_click, game_finished, remaining_flags, game_win = play_screen(screen, mouse_pos, left_mouse_clicked,right_mouse_clicked, first_click, remaining_flags)
            if game_finished or game_win:
                if game_finished:
                    game_end(screen, "LOSE")
                elif game_win:
                    game_end(screen, "WIN")
                pygame.display.flip()
                pygame.time.wait(2000)
                reload = True
    pygame.display.flip()
pygame.quit()