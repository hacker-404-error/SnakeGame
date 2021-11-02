
# *********************************** HELLO GUYS THIS IS MY FIRST GAME - SNAKE GAME *******************************************

import pygame
import random
import os

pygame.mixer.init()



x = pygame.init()                                      # to initialize all function of pygame
#print(x)

screen_height = 800
screen_width = 800





#COLOURS with their RGB colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
pink = (139, 10, 80)
yellow = (255, 193, 37)
catedblue = (152, 245, 255)
gold = (255,215,0)





#CREATING WINDOW
GameWindow = pygame.display.set_mode((screen_height, screen_width))        # to set the display using set_mode(width,height)
image = pygame.image.load(r'C:\Users\Prita\PycharmProjects\SNAKE_GAME\images\python.jpg')
pygame.display.set_caption("__SNAKE GAME__")            # to set the name of the window
pygame.display.update()                                 # update above display
clock = pygame.time.Clock()


# DISPLAY FONT
font = pygame.font.SysFont(" comicsansms ", 25)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    GameWindow.blit(screen_text, [x, y])


# CREATE SNAKE
def plot_snake(GameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(GameWindow, red, [x, y, snake_size, snake_size])



def welcome():
    pygame.mixer.music.load("hello.wav")
    pygame.mixer.music.play()
    exit_game = False
    while not exit_game:

        GameWindow.fill(black)
        j = pygame.image.load(r'C:\Users\Prita\PycharmProjects\SNAKE_GAME\images\snake.jpg')
        GameWindow.blit(j, (0, -27))

        text_screen("WELCOME TO", gold, 560, 100)
        text_screen(" SNAKE GAME ", gold, 560, 140)
        text_screen("   PLAY?- ", red, 560, 260)
        text_screen("ENTER SPACE ", red, 560, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            pygame.display.update()  # update above display
            clock.tick(60)


            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('back.wav')
                    pygame.mixer.music.play()
                    game_loop()

    pygame.quit()  # after coming out from while loop our pygame will quit
    quit()



# CREATING A GAME LOOP
def game_loop():
    # GAME SPECIFIC VARIABLES
    exit_game = False
    game_over = False
    snake_x = 45  # size of our snake
    snake_y = 55  # size of our snake
    snake_size = 30  #
    velocity_x = 0
    velocity_y = 0
    fps = 20
    food_x = random.randint(10, int(screen_width / 2))
    food_y = random.randint(10, int(screen_height / 2))
    food_size = 20
    init_velocity = 10
    snake_list = []
    snake_length = 1
    score = 0

    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")
    with open ("highscore.txt", "r") as f:
        highscore = f.read()


    while not exit_game:                                   # our game window can be shown constant
        if game_over:

            with open("highscore.txt", "w") as f:
                f.write(str(highscore))

            GameWindow.fill(pink)
            #text_screen("game over press enter to continue", red, 200, 200)
            i = pygame.image.load(r'C:\Users\Prita\PycharmProjects\SNAKE_GAME\images\gameover1.jpg')
            GameWindow.blit(i, (45, 10))
            text_screen("PLEASE ENTER TO CONTINUE ", black, 200, 755)
            text_screen(" TOTAL SCORE : " + str(score), yellow, 300, 50)
            text_screen("HIGH-SCORE:" + str(highscore), yellow, 570, 50)
            text_screen("P-R-I-T-A-M--D-A-Y-S ", gold, 260, 460)
            for event in pygame.event.get():                   # for event handling
                #print(event)                                  # print all event happens inside our game
                if event.type == pygame.QUIT:                  # for event handling (quit event handling)
                    exit_game = True                           # game will quit

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():                   # for event handling
                #print(event)                                  # print all event happens inside our game
                if event.type == pygame.QUIT:                  # for event handling (quit event handling)
                    exit_game = True                           # game will quit


                #EVENT HANDLING
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #print("you have ENTERED right key")
                        #snake_x = snake_x + 10                 # snake will move right if press right key
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        #print("you have ENTERED left key")
                        #snake_x = snake_x - 10                 # snake will move right if press left key
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        #print("you have ENTERED up key")
                        #snake_y = snake_y - 10                 # snake will move right if press up key
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        #print("you have ENTERED down key")
                        #snake_y = snake_y + 10                 # snake will move right if press down key
                        velocity_y = +init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:
                        score += 10


            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 30 and abs(snake_y - food_y) < 20:
                food_x = random.randint(10, int(screen_width / 2))
                food_y = random.randint(10, int(screen_height / 2))
                score += 10
                print(" SCORE : ", score)
                snake_length += 2
                if score>int(highscore):
                    highscore = score


            GameWindow.fill(white)                             # fill our game window with black
            GameWindow.blit(image, (-50,-70))
            pygame.draw.rect(GameWindow, black, [food_x, food_y, food_size, food_size])  # draw a rectangle food
            text_screen("SCORE : " + str(score) , catedblue, 570, 20)
            text_screen( "HIGH-SCORE:" + str(highscore), red, 570, 50)
            #text_screen("P_R_I_T_A_M__D_A_Y_S", yellow, 450, 755)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]


            if head in snake_list[:-1]:
                pygame.mixer.music.load('Gameover.wav')
                pygame.mixer.music.play()
                game_over = True


            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                pygame.mixer.music.load('Gameover.wav')
                pygame.mixer.music.play()
                game_over = True
                #print("game over")
                #text_screen("G_A_M_E__O_V_E_R_!!!!", yellow, 450, 755)
            plot_snake(GameWindow, white, snake_list, snake_size)
        pygame.display.update()                            # update above display
        clock.tick(fps)








    pygame.quit()                                          # after coming out from while loop our pygame will quit
    quit()

welcome()
game_loop()

