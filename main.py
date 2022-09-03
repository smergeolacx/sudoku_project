from settings import *
import pygame
from sys import exit

pygame.init()
clock = pygame.time.Clock()

selector_x, selector_y = 0, 0
# current_pos_x,current_pos_y = 0,0
cell_size = 50
height = cell_size*9
width = cell_size*9
screen = pygame.display.set_mode((height,width))
text_surf = pygame.font.Font(None,int(cell_size*0.7))

#TODO: put selector and be able to change position and its value in it

selector_pos = ()
class sudoku:


    def __init__(self,screen,x,y):
        self.screen = screen
        self.x = x
        self.y = y
        self.current_pos_x = 0
        self.current_pos_y = 0

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
                    pygame.draw.rect(self.screen, light_gray,pygame.Rect(cell_size * row, cell_size * column, cell_size, cell_size))
                else:
                    pygame.draw.rect(self.screen, white,pygame.Rect(cell_size * row, cell_size * column, cell_size, cell_size))

        self.grid()
        for row in range(9):
            for column in range(9):
                text = text_surf.render(prob[column][row][0], False, black)
                text_pos = text.get_rect(center=(((cell_size) * (row + 1))-cell_size/2, ((cell_size) * (column + 1))-cell_size/2))
                screen.blit(text, text_pos)

sudo = sudoku(screen,selector_x,selector_y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selector_y -= cell_size
            if event.key == pygame.K_DOWN:
                selector_y += cell_size
            if event.key == pygame.K_RIGHT:
                selector_x += cell_size
            if event.key == pygame.K_LEFT:
                selector_x -= cell_size

            if isinstance(prob[int(selector_y/cell_size)][int(selector_x/cell_size)],list):
                if event.key == pygame.K_0:
                    prob[int(selector_y/cell_size)][int(selector_x/cell_size)][0] = "0"
                if event.key == pygame.K_1:
                    prob[int(selector_y/cell_size)][int(selector_x/cell_size)][0] = "1"
                if event.key == pygame.K_2:
                    prob[int(selector_y/cell_size)][int(selector_x/cell_size)][0] = "2"
                if event.key == pygame.K_3:
                    prob[int(selector_y/cell_size)][int(selector_x/cell_size)][0] = "3"
                if event.key == pygame.K_4:
                    prob[int(selector_y/cell_size)][int(selector_x/cell_size)][0] = "4"
                if event.key == pygame.K_5:
                    prob[int(selector_y/cell_size)][int(selector_x/cell_size)][0] = "5"
                if event.key == pygame.K_6:
                    prob[int(selector_y/cell_size)][int(selector_x/cell_size)][0] = "6"
                if event.key == pygame.K_7:
                    prob[int(selector_y/cell_size)][int(selector_x/cell_size)][0] = "7"
                if event.key == pygame.K_8:
                    prob[int(selector_y/cell_size)][int(selector_x/cell_size)][0] = "8"
                if event.key == pygame.K_9:
                    prob[int(selector_y/cell_size)][int(selector_x/cell_size)][0] = "9"
                if event.key == pygame.K_BACKSPACE:
                    prob[int(selector_y / cell_size)][int(selector_x / cell_size)][0] = " "

    screen.fill(white)
    sudo.box()
    pygame.draw.rect(screen, yellow, pygame.Rect(selector_x, selector_y, cell_size, cell_size), 5)
    # if selector_x < 0: selector_x = 640
    # if selector_y < 0: selector_y = 0
    # if selector_x > 640: selector_x = 640
    # if selector_y > 640: selector_y = 640
    pygame.display.flip()
    clock.tick(60)