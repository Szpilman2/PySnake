import pygame as game
import pygame.locals as GameGlobals
import pygame.event as GameEvents
import sys
import time
import random

class Food(object):
    def __init__(self,window):
        self.window = window

    def generate_food(self,x,y):
        #self.window.fill((100,255,100))
        food = game.draw.rect(self.window,(255,0,0),(x,y,7,7))
        game.display.update()
        return  food


class Snake(object):
    def __init__(self,window,length):
        self.length = length
        self.body_x = [50] * length
        self.body_y = [50] * length
        self.head_x = self.body_x[0]
        self.head_y = self.body_y[0]
        self.head_rect = None
        self.snake_score = 0

    def increase_snake(self):
        self.length += 1
        self.body_x.append(50)
        self.body_y.append(50)


    def draw_snake(self,window,turn,i):
        if turn == 'UP':
            self.body_y[i] -= 8
            rect = game.draw.rect(window, (0,0,0), (self.body_x[i], self.body_y[i], 7, 7))
            if i==0:
                self.head_rect = rect
        elif turn == 'DOWN':
            self.body_y[i] += 8
            rect = game.draw.rect(window, (0,0,0), (self.body_x[i], self.body_y[i] , 7, 7))
            if i==0:
                self.head_rect = rect
        elif turn == 'RIGHT':
            self.body_x[i] += 8
            rect = game.draw.rect(window, (0,0,0), (self.body_x[i] , self.body_y[i] , 7, 7))
            if i==0:
                self.head_rect = rect
        elif turn == 'LEFT':
            self.body_x[i] -= 8
            rect = game.draw.rect(window, (0,0,0), (self.body_x[i]  , self.body_y[i] , 7, 7))
            if i==0:
                self.head_rect = rect

        for j in range(len(self.body_x) - 1, 0, -1):
          #  #print(self.snake.head_x[j])
            self.body_x[j] = self.body_x[j - 1]
            self.body_y[j] = self.body_y[j - 1]
        game.display.update()


class Game(object):
    def __init__(self):
        game.init()
        self.window = game.display.set_mode((800, 800))
        game.display.set_caption("PSnake")
        self.snake = Snake(self.window,1)
        self.food = Food(self.window)


    def game_run(self):
        dx = 0
        dy = 0
        turn = 'UP'
        food_x = 450
        food_y = 450

        while(True):

            self.window.fill((100,255,100))
            for i in range (0,self.snake.length):
                self.snake.draw_snake(self.window,turn,i)

            font = game.font.SysFont(None, 24)
            img = font.render('score: ' + str(self.snake.snake_score), True, (0,0,255))
            self.window.blit(img, (20, 20))


            current_food = self.food.generate_food(food_x,food_y)

            key_input = game.key.get_pressed()
            if key_input[game.K_RIGHT] and turn!='LEFT':
                turn = 'RIGHT'
                #dx += 0.3
            elif key_input[game.K_LEFT] and turn!='RIGHT':
                turn = 'LEFT'
                #dx -= 0.3
            elif key_input[game.K_UP] and turn!='DOWN':
                turn = 'UP'
                #dy -= 0.3
            elif key_input[game.K_DOWN] and turn!='UP':
                turn = 'DOWN'
                #dy += 0.3


            if game.Rect.colliderect(current_food,self.snake.head_rect):
                #print("collide")
                self.snake.increase_snake()
                self.snake.snake_score += 1
                food_x = random.randint(0,700)
                food_y = random.randint(0,700)
                current_food = self.food.generate_food(food_x,food_y)

            for event in GameEvents.get():
                if event.type == GameGlobals.QUIT:
                    game.quit()
                    sys.exit()
            time.sleep(0.1)
            game.display.update()






s = Game()
s.game_run()


