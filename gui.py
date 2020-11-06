# gui.py - handles user interface for abalone game

import pygame

true = True
false = False

screenWidth = 1060
screenHeight = 768

tilePath = "imgs/tile.png"
logoPath = "imgs/logo.png"

gameTitle = "Abalone"

tileSpaceX = 50
tileSpaceY = 50
tileSpaceOffset = 25

def gui():
    """handles creating the user interface"""

    #init pygame
    pygame.init()
    logo = pygame.image.load(logoPath)
    pygame.display.set_icon(logo)
    pygame.display.set_caption(gameTitle)

    #create a surface
    screen = pygame.display.set_mode((screenWidth,screenHeight))

    #init board
    tile = pygame.image.load(tilePath)
    tile = pygame.transform.scale(tile, (tileSpaceX,tileSpaceY))

    #exit variable
    running = true

    #main loop
    while running:
        #event handling
        for event in pygame.event.get():
            #quit
            if event.type == pygame.QUIT:
                running = false

        keys = pygame.key.get_pressed()
        if(keys[pygame.K_q]):
            running = false

        generate_board(screen, tile)

def render_board(screen, tile, x, y):
    """renders the board"""

    screen.blit(tile, (x,y))
    pygame.display.flip()

def generate_board(screen, tile):
    k = 4
    for i in range(9):
        if(i < 5):
            k = k + 1
            l = tileSpaceOffset * (4 - i)
        else:
            k = k - 1
            l = tileSpaceOffset * (i - 4)
        for j in range(k):
            render_board(screen, tile, (tileSpaceX * j) + l, tileSpaceY * i)

gui()
