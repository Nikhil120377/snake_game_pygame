import pygame
import time
import random


snake_speed = 15


window_x = 720
window_y = 480


black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
purple = pygame.Color(128,0,128)

pygame.init()


pygame.display.set_caption('Snakes')
game_window = pygame.display.set_mode((window_x, window_y))


fps = pygame.time.Clock()
apple_image = pygame.image.load('apple-removebg-preview (1).png')
icon_image= pygame.image.load('apple-removebg-preview (1).png')
pygame.display.set_icon(icon_image)

snake_position = [100, 50]


snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]

fruit_spawn = True


direction = 'RIGHT'
change_to = direction


score = 0



def game_intro():
    intro = True
    while intro:
        game_window.fill(white)
        font = pygame.font.SysFont('Comicsansms',40)
        font1 = pygame.font.SysFont('Comicsansms',20)
        font2 = pygame.font.SysFont('Comicsansms',26)

        intro_image = font.render("Welcome to snake game",False,purple)
        intro_image1 = font1.render("Main Objective: Eat apple to grow  ",False,black)
        intro_image2 = font1.render("Survive till you can!!!", False, black)
        intro_image3 = font2.render("Press space to play and q to quit", False, black)

        intro_rect = intro_image.get_rect()
        intro_rect.center = (window_x / 2, window_y / 4)

        game_window.blit(intro_image1,(200,180))
        game_window.blit(intro_image,intro_rect)
        game_window.blit(intro_image2, (260, 200))
        game_window.blit(intro_image3, (170, 260))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over()
                elif event.key == pygame.K_SPACE:
                    intro = False




def show_score(choice, color, font, size):

    score_font = pygame.font.SysFont(font, size)


    score_surface = score_font.render('Score : ' + str(score), True, color)


    score_rect = score_surface.get_rect()


    game_window.blit(score_surface, score_rect)


def game_over():
    game_window.fill(white)
    pygame.display.update()

    my_font = pygame.font.SysFont('Comicsansms', 50)


    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)


    game_over_rect = game_over_surface.get_rect()


    game_over_rect.midtop = (window_x / 2, window_y / 4)


    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()


    time.sleep(2)


    pygame.quit()


    quit()


game_intro()

while True:


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'


        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10


        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                              random.randrange(1, (window_y // 10)) * 10]

        fruit_spawn = True
        game_window.fill(black)

        for pos in snake_body:
            pygame.draw.rect(game_window, green,
                             pygame.Rect(pos[0], pos[1], 10, 10))
        #pygame.draw.rect(game_window, white, pygame.Rect(
            #fruit_position[0], fruit_position[1], 10, 10))
        game_window.blit(apple_image,(fruit_position[0], fruit_position[1]))


        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over()


        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()


        show_score(1, white, 'Comicsansms', 20)


        pygame.display.update()


        fps.tick(snake_speed)


