import pygame, sys
from pygame.locals import *
from time import *
from SacaeMap import *
from Player import *


def RescaleImage(image):
    return pygame.transform.scale(image, (TILESIZE-2, TILESIZE-2))

def gridDistance(pos1, pos2):
    return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])


# Turn Debug mode on and off
DEBUG = True

# Information for Error Handling
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0]
case = 0
turn='Green'
phase='Move'

# Initialize Players and Positions
Lord = Player('Lord', 'CharacterSprites/lyn.png', [10, 9], 'Green')
Mage = Player('Mage', 'CharacterSprites/mage.png', [9, 9], 'Green')
Archer = Player('Archer', 'CharacterSprites/archer.png', [8, 9], 'Green')
Bard = Player('Bard', 'CharacterSprites/bard.png', [7, 9], 'Green')
listPLAYERS = [Lord, Mage, Archer, Bard]

Red1 = Player('Mage1', 'CharacterSprites/red_mage.png', [0, 1], 'Red')
Red2 = Player('Mage2', 'CharacterSprites/red_mage.png', [5, 3], 'Red')
Red3 = Player('Mage3', 'CharacterSprites/red_mage.png', [9, 8], 'Red')
listENEMIES = [Red1, Red2, Red3]

walk_delay = 1
walk_cd = 0

HOTKEYS = {
    1: Lord,
    2: Mage,
    3: Archer,
    4: Bard
}

# First player is default
PLAYER = listPLAYERS[0]
PLAYER_NAME = listPLAYERS[0].name
playerPos = listPLAYERS[0].position
new_coord = playerPos
clock = pygame.time.Clock()
facing = listPLAYERS[0].facing

# Initialize Cursor to load on Default Character
Cursor = pygame.image.load('CharacterSprites/cursor.png')
cursorPos = PLAYER.position

# Set up the Display
pygame.init()
if DEBUG:
    const = 200
    INVFONT = pygame.font.SysFont('FreeSans.tff', 18)

else:
    const = 0
# Create display surface
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE + const), RESIZABLE)
nextWidth=MAPWIDTH * TILESIZE
nextHeight= MAPHEIGHT * TILESIZE + const
while True:

    TILESIZE = int(nextWidth / MAPWIDTH)
    #DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE + const), RESIZABLE)
    #DISPLAYSURF.update()

    mouse_coord = [pygame.mouse.get_pos()[0] / TILESIZE, pygame.mouse.get_pos()[1] / TILESIZE]
    cursorPos = PLAYER.position

    # Movement Cooldown Clock
    turn_clock = clock.tick() / 1000.0
    walk_cd -= turn_clock

    # Get all user events
    for event in pygame.event.get():
        # If user wants to
        if (event.type == VIDEORESIZE):
            nextWidth=event.w
            nextHeight=event.h
            DISPLAYSURF = pygame.display.set_mode((event.w, event.h),
                                              pygame.RESIZABLE)

        # If user wants to quit, end game and and close window
        elif (event.type == QUIT):
            pygame.quit()
            sys.exit()

        # Mouse inputs
        elif pygame.mouse.get_pressed()[0]:
            new_coord = [int(pygame.mouse.get_pos()[0] / TILESIZE), int(pygame.mouse.get_pos()[1] / TILESIZE)]
            for player in listPLAYERS:
                if player.position == new_coord:
                    PLAYER = player

        elif (event.type == KEYDOWN):
            if (event.key == K_1):
                PLAYER = HOTKEYS[1]
                cursorPos = PLAYER.position
                new_coord = cursorPos
            if (event.key == K_2):
                PLAYER = HOTKEYS[2]
                cursorPos = PLAYER.position
                new_coord = cursorPos
            if (event.key == K_3):
                PLAYER = HOTKEYS[3]
                cursorPos = PLAYER.position
                new_coord = cursorPos
            if (event.key == K_4):
                PLAYER = HOTKEYS[4]
                cursorPos = PLAYER.position
                new_coord = cursorPos
            # Keyboard Inputs

            if phase=='Move':
                if (event.key == K_d and PLAYER.moves_left>0):
                    PLAYER.facing = 'RIGHT'
                    increment = 1
                    case = 0
                    new_coord = [PLAYER.position[0] + 1, PLAYER.position[1]]
                    if new_coord[0] not in range(MAPWIDTH):
                        increment = 0
                        case = 1
                    elif tilemap[new_coord[1]][new_coord[0]] not in PASSABLE:
                        increment = 0
                        case = 2
                    else:
                        for player in listPLAYERS + listENEMIES:
                            if new_coord == player.position:
                                increment = 0
                                case = 3
                    PLAYER.position[0] += increment
                    PLAYER.decrement_Moves(increment)

                if (event.key == K_a and PLAYER.moves_left>0):
                    PLAYER.facing = 'LEFT'
                    increment = 1
                    case = 0
                    new_coord = [PLAYER.position[0] - 1, PLAYER.position[1]]
                    if new_coord[0] not in range(MAPWIDTH):
                        increment = 0
                        case = 1
                    elif tilemap[new_coord[1]][new_coord[0]] not in PASSABLE:
                        increment = 0
                        case = 2
                    else:
                        for player in listPLAYERS + listENEMIES:
                            if new_coord == player.position:
                                increment = 0
                                case = 3
                    PLAYER.position[0] -= increment
                    PLAYER.decrement_Moves(increment)

                if (event.key == K_w and PLAYER.moves_left>0):
                    PLAYER.facing = 'UP'
                    increment = 1
                    case = 0
                    new_coord = [PLAYER.position[0], PLAYER.position[1] - 1]
                    if new_coord[1] not in range(MAPHEIGHT):
                        increment = 0
                        case = 1
                    elif tilemap[new_coord[1]][new_coord[0]] not in PASSABLE:
                        increment = 0
                        case = 2
                    else:
                        for player in listPLAYERS + listENEMIES:
                            if new_coord == player.position:
                                increment = 0
                                case = 3
                    PLAYER.position[1] -= increment
                    PLAYER.decrement_Moves(increment)

                if (event.key == K_s and PLAYER.moves_left>0):
                    PLAYER.facing = 'DOWN'
                    increment = 1
                    case = 0
                    new_coord = [PLAYER.position[0], PLAYER.position[1] + 1]
                    if new_coord[1] not in range(MAPHEIGHT):
                        increment = 0
                        case = 1
                    elif tilemap[new_coord[1]][new_coord[0]] not in PASSABLE:
                        increment = 0
                        case = 2
                    else:
                        for player in listPLAYERS + listENEMIES:
                            if new_coord == player.position:
                                increment = 0
                                case = 3
                    PLAYER.position[1] += increment
                    PLAYER.decrement_Moves(increment)

                if (event.key == K_RETURN):
                    for player in listPLAYERS:
                        player.decrement_Moves(player.max_moves)

                allDone=True
                for player in listPLAYERS:
                    if(player.moves_left > 0):
                        allDone=False
                        break
                if allDone:
                    phase = 'Attack'
                    for player in listPLAYERS:
                        player.restoreSprite()
            else:
                if pygame.mouse.get_pressed()[2]:
                    new_coord = [int(pygame.mouse.get_pos()[0] / TILESIZE), int(pygame.mouse.get_pos()[1] / TILESIZE)]


    # Display map sprites
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(RescaleImage(textures[tilemap[row][column]]), (column * TILESIZE, row * TILESIZE))

    # Display players and cursor
    for player in listPLAYERS + listENEMIES:
        DISPLAYSURF.blit(RescaleImage(player.sprite), (player.position[0] * TILESIZE, player.position[1] * TILESIZE))
    DISPLAYSURF.blit(RescaleImage(Cursor), (cursorPos[0] * TILESIZE, cursorPos[1] * TILESIZE))

    # Display DEBUG Information
    if DEBUG:
        pygame.draw.rect(DISPLAYSURF,(0,0,0),pygame.Rect(0,MAPHEIGHT * TILESIZE,nextWidth,nextHeight-MAPHEIGHT * TILESIZE))

        placePosition = 5
        Text_Char_Pos = INVFONT.render('Character Position: {}'.format(PLAYER.position) + '  ', True, WHITE, BLACK)
        DISPLAYSURF.blit(Text_Char_Pos, (placePosition, MAPHEIGHT * TILESIZE))

        mouse_coord = [int(pygame.mouse.get_pos()[0] / TILESIZE), int(pygame.mouse.get_pos()[1] / TILESIZE)]
        Text_Mouse_Pos = INVFONT.render('Cursor Position: ' + str(mouse_coord) + '  ', True, WHITE, BLACK)
        DISPLAYSURF.blit(Text_Mouse_Pos, (placePosition, MAPHEIGHT * TILESIZE + 15))

        Text_Button_Facing = INVFONT.render('Direction Facing: ' + str(PLAYER.facing) + 9 * '  ', True, WHITE, BLACK)
        DISPLAYSURF.blit(Text_Button_Facing, (placePosition, MAPHEIGHT * TILESIZE + 30))

        Text_New_Coords = INVFONT.render('Desired Coordinates: ' + str(new_coord) + '  ', True, WHITE, BLACK)
        DISPLAYSURF.blit(Text_New_Coords, (placePosition, MAPHEIGHT * TILESIZE + 45))

        error_cases = {
            1: 'OUT OF BOUNDS',
            2: 'IMPASSABLE TERRAIN',
            3: 'CHARACTER OCCUPYING TILE',
            4: 'MOVEMENT COOLDOWN'
        }
        Text_Valid = INVFONT.render(1000 * ' ', True, BLACK, BLACK)
        if case != 0:
            Text_Valid = INVFONT.render('INVALID COMMAND: {}'.format(error_cases[case]) + 10 * '   ', True, RED, BLACK)
        DISPLAYSURF.blit(Text_Valid, (placePosition, MAPHEIGHT * TILESIZE + 60))

        Text_Char_Selected = INVFONT.render('Currently Selected: ' + PLAYER.name + '        ', True, WHITE, BLACK)
        DISPLAYSURF.blit(Text_Char_Selected, (placePosition, MAPHEIGHT * TILESIZE + 75))

        Text_Hotkey1 = INVFONT.render('1 : {}'.format(HOTKEYS[1].name) + 5 * '  ', True, WHITE, BLACK)
        Text_Hotkey2 = INVFONT.render('2 : {}'.format(HOTKEYS[2].name) + 5 * '  ', True, WHITE, BLACK)
        Text_Hotkey3 = INVFONT.render('3 : {}'.format(HOTKEYS[3].name) + 5 * '  ', True, WHITE, BLACK)
        Text_Hotkey4 = INVFONT.render('4 : {}'.format(HOTKEYS[4].name) + 5 * '  ', True, WHITE, BLACK)
        DISPLAYSURF.blit(Text_Hotkey1, (placePosition + 200, MAPHEIGHT * TILESIZE))
        DISPLAYSURF.blit(Text_Hotkey2, (placePosition + 200, MAPHEIGHT * TILESIZE + 15))
        DISPLAYSURF.blit(Text_Hotkey3, (placePosition + 200, MAPHEIGHT * TILESIZE + 30))
        DISPLAYSURF.blit(Text_Hotkey4, (placePosition + 200, MAPHEIGHT * TILESIZE + 45))

        #		Text_Walk_Cooldown = INVFONT.render('Current Char CD: ' + str(PLAYER.move_current_cd) + (20*' '), True, WHITE, BLACK)
        #		DISPLAYSURF.blit(Text_Walk_Cooldown,(placePosition + 175, MAPHEIGHT*TILESIZE))

        current_terrain = terrains[tilemap[PLAYER.position[1]][PLAYER.position[0]]]
        Text_Terrain = INVFONT.render('Terrain: ' + str(current_terrain) + (9 * '  '), True, WHITE, BLACK)
        DISPLAYSURF.blit(Text_Terrain, (placePosition, MAPHEIGHT * TILESIZE + 90))

    pygame.display.update()
