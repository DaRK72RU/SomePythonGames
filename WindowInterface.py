#import
import pygame, sys, pygame_widgets
from pygame_widgets.textbox import TextBox
from pygame_widgets.button import Button
pygame.init()

#colors
GRAY = (75, 75, 75)

#setup window
pygame.display.set_caption("Set screen size")
setupScreen = pygame.display.set_mode(size = (320, 200))

screenSize = ()

#buttons
def returnSize(w, h):
    global screenSize
    screenSize = (w, h)
    print(f'Screen size - {w}x{h}')
    return (w, h)
def Close(x):
    global screenSize
    if len(screenSize) != 0:
        print(f'Size {screenSize} confirmed')
        quit()
    else:
        print(f'Select screen size first')
set640x480 = Button(setupScreen, x = 0, y = 0, width = 100, height = 50, onClick=lambda : returnSize(640, 480), text = '640x480')
set800x600 = Button(setupScreen, x = 0, y = 50, width = 100, height = 50, onClick=lambda : returnSize(800, 600), text = '800x600')
set1024x768 = Button(setupScreen, x = 0, y = 100, width = 100, height = 50, onClick=lambda : returnSize(1024, 768), text = '1024x768')
set1280x800 = Button(setupScreen, x = 100, y = 0, width = 100, height = 50, onClick=lambda : returnSize(1280, 800), text = '1280x800')
set1600x900 = Button(setupScreen, x = 100, y = 50, width = 100, height = 50, onClick=lambda : returnSize(1600, 900), text = '1600x900')
set1920x1080 = Button(setupScreen, x = 100, y = 100, width = 100, height = 50, onClick=lambda : returnSize(1920, 1080), text = '1920x1080')
confirmButton = Button(setupScreen, x = 220, y = 150, width = 100, height = 50, onClick=lambda : Close(1), text = 'Confirm')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    setupScreen.fill(GRAY)
    pygame_widgets.update(pygame.event.get())
    pygame.display.update()

#Setup is done