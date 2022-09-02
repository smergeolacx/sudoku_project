from settings import *
import pygame
from sys import exit

pygame.init()
clock = pygame.time.Clock()

cell_size = 80
height = cell_size*9
width = cell_size*9
screen = pygame.display.set_mode((height,width))
text_surf = pygame.font.Font(None,int(cell_size*0.7))

#TODO: put selector and be able to change position and its value in it

sq_width = height / 9

class sudoku:


    def __init__(self,screen,height):
        self.screen = screen
        self.image = pygame.image.load("pointer.png")

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
                pygame.draw.rect(self.screen, white,pygame.Rect(sq_width * row, sq_width * column, sq_width, sq_width))
        self.grid()
        for row in range(9):
            for column in range(9):
                text = text_surf.render(prob[column][row][0], False, black)
                text_pos = text.get_rect(center=(((sq_width) * (row + 1))-sq_width/2, ((sq_width) * (column + 1))-sq_width/2))
                screen.blit(text, text_pos)

        # self.place()

    def place(self):
        pass


sudo = sudoku(screen,height)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            try:
                if event.key == pygame.K_a:
                    prob[0][0][0] = "0"
            except:pass
    screen.fill(white)
    sudo.box()

    pygame.display.flip()
    clock.tick(60)