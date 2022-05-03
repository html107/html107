import pygame
import random
from pygame import mixer

pygame.init()

icon = pygame.image.load('shell32_3.ico')
pygame.display.set_icon(icon)

white = (255, 255, 255)
yellow = (252, 252, 4)
black = (0, 0, 0)
red = (191, 191, 191)
green = (0, 255, 0)
blue = (0, 120, 215)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15


font_style = pygame.font.SysFont("SegoeUI", 20)
sad_font = pygame.font.SysFont("SegoeUI", 70)
score_font = pygame.font.SysFont("SegoeUI", 20)
description_font = pygame.font.SysFont("SegoeUI", 10)

score_num = 0

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

def sad_face(msg, color):
    mesge = sad_font.render(msg, True, color)
    dis.blit(mesge, [dis_width / 5, dis_height / 11])
def Description_NOTE(msg, color):
    megs = description_font.render(msg, True, color)
    dis.blit(megs, [dis_width / 5, dis_height / 1.9])
def Note(msg, color):
    megs = description_font.render(msg, True, color)
    dis.blit(megs, [dis_width / 5, dis_height / 2.5])
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 5, dis_height / 3])
def intructions(msg, color):
    megs = description_font.render(msg, True, color)
    dis.blit(megs, [dis_width / 5, dis_height / 2.5])


def Your_score():
    value = score_font.render("Press wasd or arrow keys to move ", True, white)
    dis.blit(value, [0, 0])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            dis.fill(blue)
            sad_face(":(", white)
            message("Game Over!", white)
            Note("Press R to Play Again or Q to Quit", white)
            Description_NOTE("NOTE: I do not own microsoft or work with them, this is just made for fun", white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, white, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 2
            eat_sound = mixer.Sound('Windows Exclamation.wav')
            eat_sound.play()
        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
