import pygame
import sys
import math
import random
import time

WIDTH = 800

WHITE = (255, 255, 255)
NAVY = (12, 7, 82)
BLUE = (10, 94, 125)
GREEN = (18, 117, 99)

pygame.init()
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Sorting Algorithm Visualization")
header =pygame.image.load('header.png')

settings = [1, 1, 3, 1]
chart = []



class bar:
    def __init__(self, height, color):
        self.height = height
        self.color = color

    def get_height(self):
        return self.height

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


def set_array():
    chart.clear()
    if settings[1] == 1:
        array_size = 800
    elif settings[1] == 2:
        array_size = 400
    elif settings[1] == 3:
        array_size = 100
    elif settings[1] == 4:
        array_size = 50
    elif settings[1] == 5:
        array_size = 8
    for i in range(array_size):
        chart.append(bar(random.randint(5, WIDTH * (3/4) - 5), NAVY))
    return array_size

def draw_screen(array_size):
    WIN.fill(WHITE)
    WIN.blit(header, (0, 0))
    for i in range(len(chart)):
        pygame.draw.rect(WIN, chart[i].get_color(), pygame.Rect((i * (int((WIDTH)/array_size))), 800-chart[i].get_height(), int((WIDTH)/array_size), chart[i].get_height()), width=0)

    for i in range(3):
        pygame.draw.rect(WIN, NAVY, pygame.Rect(int(WIDTH/4)*int(i+1), 27 * settings[i], int(WIDTH/4), 27), width=1)
    pygame.draw.line(WIN, NAVY, (settings[3]*int(WIDTH/4), int(WIDTH/4)-10), ((settings[3]+1)*int(WIDTH/4), int(WIDTH/4)-10))

def check_mouse():
    pos = pygame.mouse.get_pos()
    if pos[0] < int(WIDTH/4) and pos[1] < int(WIDTH/8):
        array_size = set_array()
        return False, array_size
    if pos[0] < int(WIDTH/4) and pos[1] > int(WIDTH/8) and pos[1] < int(WIDTH/4):
        return True, array_size

def check_key(event):
    if event.key == pygame.K_LEFT:
        settings[3] -= 1
        if settings[3] < 1:
            settings[3] = 3
    elif event.key == pygame.K_RIGHT:
        settings[3] += 1
        if settings[3] > 3:
            settings[3] = 1
    elif event.key == pygame.K_UP:
        settings[settings[3]-1] -= 1
        if settings[settings[3]-1] < 1:
            settings[settings[3]-1] = 5
    elif event.key == pygame.K_DOWN:
        settings[settings[3]-1] += 1
        if settings[settings[3]-1] > 5:
            settings[settings[3]-1] = 1
    
def sort():
    if settings[0] == 1:
        bubble()
    elif settings[0] == 2:
        insertion()
    elif settings[0] == 3:
        quick()
    elif settings[0] == 4:
        merge()
    elif settings[0] == 5:
        heap()
    return False





array_size = set_array()
run = True
sorting = False

while run:
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            run = False
        elif not sorting:
            if event.type == pygame.MOUSEBUTTONUP: 
                temp = check_mouse()
                sorting, array_size = temp[0], temp[1]
            elif event.type == pygame.KEYDOWN:
                check_key(event)
    
    if sorting:
        sorting = sort()
    draw_screen(array_size)
    pygame.display.update()


