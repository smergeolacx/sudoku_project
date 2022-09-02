from settings import *
import pygame
from sys import exit

pygame.init()
clock = pygame.time.Clock()

selector_x, selector_y = 0, 0

cell_size = 80
height = cell_size*9
width = cell_size*9
screen = pygame.display.set_mode((height,width))
text_surf = pygame.font.Font(None,int(cell_size*0.7))

#TODO: put selector and be able to change position and its value in it

sq_width = height / 9

class sudoku:


    def __init__(self,screen,x,y):
        self.screen = screen
        self.x = x
        self.y = y

    def grid(self):
        for i in range(10):
            if i%3 == 0:
                pygame.draw.line(self.screen, black, (0, i * height / 9), (width, i * height / 9), width=3)
                pygame.draw.line(self.screen, black, (i * height / 9, 0), (i * height / 9, width), width=3)
                pygame.rect.Rect((0,0,100,100))

                continue
            pygame.draw.line(screen, black, (0, i * height / 9), (width, i * height / 9), width=1)
            pygame.draw.line(screen, black, (i * height / 9, 0), (i * height / 9, width), width=1)

    def box(self):
        for row in range(9):
            for column in range(9):
                if isinstance(prob[column][row],str):
                    pygame.draw.rect(self.screen, light_gray,pygame.Rect(sq_width * row, sq_width * column, sq_width, sq_width))
                else:
                    pygame.draw.rect(self.screen, white,pygame.Rect(sq_width * row, sq_width * column, sq_width, sq_width))

        self.grid()
        for row in range(9):
            for column in range(9):
                text = text_surf.render(prob[column][row][0], False, black)
                text_pos = text.get_rect(center=(((sq_width) * (row + 1))-sq_width/2, ((sq_width) * (column + 1))-sq_width/2))
                screen.blit(text, text_pos)

    def selector(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= sq_width
        if keys[pygame.K_DOWN]:
            self.y += sq_width
        if keys[pygame.K_RIGHT]:
            self.x += sq_width
        if keys[pygame.K_LEFT]:
            self.x -= sq_width
        pygame.draw.rect(self.screen, yellow, pygame.Rect(self.x,self.y, sq_width, sq_width), 8)
        if self.x < 0: self.x = 0
        if self.y < 0: self.y = 0
        if self.x > 640: self.x = 640
        if self.y > 640: self.y = 640

    def modify(self):



sudo = sudoku(screen,selector_x,selector_y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_UP:
        #         selector_y -= sq_width
        #     if event.key == pygame.K_DOWN:
        #         selector_y += sq_width
        #     if event.key == pygame.K_RIGHT:
        #         selector_x += sq_width
        #     if event.key == pygame.K_LEFT:
        #         selector_x -= sq_width

    screen.fill(white)
    sudo.box()
    sudo.selector()
    # pygame.draw.rect(screen, yellow, pygame.Rect(selector_x,selector_y, sq_width, sq_width), 5)


    pygame.display.flip()
    clock.tick(10)