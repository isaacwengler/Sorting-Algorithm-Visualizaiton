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
NEON = (114, 218, 63)
PURPLE = (129, 34, 158)

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

    def set_height(self, height):
        self.height = height

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
    pygame.draw.rect(WIN, NAVY, pygame.Rect(int(3*WIDTH/4)+10, 0, int(WIDTH/4)-10, int(WIDTH/4)-10))
    for i in range(len(chart)):
        pygame.draw.rect(WIN, chart[i].get_color(), pygame.Rect((i * (int((WIDTH)/array_size))), 800-chart[i].get_height(), int((WIDTH)/array_size), chart[i].get_height()))

    for i in range(2):
        pygame.draw.rect(WIN, NAVY, pygame.Rect(int(WIDTH/4)*int(i+1), 27 * settings[i], int(WIDTH/4), 27), width=1)
    pygame.draw.line(WIN, NAVY, (settings[3]*int(WIDTH/4), int(WIDTH/4)-10), ((settings[3]+1)*int(WIDTH/4), int(WIDTH/4)-10))

def check_mouse():
    pos = pygame.mouse.get_pos()
    if pos[0] < int(WIDTH/4) and pos[1] < int(WIDTH/8):
        array_size = set_array()
        return array_size
    if pos[0] < int(WIDTH/4) and pos[1] > int(WIDTH/8) and pos[1] < int(WIDTH/4):
        return True

def check_key(event):
    if event.key == pygame.K_LEFT:
        settings[3] -= 1
        if settings[3] < 1:
            settings[3] = 2
    elif event.key == pygame.K_RIGHT:
        settings[3] += 1
        if settings[3] > 2:
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
        quicksort(0, len(chart)-1)
    elif settings[0] == 4:
        merge()
    elif settings[0] == 5:
        heap()
    return False

def bubble():
    for i in range(len(chart)):
        for j in range(len(chart)-i-1):
            chart[j].set_color(BLUE)
            chart[j+1].set_color(BLUE)
            draw_screen(len(chart))
            pygame.display.update()
            if chart[j].get_height() > chart[j+1].get_height():
                chart[j].set_color(NEON)
                chart[j+1].set_color(NEON)
                draw_screen(len(chart))
                pygame.display.update()
                temp = chart[j].get_height()
                chart[j].set_height(chart[j+1].get_height())
                chart[j+1].set_height(temp)
            chart[j].set_color(NAVY)
            chart[j+1].set_color(NAVY)
            if (j+1) == (len(chart)-i-1):
                chart[j+1].set_color(GREEN)
                if j == 0:
                    chart[j].set_color(GREEN)
            
def insertion():
    def color_rest_green(j):
        for i in range(j, -1, -1):
            chart[i].set_color(GREEN)
            draw_screen(len(chart))
            pygame.display.update()

    for i in range(1,len(chart)):
        key = chart[i].get_height()
        chart[i].set_height
        j = i - 1
        chart[i].set_color(PURPLE)
        draw_screen(len(chart))
        pygame.display.update()
        while j >= 0 and key < chart[j].get_height():
            chart[j + 1].set_height(chart[j].get_height())
            chart[j].set_height(key)
            chart[j].set_color(PURPLE)
            chart[j+1].set_color(BLUE)
            if i == len(chart)-1:
                chart[j + 1].set_color(GREEN)
            draw_screen(len(chart))
            pygame.display.update()
            chart[j].set_color(NAVY)
            if i != len(chart)-1:
                chart[j+1].set_color(NAVY)
            j -= 1
        if i == len(chart)-1:
            color_rest_green(j + 1)

def partition(low, high):
    i = low-1
    pivot = chart[high].get_height()
    chart[high].set_color(NEON)
    for j in range(low, high):
        chart[j].set_color(PURPLE)
        draw_screen(len(chart))
        pygame.display.update()
        if chart[j].get_height() < pivot:
            i += 1
            temp = chart[i].get_height()
            chart[i].set_height(chart[j].get_height())
            chart[j].set_height(temp)
            chart[i].set_color(BLUE)
            chart[j].set_color(BLUE)
            draw_screen(len(chart))
            pygame.display.update()
            chart[i].set_color(NAVY)
        chart[j].set_color(NAVY)
    temp = chart[i + 1].get_height()
    chart[i + 1].set_height(chart[high].get_height())
    chart[high].set_height(temp)
    chart[i+1].set_color(GREEN)
    draw_screen(len(chart))
    pygame.display.update()
    return (i+1)

def quicksort(low, high):
    if low < high:
        pi = partition(low, high)
        quicksort(low, pi-1)
        quicksort(pi+1, high)
    else:
        if low <= len(chart)-1:
            chart[low].set_color(GREEN)
        

def merge():
    array = []
    for i in range(len(chart)):
        array.append(chart[i].get_height())
    mergesort(array, 0)


def mergesort(array, pos):
    if len(array) > 1:
        m = len(array) // 2
        chart[m+pos].set_color(PURPLE)
        draw_screen(len(chart))
        pygame.display.update()
        l = array[:m]
        r = array[m:]

        mergesort(l, pos)
        mergesort(r, m + pos)

        
        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                array[k] = l[i]
                chart[pos + k].set_height(l[i])
                chart[pos + k].set_color(BLUE)
                if pos == 0 and len(array) == len(chart):
                    chart[pos + k].set_color(GREEN)
                draw_screen(len(chart))
                pygame.display.update()
                i += 1
            else:
                array[k] = r[j]
                chart[pos + k].set_height(r[j])
                chart[pos + k].set_color(BLUE)
                if pos == 0 and len(array) == len(chart):
                    chart[pos + k].set_color(GREEN)
                draw_screen(len(chart))
                pygame.display.update()
                j += 1
            k+=1
        
        while i < len(l):
            array[k] = l[i]
            chart[pos + k].set_height(l[i])
            chart[pos + k].set_color(BLUE)
            if pos == 0 and len(array) == len(chart):
                chart[pos + k].set_color(GREEN)
            draw_screen(len(chart))
            pygame.display.update()
            i += 1
            k += 1

        while j < len(r):
            array[k] = r[j]
            chart[pos + k].set_height(r[j])
            chart[pos + k].set_color(BLUE)
            if pos == 0 and len(array) == len(chart):
                chart[pos + k].set_color(GREEN)
            draw_screen(len(chart))
            pygame.display.update()
            j += 1
            k += 1       


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
                if type(temp) == int:
                    array_size = temp
                else:
                    sorting = temp
            elif event.type == pygame.KEYDOWN:
                check_key(event)
    
    if sorting:
        sorting = sort()
    draw_screen(array_size)
    pygame.display.update()


