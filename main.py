# ----------- importing libraries -------------- #
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = ""
import pygame
import time
import random
import Snake1
import Snake2

# ----------- importing libraries -------------- #

# snake class
snake_1 = Snake1.Snake1()
snake_2 = Snake2.Snake2()

snake_speed = 20

# Window size
# window_x = 720
# window_y = 480
window_x = 1080
window_y = 720

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
dark_red = pygame.Color(190, 0, 0)
green = pygame.Color(0, 255, 0)
dark_green = pygame.Color(0, 190, 0)
blue = pygame.Color(0, 0, 255)
sky_blue = pygame.Color(158, 195, 255)
dark_sky_blue = pygame.Color(58, 107, 186)
grey = pygame.Color(204, 204, 204)
dark_grey = pygame.Color(116, 117, 117)

# ------------------ artifact position ------------------ #
artifact_spawn = True
artifact_position = [random.randrange(1, (window_x // 10)) * 10 + 20,
                     random.randrange(1, (window_y // 10)) * 10 - 20]
# ------------------ artifact position ------------------ #

# ------------------ fruit position ------------------ #
fruit_spawn = True
fruit_position = [random.randrange(1, (window_x // 10)) * 10 + 20,
                  random.randrange(1, (window_y // 10)) * 10 - 20]
# ------------------ fruit position ------------------ #

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Snake Game Competition')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# defining safe zone
snake_1.set_safe_zone([0, window_x - 10, 0, window_y - 10])
snake_2.set_safe_zone([0, window_x - 10, 0, window_y - 10])

# defining snake default position
snake_1_position = [0, window_y // 2]
snake_2_position = [window_x - 10, window_y // 2]
# snake_1_position = [random.randrange(1, (window_x // 10)) * 10,
#                     random.randrange(1, (window_y // 10)) * 10]
# snake_2_position = [random.randrange(1, (window_x // 10)) * 10,
#                     random.randrange(1, (window_y // 10)) * 10]
snake_1.set_position(snake_1_position)
snake_2.set_position(snake_2_position)

# defining first block of snake body
snake_1_body = [[0, window_y // 2]]
snake_2_body = [[window_x - 10, window_y // 2]]
# snake_1_body = [[random.randrange(1, (window_x // 10)) * 10,
#                  random.randrange(1, (window_y // 10)) * 10]]
# snake_2_body = [[random.randrange(1, (window_x // 10)) * 10,
#                  random.randrange(1, (window_y // 10)) * 10]]
snake_1.set_body(snake_1_body)
snake_2.set_body(snake_2_body)

# initial score
# score = 0
snake_1_score = 0
snake_2_score = 0

# time counter
main_timer = 0
snake_len = 1


# displaying Score function
def show_score(choice, color, font, size):
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render(
        '(' + str(snake_1_score) + ') ' + snake_1.get_name() + '  VS  ' + snake_2.get_name() + ' (' + str(
            snake_2_score) + ')',
        True, color)

    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect(center=(window_x // 2, window_y - (window_y * 0.95)))

    # displaying text
    game_window.blit(score_surface, score_rect)


# game over function
def game_over(snake1, action, snake2=''):
    print(str(snake1 + ' ' + action + ' ' + snake2 + '\n'))

    # creating font object my_font
    my_font = pygame.font.SysFont('tahoma', 56)
    my_font2 = pygame.font.SysFont('tahoma', 18)

    # creating a text surface on which text
    score_txt = ''
    if snake_1_score == snake_2_score:
        score_txt = 'TIE!'

    elif snake_1_score > snake_2_score:
        score_txt = snake_1.get_name() + ' WIN!'

    elif snake_1_score < snake_2_score:
        score_txt = snake_2.get_name() + ' WIN!'

    game_over_surface = my_font.render(score_txt, True, red)
    game_window_closing_txt = my_font2.render('This window will close in 5 seconds.', True, red)

    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()
    game_window_closing_txt_rect = game_window_closing_txt.get_rect()

    # setting position of the text
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window_closing_txt_rect.midtop = ((window_x / 2, window_y - 50))

    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    game_window.blit(game_window_closing_txt, game_window_closing_txt_rect)
    pygame.display.flip()

    # after 2 seconds we will quit the program
    time.sleep(5)

    # deactivating pygame library
    pygame.quit()

    # quit the program
    quit()


# Main Function
while True:

    # timer update
    main_timer += 1

    # snake flag
    snake_1_flag = ''
    snake_2_flag = ''

    # snake len control
    if main_timer % 10 == 0:
        snake_len += 1

    # snake old position
    snake_1_snapshot = snake_1.get_position()[:]
    snake_2_snapshot = snake_2.get_position()[:]

    if len(snake_1.get_body()) > snake_len:
        snake_1.body_pop()

    if len(snake_2.get_body()) > snake_len:
        snake_2.body_pop()

    # handling key events
    for event in pygame.event.get():
        # Detect window close
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # intelligences information update
    snake_1.update_enemy_body(snake_2.get_body())
    snake_1.update_artifact_position(artifact_position)
    snake_1.update_fruit_position(fruit_position)
    snake_1.update_score(snake_1_score)
    snake_1.update_enemy_score(snake_2_score)

    snake_2.update_enemy_body(snake_1.get_body())
    snake_2.update_artifact_position(artifact_position)
    snake_2.update_fruit_position(fruit_position)
    snake_2.update_score(snake_2_score)
    snake_2.update_enemy_score(snake_1_score)

    # Snake body growing mechanism
    # will be incremented by 10
    # snake_body.insert(0, list(snake_1_position))
    snake_1.snake_control()  # snake movement
    snake_2.snake_control()  # snake movement

    # print(str(snake_1.get_position()) + ' ' + str(snake_2.get_position()))
    # print(str(snake_1.get_body()))

    if snake_1.get_position()[0] == artifact_position[0] and snake_1.get_position()[1] == artifact_position[1]:
        snake_1_score -= 5
        artifact_spawn = False

    if snake_2.get_position()[0] == artifact_position[0] and snake_2.get_position()[1] == artifact_position[1]:
        snake_2_score -= 5
        artifact_spawn = False

    if snake_1.get_position()[0] == fruit_position[0] and snake_1.get_position()[1] == fruit_position[1]:
        snake_1_score += 5
        fruit_spawn = False

    if snake_2.get_position()[0] == fruit_position[0] and snake_2.get_position()[1] == fruit_position[1]:
        snake_2_score += 5
        fruit_spawn = False

    # respawn artifact
    if not artifact_spawn:
        artifact_position = [random.randrange(1, (window_x // 10)) * 10 + 20,
                             random.randrange(1, (window_y // 10)) * 10 - 20]

    artifact_spawn = True

    # respawn fruit
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10 + 20,
                          random.randrange(1, (window_y // 10)) * 10 - 20]

    fruit_spawn = True

    game_window.fill(white)

    # draw snake 1
    for pos_s1 in snake_1.get_body():
        if pos_s1 == snake_1.get_position():
            pygame.draw.rect(game_window, dark_grey, pygame.Rect(pos_s1[0], pos_s1[1], 10, 10))
        else:
            pygame.draw.rect(game_window, grey, pygame.Rect(pos_s1[0], pos_s1[1], 10, 10))

    # draw snake 2
    for pos_s2 in snake_2.get_body():
        if pos_s2 == snake_2.get_position():
            pygame.draw.rect(game_window, dark_sky_blue, pygame.Rect(pos_s2[0], pos_s2[1], 10, 10))
        else:
            pygame.draw.rect(game_window, sky_blue, pygame.Rect(pos_s2[0], pos_s2[1], 10, 10))

    # draw artifact
    pygame.draw.rect(game_window, dark_red, pygame.Rect(artifact_position[0], artifact_position[1], 10, 10))

    # draw fruit
    pygame.draw.rect(game_window, dark_green, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # ----------------- Game Over conditions -------------------- #
    if (snake_1.get_position()[0] < 0 or snake_1.get_position()[0] > window_x - 10) or (
            snake_1.get_position()[1] < 0 or snake_1.get_position()[1] > window_y - 10):
        snake_1_score -= 10
        # game_over(snake_1.get_name(), 'out of bound')
        snake_1_flag = 'OOB'

    if (snake_2.get_position()[0] < 0 or snake_2.get_position()[0] > window_x - 10) or (
            snake_2.get_position()[1] < 0 or snake_2.get_position()[1] > window_y - 10):
        snake_2_score -= 10
        # game_over(snake_2.get_name(), 'out of bound')
        snake_2_flag = 'OOB'

    # snake collision
    if snake_1.get_position()[0] == snake_2.get_position()[0] and snake_1.get_position()[1] == snake_2.get_position()[
        1]:
        snake_1_score -= 10
        snake_2_score -= 10
        # game_over(snake_1.get_name(), 'vs', snake_2.get_name())
        snake_1_flag = 'COLX'
        snake_2_flag = 'COLX'

    # touching itself
    for block_s1 in snake_1.get_body()[1:]:
        if snake_1.get_position()[0] == block_s1[0] and snake_1.get_position()[1] == block_s1[1]:
            snake_1_score -= 10
            # game_over(snake_1.get_name(), 'self destructed')
            snake_1_flag = 'SD'

    # touching enemy
    for block_s1x in snake_2.get_body()[1:]:
        if snake_1.get_position()[0] == block_s1x[0] and snake_1.get_position()[1] == block_s1x[1]:
            snake_1_score -= 10
            snake_2_score += 5
            # game_over(snake_1.get_name(), '-->', snake_2.get_name())
            snake_1_flag = 'ATE'

    # touching itself
    for block_s2 in snake_2.get_body()[1:]:
        if snake_2.get_position()[0] == block_s2[0] and snake_2.get_position()[1] == block_s2[1]:
            snake_2_score -= 10
            # game_over(snake_2.get_name(), 'self destructed')
            snake_2_flag = 'SD'

    # stuck detection
    if snake_1.get_position() == snake_1_snapshot:
        snake_1_score -= 10
        snake_1_flag = 'SD'
    if snake_2.get_position() == snake_2_snapshot:
        snake_2_score -= 10
        snake_2_flag = 'SD'

    # touching enemy
    for block_s2x in snake_1.get_body()[1:]:
        if snake_2.get_position()[0] == block_s2x[0] and snake_2.get_position()[1] == block_s2x[1]:
            snake_2_score -= 10
            snake_1_score += 5
            # game_over(snake_2.get_name(), '-->', snake_1.get_name())
            snake_2_flag = 'ATE'

    if snake_1_flag == 'OOB':
        game_over(snake_1.get_name(), 'out of bound')

    if snake_2_flag == 'OOB':
        game_over(snake_2.get_name(), 'out of bound')

    if snake_1_flag == 'ATE':
        game_over(snake_1.get_name(), '-->', snake_2.get_name())

    if snake_2_flag == 'ATE':
        game_over(snake_2.get_name(), '-->', snake_1.get_name())

    if snake_1_flag == 'COLX' and snake_2_flag == 'COLX':
        game_over(snake_1.get_name(), 'vs', snake_2.get_name())

    if snake_1_flag == 'SD':
        game_over(snake_1.get_name(), 'self destructed')

    if snake_2_flag == 'SD':
        game_over(snake_2.get_name(), 'self destructed')

    # ----------------- Game Over conditions -------------------- #

    # displaying score continuously
    show_score(1, black, 'tahoma', 24)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)
