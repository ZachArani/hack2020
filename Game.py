import pygame, sys
from pygame.locals import *
from time import *
from SacaeMap import *
from Player import *
import time
import os


from operator import itemgetter
import time
from random import shuffle

current_path = os.path.dirname(__file__)

def RescaleImage(image):
    return pygame.transform.scale(image, (TILESIZE, TILESIZE))

def gridDistance(pos1, pos2):
    return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])

def attack(fromCharacter,toCharacter):
    if not fromCharacter.has_attacked:
        toCharacter.takeHit(fromCharacter.giveHit())
        if not toCharacter.isAlive:
            if toCharacter in listENEMIES:
                listENEMIES.remove(toCharacter)
            else:
                listPLAYERS.remove(toCharacter)
    else:
        print("This character can't attack twice!")
def incrementAdjacent(dist,row,column,parent,toCharacter):
    for xinc,yinc in [[1,0],[0,1],[-1,0],[0,-1]]:
        #print(str(xinc)+" "+str(row)+" "+str(xinc+row))
        newPos=[column+yinc,row+xinc]
        good=True
        for character in listPLAYERS+listENEMIES:
            if newPos == character.position and not character.position==toCharacter.position:
                good=False
                break
        if good and row+xinc<len(tilemap) and column+yinc<len(tilemap[0]) and row+xinc>-1 and column+yinc>-1:
            if dist[row+xinc][column+yinc] > dist[row][column] and not tilemap[row+xinc][column+yinc] in NOT_PASSABLE:
                dist[row+xinc][column+yinc]=dist[row][column]+1
                parent[(row+xinc,column+yinc)]=(row,column)

def scuffedDijkstra(fromCharacter, toCharacter):
    parent={}
    startPos = toCharacter.position
    print(startPos)
    endPos=fromCharacter.position

    #set all to infinity
    dist = [[30 for x in range(len(tilemap[0]))] for x in range(len(tilemap))]
    explored=[startPos]
    dist[startPos[1]][startPos[0]]=0


    while len(explored)<len(tilemap)*len(tilemap[0])-len(NOT_PASSABLE):
        minVal=29
        minRow=-1
        minTile=-1
        for row_index in range(len(tilemap)):
            for tile_index in range(len(tilemap[row_index])):
                tile=tilemap[row_index][tile_index]
                distance=dist[row_index][tile_index]
                if not tile in NOT_PASSABLE and not [row_index,tile_index] in explored and not distance ==30:
                    if distance<minVal:
                        minVal=distance
                        minRow=row_index
                        minTile=tile_index
        explored.append([minRow,minTile])
        incrementAdjacent(dist,minRow,minTile,parent,fromCharacter)
        if [minTile,minRow]==endPos:
            for d in dist:
                print(d)
            return [dist[minRow][minTile],parent]
    for d in dist:
        print (d)
    return -1,parent

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
Asparagus = Player('Asparagus', os.path.join(current_path,'CharacterSprites/asparagus.png'), [10, 9], 'Green')
Kohlrabi = Player('Broccoli', os.path.join(current_path,'CharacterSprites/kohlrabi.png'), [9, 9], 'Green')
Sugarcane = Player('Archer', os.path.join(current_path,'CharacterSprites/sugarcane.png'), [8, 9], 'Green')
listPLAYERS = [Asparagus, Kohlrabi, Sugarcane]


Broccoli = Player('Broccoli', os.path.join(current_path,'CharacterSprites/broccoli.png'), [0, 1], 'Red')
Cinnamon = Player('Cinnamon', os.path.join(current_path,'CharacterSprites/cinnamon.png'), [2, 1], 'Red')
Wasabi = Player('Wasabi', os.path.join(current_path,'CharacterSprites/wasabi.png'), [9, 8], 'Red')
listENEMIES = [Broccoli, Cinnamon, Wasabi]


playerAttack = pygame.transform.scale(pygame.image.load(os.path.join(current_path,'CharacterSprites/play_attack.png')),(5*TILESIZE, 2*TILESIZE))
opponentMove = pygame.transform.scale(pygame.image.load(os.path.join(current_path,'CharacterSprites/opp_move.png')), (5*TILESIZE, 2*TILESIZE))

walk_delay = 1
walk_cd = 0

HOTKEYS = {
    1: Asparagus,
    2: Kohlrabi,
    3: Sugarcane
}

# First player is default
PLAYER = listPLAYERS[0]
PLAYER_NAME = listPLAYERS[0].name
playerPos = listPLAYERS[0].position
new_coord = playerPos
clock = pygame.time.Clock()
facing = listPLAYERS[0].facing

# Initialize Cursor to load on Default Character
Cursor = pygame.image.load(os.path.join(current_path,'CharacterSprites/cursor.png'))
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


def redTurn():
    #Moves
    for enemy in listENEMIES:
        closest=None
        for player in listPLAYERS:
            if closest is None:
                closest = player
            else:
                if gridDistance(player.position, enemy.position) < gridDistance(closest.position, enemy.position):
                    closest = player
        answer=scuffedDijkstra(enemy,closest)
        closest_dist=answer[0]
        parent=answer[1]
        #numparentmoves=closest_dist-
        print(closest_dist)
        if closest_dist>1:
            n=min(enemy.max_moves,closest_dist-1)
            for x in range(n):
                nextPos=parent[(enemy.position[1],enemy.position[0])]
                enemy.position=[nextPos[1],nextPos[0]]
                drawCharacters()
                pygame.display.update()
                time.sleep(0.4)
        for player in listPLAYERS:
            if gridDistance(player.position,enemy.position)==1:
                attack(enemy,player)
                enemy.giveHit()
                drawCharacters()
                pygame.display.update()
                time.sleep(0.4)

        #if can_hit go to it
    #Attacks

turn='Green'
def drawCharacters():
    # Display map sprites
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(RescaleImage(textures[tilemap[row][column]]), (column * TILESIZE, row * TILESIZE))

    # Display players and cursor
    for player in listPLAYERS + listENEMIES:
        DISPLAYSURF.blit(RescaleImage(player.sprite), (player.position[0] * TILESIZE, player.position[1] * TILESIZE))
    DISPLAYSURF.blit(RescaleImage(Cursor), (cursorPos[0] * TILESIZE, cursorPos[1] * TILESIZE))
while True:
    if turn == 'Red':
        redTurn()
        turn ='Green'
        time.sleep(1)
        for enemy in listENEMIES:
            enemy.start_turn()
    if not PLAYER in listPLAYERS:
        PLAYER=listPLAYERS[0]
    TILESIZE = int(nextWidth / MAPWIDTH)
    #DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE + const), RESIZABLE)
    #DISPLAYSURF.update()

    mouse_coord = [pygame.mouse.get_pos()[0] / TILESIZE, pygame.mouse.get_pos()[1] / TILESIZE]
    cursorPos = PLAYER.position


    # Movement Cooldown Clock
    turn_clock = clock.tick() / 1000.0
    walk_cd -= turn_clock

    # Get all user events
    events = []
    for e in pygame.event.get():
        events.append(e)

    for event in events:
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


    for event in events:

        if phase == 'Move':
            if pygame.mouse.get_pressed()[0]:
                new_coord = [int(pygame.mouse.get_pos()[0] / TILESIZE), int(pygame.mouse.get_pos()[1] / TILESIZE)]
                for player in listPLAYERS:
                    if player.position == new_coord:
                        PLAYER = player

            if (event.type == KEYDOWN):
            # if (event.key == K_1):
            #     PLAYER = HOTKEYS[1]
            #     cursorPos = PLAYER.position
            #     new_coord = cursorPos
            # if (event.key == K_2):
            #     PLAYER = HOTKEYS[2]
            #     cursorPos = PLAYER.position
            #     new_coord = cursorPos
            # if (event.key == K_3):
            #     PLAYER = HOTKEYS[3]
            #     cursorPos = PLAYER.position
            #     new_coord = cursorPos
            # if (event.key == K_4):
            #     PLAYER = HOTKEYS[4]
            #     cursorPos = PLAYER.position
            #     new_coord = cursorPos
            # Keyboard Inputs
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
                    DISPLAYSURF.blit(playerAttack, (nextWidth/2 -(5*TILESIZE/2), nextHeight/2 - const))
                    pygame.display.update()
                    time.sleep(2)
                    for player in listPLAYERS:
                        player.start_turn()

        else: # Attack phase
            if pygame.mouse.get_pressed()[0]:
                new_coord = [int(pygame.mouse.get_pos()[0] / TILESIZE), int(pygame.mouse.get_pos()[1] / TILESIZE)]
                for player in listPLAYERS:
                    if player.position == new_coord:
                        PLAYER = player
                for enemy in listENEMIES:
                    if enemy.position == new_coord and gridDistance(new_coord, PLAYER.position)<=PLAYER.range:
                        attack(PLAYER, enemy)
            elif (event.type == KEYDOWN):
                if (event.key == K_RETURN):
                    for player in listPLAYERS:
                        player.giveHit()
            allDone = True
            canAttack = False
            for player in listPLAYERS:
                if (not player.has_attacked):
                    allDone = False
                    for enemy in listENEMIES:
                        if gridDistance(player.position, enemy.position) <= player.range:
                            canAttack = True
                            break

            if allDone or not canAttack:
                phase = 'Move'
                turn= 'Red'
                DISPLAYSURF.blit(opponentMove, (nextWidth / 2-(5*TILESIZE/2), nextHeight / 2 - const))
                pygame.display.update()
                time.sleep(2)
                for player in listPLAYERS:
                    player.start_turn()

    # Display map sprites
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(RescaleImage(textures[tilemap[row][column]]), (column * TILESIZE, row * TILESIZE))

    # Display players and cursor
    for player in listPLAYERS + listENEMIES:
        DISPLAYSURF.blit(RescaleImage(player.sprite), (player.position[0] * TILESIZE, player.position[1] * TILESIZE))
    DISPLAYSURF.blit(RescaleImage(Cursor), (cursorPos[0] * TILESIZE, cursorPos[1] * TILESIZE))

    # Display Tooltip Information
    if DEBUG:
        pygame.draw.rect(DISPLAYSURF,(0,0,0),pygame.Rect(0,MAPHEIGHT * TILESIZE,nextWidth,nextHeight-MAPHEIGHT * TILESIZE))

        placePosition = 5

        # Selected Character
        DISPLAYSURF.blit(RescaleImage(PLAYER.sprite), (placePosition, MAPHEIGHT * TILESIZE))
        Text_Name_Coords = INVFONT.render(
            'Name: ' + str(PLAYER.name) + '  ', True, WHITE, BLACK)
        DISPLAYSURF.blit(Text_Name_Coords, (placePosition + 75, MAPHEIGHT * TILESIZE))
        Text_Health_Coords = INVFONT.render(
            'Health: ' + str(PLAYER.health) + '/' + str(PLAYER.max_health) + '  ', True, WHITE, BLACK)
        DISPLAYSURF.blit(Text_Health_Coords, (placePosition + 75, MAPHEIGHT * TILESIZE + 15))
        Text_Move_Coords = INVFONT.render(
            'Moves: ' + str(PLAYER.moves_left) + '/' + str(PLAYER.max_moves) + '  ', True, WHITE, BLACK)
        DISPLAYSURF.blit(Text_Move_Coords, (placePosition + 75, MAPHEIGHT * TILESIZE + 30))
        Text_Range_Coords = INVFONT.render(
            'Range: ' + str(PLAYER.range) + '  ', True, WHITE, BLACK)
        DISPLAYSURF.blit(Text_Range_Coords, (placePosition + 75, MAPHEIGHT * TILESIZE + 45))
        Text_Damage_Coords = INVFONT.render(
            'Damage: ' + str(PLAYER.damage) + '  ', True, WHITE, BLACK)
        DISPLAYSURF.blit(Text_Damage_Coords, (placePosition + 75, MAPHEIGHT * TILESIZE + 60))

        # Moused over character
        new_coord = [int(pygame.mouse.get_pos()[0] / TILESIZE), int(pygame.mouse.get_pos()[1] / TILESIZE)]
        for player in listPLAYERS + listENEMIES:
            if new_coord == player.position:
                DISPLAYSURF.blit(RescaleImage(player.sprite), (placePosition + 275, MAPHEIGHT * TILESIZE))
                Text_Name_Coords = INVFONT.render(
                    'Name: ' + str(player.name) + '  ', True, WHITE, BLACK)
                DISPLAYSURF.blit(Text_Name_Coords, (placePosition + 350, MAPHEIGHT * TILESIZE))
                Text_Health_Coords = INVFONT.render('Health: ' + str(player.health) + '/' + str(player.max_health) + '  ', True, WHITE, BLACK)
                DISPLAYSURF.blit(Text_Health_Coords, (placePosition + 350, MAPHEIGHT * TILESIZE + 15))
                Text_Move_Coords = INVFONT.render('Moves: ' + str(player.moves_left) + '/' + str(player.max_moves) + '  ', True, WHITE, BLACK)
                DISPLAYSURF.blit(Text_Move_Coords, (placePosition + 350, MAPHEIGHT * TILESIZE + 30))
                Text_Range_Coords = INVFONT.render(
                    'Range: ' + str(player.range) + '  ', True, WHITE, BLACK)
                DISPLAYSURF.blit(Text_Range_Coords, (placePosition + 350, MAPHEIGHT * TILESIZE + 45))
                Text_Damage_Coords = INVFONT.render(
                    'Damage: ' + str(player.damage) + '  ', True, WHITE, BLACK)
                DISPLAYSURF.blit(Text_Damage_Coords, (placePosition + 350, MAPHEIGHT * TILESIZE + 60))



        error_cases = {
            1: 'OUT OF BOUNDS',
            2: 'IMPASSABLE TERRAIN',
            3: 'CHARACTER OCCUPYING TILE',
            4: 'MOVEMENT COOLDOWN'
        }
        Text_Valid = INVFONT.render(1000 * ' ', True, BLACK, BLACK)
        if case != 0:
            Text_Valid = INVFONT.render('INVALID COMMAND: {}'.format(error_cases[case]) + 10 * '   ', True, RED, BLACK)
        DISPLAYSURF.blit(Text_Valid, (placePosition, MAPHEIGHT * TILESIZE + 90))

        # Text_Char_Selected = INVFONT.render('Currently Selected: ' + PLAYER.name + '        ', True, WHITE, BLACK)
        # DISPLAYSURF.blit(Text_Char_Selected, (placePosition, MAPHEIGHT * TILESIZE + 75))

        # Text_Hotkey1 = INVFONT.render('1 : {}'.format(HOTKEYS[1].name) + 5 * '  ', True, WHITE, BLACK)
        # Text_Hotkey2 = INVFONT.render('2 : {}'.format(HOTKEYS[2].name) + 5 * '  ', True, WHITE, BLACK)
        # Text_Hotkey3 = INVFONT.render('3 : {}'.format(HOTKEYS[3].name) + 5 * '  ', True, WHITE, BLACK)
        # Text_Hotkey4 = INVFONT.render('4 : {}'.format(HOTKEYS[4].name) + 5 * '  ', True, WHITE, BLACK)
        # DISPLAYSURF.blit(Text_Hotkey1, (placePosition + 200, MAPHEIGHT * TILESIZE))
        # DISPLAYSURF.blit(Text_Hotkey2, (placePosition + 200, MAPHEIGHT * TILESIZE + 15))
        # DISPLAYSURF.blit(Text_Hotkey3, (placePosition + 200, MAPHEIGHT * TILESIZE + 30))
        # DISPLAYSURF.blit(Text_Hotkey4, (placePosition + 200, MAPHEIGHT * TILESIZE + 45))

        #		Text_Walk_Cooldown = INVFONT.render('Current Char CD: ' + str(PLAYER.move_current_cd) + (20*' '), True, WHITE, BLACK)
        #		DISPLAYSURF.blit(Text_Walk_Cooldown,(placePosition + 175, MAPHEIGHT*TILESIZE))

    pygame.display.update()
