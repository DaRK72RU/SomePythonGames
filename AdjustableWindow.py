#import
import pygame, sys, pygame_widgets
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
pygame.init()

#colors
BLACK = (0, 0, 0)

config = open('config.txt').read().split('.')[-1]
screenSize = (tuple(map(int, config.split(' '))))[:2]
pygame.display.set_caption(f"Main display, {config.replace(' ', 'x')}")
screen = pygame.display.set_mode(size = screenSize)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(BLACK)
    pygame_widgets.update(pygame.event.get())
    pygame.display.update()