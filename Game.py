import pygame, sys
from pygame.locals import *
from time import *
from SacaeMap import *
from Player import *
import time
import os
import pygameMenu
import questionMenu as menu

from operator import itemgetter
import time
from random import shuffle

current_path = os.path.dirname(__file__)

Questions = {
    'Who is the mother of programming?': [['Ada Lovelace','Grace Hopper','Kim Gordon','Wendy Carlos'],1],
    'Who created the Analytical Engine?': [['Alan Turing','Charles Babbage','Steve Jobs','Ada Lovelace'],2],
    'What was the name of the first digital computer?': [['ABC','ENIVAC','UNIVAC','Indigo'],1],
    'Who came up with the idea of a machine that could compute anything which is computable?': [['Charles Babbage','Ada Lovelace','Alan Turing','Albert Einstein'],1],
    'What is the lowest level programming language?': [['Assembly','C','Java','FORTRAN'],1],
    'What was the first commercial computer?': [['ABC','ENIVAC','Xerox Alto', 'UNIVAC'], 4],
    'Who developed the concept of Machine Independent Programming?': [['Grace Hopper','Ada Lovelace','Dennis Ritiche','Alan Turing'],1],
    'When was the internet created?': [['1960s','1970s','1980s','1990s'], 1],
    'Who created the computer chip and was awarded with a Nobel Prize in Physics?': [['Alan Turing','Bill Gates','Jack Kilby','Ken Thompson'],3],
    'Where was UNIX developed?': [['Bell Laboratories','Xerox Laboratories','BBC Laboratories','Microsoft'],1],
    'What was the first portable computer?': [['IBM 5100','Osborne 1','IBN 5100','Macintosh'],1],
    'Who created the C programming language?': [['Ken Thompson','Grace Hopper','Dennis Ritchie','Steve Jobs'], 3],
    'What company created the first Object Oriented Programming language?': [['Apple,','Bell','Sun Microsystems', 'Xerox'], 4],
    'First personal computer with a graphical user interface?': [['Xerox Alto','Macintosh','IBN 5100','Indigo'], 1],
    'When was the first dot com domain registered?': [['1993','1995','1988', '1985'], 4],
    'What was the name of the AI who beat Grandmasters in chess?': [['ChessMind','Open King','Deep Blue','Master AI'],3]
}



class Question(object):
    def __init__(self, question, answers, correctAnswer):
        selected = False
        selectedNo = 0
        self.questionFont = pygame.font.SysFont('FreeSerif', 35)
        self.answerFont = pygame.font.SysFont('FreeSerif', 25)
        self.question = fill_gradient(DISPLAYSURF, color=(80, 108, 250), gradient=(16, 12, 97),
                      rect=pygame.Rect(5, DISPLAYSURF.get_rect().centery * 0.85, DISPLAYSURF.get_rect().width - 12,
                                       100), forward=False)
        DISPLAYSURF.blit(self.questionFont.render(question, 1, (255, 255, 255)), (10, DISPLAYSURF.get_rect().centery * 0.85))

        self.a1 = fill_gradient(DISPLAYSURF, color=(80, 108, 250), gradient=(16, 12, 97),
                      rect=pygame.Rect(5, DISPLAYSURF.get_rect().centery * 1.10, DISPLAYSURF.get_rect().width * 0.48,
                                       80), forward=False)
        DISPLAYSURF.blit(self.answerFont.render(answers[0], 1, (255, 255, 255)), (10, DISPLAYSURF.get_rect().centery * 1.10))

        self.a2 = fill_gradient(DISPLAYSURF, color=(80, 108, 250), gradient=(16, 12, 97),
                      rect=pygame.Rect(DISPLAYSURF.get_rect().width * 0.5, DISPLAYSURF.get_rect().centery * 1.10,
                                       DISPLAYSURF.get_rect().width * 0.49, 80), forward=False)
        DISPLAYSURF.blit(self.answerFont.render(answers[1], 1, (255, 255, 255)), (DISPLAYSURF.get_rect().width * 0.505, DISPLAYSURF.get_rect().centery * 1.10))


        self.a3 = fill_gradient(DISPLAYSURF, color=(80, 108, 250), gradient=(16, 12, 97),
                      rect=pygame.Rect(5, DISPLAYSURF.get_rect().centery * 1.30, DISPLAYSURF.get_rect().width * 0.48,
                                       80), forward=False)
        DISPLAYSURF.blit(self.answerFont.render(answers[2], 1, (255, 255, 255)), (10, DISPLAYSURF.get_rect().centery * 1.30))

        self.a4 = fill_gradient(DISPLAYSURF, color=(80, 108, 250), gradient=(16, 12, 97),
                      rect=pygame.Rect(DISPLAYSURF.get_rect().width * 0.5, DISPLAYSURF.get_rect().centery * 1.30,
                                       DISPLAYSURF.get_rect().width * 0.49, 80), forward=False)
        DISPLAYSURF.blit(self.answerFont.render(answers[3], 1, (255, 255, 255)), (DISPLAYSURF.get_rect().width * 0.505, DISPLAYSURF.get_rect().centery * 1.30))
        while not selected:
            if self.a1.collidepoint(pygame.mouse.get_pos()):
                self.a1 = fill_gradient(DISPLAYSURF, color=(235, 64, 52), gradient=(158, 27, 17),
                                        rect=pygame.Rect(5, DISPLAYSURF.get_rect().centery * 1.10,
                                                         DISPLAYSURF.get_rect().width * 0.48,
                                                         80), forward=False)
                DISPLAYSURF.blit(self.answerFont.render("Ada Lovelace", 1, (255, 255, 255)),
                                 (10, DISPLAYSURF.get_rect().centery * 1.10))
                if pygame.mouse.get_pressed()[0]:
                    selectedNo = 1
                    selected = True
            else:
                self.a1 = fill_gradient(DISPLAYSURF, color=(80, 108, 250), gradient=(16, 12, 97),
                                        rect=pygame.Rect(5, DISPLAYSURF.get_rect().centery * 1.10,
                                                         DISPLAYSURF.get_rect().width * 0.48,
                                                         80), forward=False)
                DISPLAYSURF.blit(self.answerFont.render("Ada Lovelace", 1, (255, 255, 255)),
                                 (10, DISPLAYSURF.get_rect().centery * 1.10))
            if self.a2.collidepoint(pygame.mouse.get_pos()):
                self.a2 = fill_gradient(DISPLAYSURF, color=(235, 64, 52), gradient=(158, 27, 17),
                                        rect=pygame.Rect(DISPLAYSURF.get_rect().width * 0.5,
                                                         DISPLAYSURF.get_rect().centery * 1.10,
                                                         DISPLAYSURF.get_rect().width * 0.49, 80), forward=False)
                DISPLAYSURF.blit(self.answerFont.render("Grace Hopper", 1, (255, 255, 255)),
                                 (DISPLAYSURF.get_rect().width * 0.505, DISPLAYSURF.get_rect().centery * 1.10))
                if pygame.mouse.get_pressed()[0]:
                    selectedNo = 2
                    selected = True
            else:
                self.a2 = fill_gradient(DISPLAYSURF, color=(80, 108, 250), gradient=(16, 12, 97),
                                        rect=pygame.Rect(DISPLAYSURF.get_rect().width * 0.5,
                                                         DISPLAYSURF.get_rect().centery * 1.10,
                                                         DISPLAYSURF.get_rect().width * 0.49, 80), forward=False)
                DISPLAYSURF.blit(self.answerFont.render("Grace Hopper", 1, (255, 255, 255)),
                                 (DISPLAYSURF.get_rect().width * 0.505, DISPLAYSURF.get_rect().centery * 1.10))
            if self.a3.collidepoint(pygame.mouse.get_pos()):
                self.a3 = fill_gradient(DISPLAYSURF, color=(235, 64, 52), gradient=(158, 27, 17),
                                        rect=pygame.Rect(5, DISPLAYSURF.get_rect().centery * 1.30,
                                                         DISPLAYSURF.get_rect().width * 0.48,
                                                         80), forward=False)
                DISPLAYSURF.blit(self.answerFont.render("Kim Gordon", 1, (255, 255, 255)),
                                 (10, DISPLAYSURF.get_rect().centery * 1.30))
                if pygame.mouse.get_pressed()[0]:
                    selectedNo = 3
                    selected = True
            else:
                self.a3 = fill_gradient(DISPLAYSURF, color=(80, 108, 250), gradient=(16, 12, 97),
                                        rect=pygame.Rect(5, DISPLAYSURF.get_rect().centery * 1.30,
                                                         DISPLAYSURF.get_rect().width * 0.48,
                                                         80), forward=False)
                DISPLAYSURF.blit(self.answerFont.render("Kim Gordon", 1, (255, 255, 255)),
                                 (10, DISPLAYSURF.get_rect().centery * 1.30))
            if self.a4.collidepoint(pygame.mouse.get_pos()):
                self.a4 = fill_gradient(DISPLAYSURF, color=(235, 64, 52), gradient=(158, 27, 17),
                                        rect=pygame.Rect(DISPLAYSURF.get_rect().width * 0.5,
                                                         DISPLAYSURF.get_rect().centery * 1.30,
                                                         DISPLAYSURF.get_rect().width * 0.49, 80), forward=False)
                DISPLAYSURF.blit(self.answerFont.render("Wendy Carlos", 1, (255, 255, 255)),
                                 (DISPLAYSURF.get_rect().width * 0.505, DISPLAYSURF.get_rect().centery * 1.30))
                if pygame.mouse.get_pressed()[0]:
                    selectedNo = 4
                    selected = True
            else:
                self.a4 = fill_gradient(DISPLAYSURF, color=(80, 108, 250), gradient=(16, 12, 97),
                                        rect=pygame.Rect(DISPLAYSURF.get_rect().width * 0.5,
                                                         DISPLAYSURF.get_rect().centery * 1.30,
                                                         DISPLAYSURF.get_rect().width * 0.49, 80), forward=False)
                DISPLAYSURF.blit(self.answerFont.render("Wendy Carlos", 1, (255, 255, 255)),
                                 (DISPLAYSURF.get_rect().width * 0.505, DISPLAYSURF.get_rect().centery * 1.30))
            pygame.event.pump()
            pygame.display.update()
        self.isCorrect = (selectedNo == correctAnswer)


pygame.mixer.init()
pygame.mixer.music.load(os.path.join(current_path, "Music/battletime.ogg"))
pygame.mixer.music.play(-1);


def RescaleImage(image):
    return pygame.transform.scale(image, (TILESIZE, TILESIZE))

def gridDistance(pos1, pos2):
    return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])

def donothing():
    x=2

def fill_gradient(surface, color, gradient, rect=None, vertical=True, forward=True):
    """fill a surface with a gradient pattern
    Parameters:
    color -> starting color
    gradient -> final color
    rect -> area to fill; default is surface's rect
    vertical -> True=vertical; False=horizontal
    forward -> True=forward; False=reverse

    Pygame recipe: http://www.pygame.org/wiki/GradientCode
    """
    if rect is None: rect = surface.get_rect()
    x1, x2 = rect.left, rect.right
    y1, y2 = rect.top, rect.bottom
    if vertical:
        h = y2 - y1
    else:
        h = x2 - x1
    if forward:
        a, b = color, gradient
    else:
        b, a = color, gradient
    rate = (
        float(b[0] - a[0]) / h,
        float(b[1] - a[1]) / h,
        float(b[2] - a[2]) / h
    )
    fn_line = pygame.draw.line
    if vertical:
        for line in range(y1, y2):
            color = (
                min(max(a[0] + (rate[0] * (line - y1)), 0), 255),
                min(max(a[1] + (rate[1] * (line - y1)), 0), 255),
                min(max(a[2] + (rate[2] * (line - y1)), 0), 255)
            )
            fn_line(surface, color, (x1, line), (x2, line))
    else:
        for col in range(x1, x2):
            color = (
                min(max(a[0] + (rate[0] * (col - x1)), 0), 255),
                min(max(a[1] + (rate[1] * (col - x1)), 0), 255),
                min(max(a[2] + (rate[2] * (col - x1)), 0), 255)
            )
            fn_line(surface, color, (col, y1), (col, y2))
    return rect


def attack(fromCharacter,toCharacter):
    menuSurface = pygame.Surface((240,180))
    menuSurface.fill((40,40,40))
    print(DISPLAYSURF.blit(pygame.image.load('Textures/bleachers.png'), [80, 10]))
    pygame.display.update()
    #testMenu = pygameMenu.Menu(surface=DISPLAYSURF, bgfun=test_background, font=pygameMenu.font.FONT_HELVETICA, font_color=(0, 0, 0), font_size=25, window_height=200, window_width=400, title="test")

   # menu.main()
def attack(fromCharacter,toCharacter):
    #menu.main()
    if not fromCharacter.has_attacked:
        toCharacter.takeHit(fromCharacter.giveHit())
        if not toCharacter.isAlive:
            if toCharacter in listENEMIES:
                listENEMIES.remove(toCharacter)
            else:
                listPLAYERS.remove(toCharacter)
        drawCharacters()
        pygame.display.update()

    else:
        print("This character can't attack twice!")

def incrementAdjacent(dist,row,column,parent,toCharacter,fromCharacter):
    for xinc,yinc in [[1,0],[0,1],[-1,0],[0,-1]]:
        #print(str(xinc)+" "+str(row)+" "+str(xinc+row))
        newPos=[column+yinc,row+xinc]
        good=True
        for character in listPLAYERS+listENEMIES:
            if newPos == character.position and not character.position==toCharacter.position and not character.position==fromCharacter.position:
                good=False
                break
        if good and row+xinc<len(tilemap) and column+yinc<len(tilemap[0]) and row+xinc>-1 and column+yinc>-1:
            if dist[row+xinc][column+yinc] > dist[row][column] and not tilemap[row+xinc][column+yinc] in NOT_PASSABLE:
                dist[row+xinc][column+yinc]=dist[row][column]+1
                parent[(row+xinc,column+yinc)]=(row,column)


def scuffedDijkstra(fromCharacter, toCharacter):

    parent={}
    startPos = toCharacter.position
    #print(startPos)
    endPos=fromCharacter.position

    #set all to infinity
    dist = [[30 for x in range(len(tilemap[0]))] for x in range(len(tilemap))]
    explored=[startPos]

    dist[startPos[1]][startPos[0]]=0
    incrementAdjacent(dist,startPos[1],startPos[0],parent,toCharacter,fromCharacter)
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
        incrementAdjacent(dist,minRow,minTile,parent,toCharacter,fromCharacter)
        if [minTile,minRow]==endPos:

            return [dist[minRow][minTile],parent]

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
Asparagus = Player('Asparaguy', os.path.join(current_path,'CharacterSprites/asparagus.png'), [10, 9], 'Green')
Kohlrabi = Player('Kohlrabi', os.path.join(current_path,'CharacterSprites/kohlrabi.png'), [9, 9], 'Green')
Sugarcane = Player('Sugarcane', os.path.join(current_path,'CharacterSprites/sugarcane.png'), [8, 9], 'Green')
listPLAYERS = [Asparagus, Kohlrabi, Sugarcane]


Broccoli = Player('Broccoli', os.path.join(current_path,'CharacterSprites/broccoli.png'), [2, 1], 'Red')
Cinnamon = Player('Cinnamon', os.path.join(current_path,'CharacterSprites/cinnamon.png'), [9, 1], 'Red')
Wasabi = Player('Wasabi', os.path.join(current_path,'CharacterSprites/wasabi.png'), [0, 1], 'Red',range=3)
listENEMIES = [Broccoli, Cinnamon, Wasabi]


playerAttack = pygame.transform.scale(pygame.image.load(os.path.join(current_path,'CharacterSprites/play_attack.png')),(5*TILESIZE, 2*TILESIZE))
playerMove = pygame.transform.scale(pygame.image.load(os.path.join(current_path,'CharacterSprites/play_move.png')),(5*TILESIZE, 2*TILESIZE))
opponentMove = pygame.transform.scale(pygame.image.load(os.path.join(current_path,'CharacterSprites/opp_move.png')), (5*TILESIZE, 2*TILESIZE))
opponentAttack = pygame.transform.scale(pygame.image.load(os.path.join(current_path,'CharacterSprites/opp_attack.png')), (5*TILESIZE, 2*TILESIZE))
youWin = pygame.transform.scale(pygame.image.load(os.path.join(current_path,'CharacterSprites/you_win.png')), (5*TILESIZE, 2*TILESIZE))
youLose = pygame.transform.scale(pygame.image.load(os.path.join(current_path,'CharacterSprites/you_lose.png')), (5*TILESIZE, 2*TILESIZE))


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
    testFont = pygame.font.SysFont('FreeSerif', 45, italic=True)
    questionFont = pygame.font.SysFont('FreeSerif', 25)

else:
    const = 0
# Create display surface
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE + const), RESIZABLE)
nextWidth=MAPWIDTH * TILESIZE
nextHeight= MAPHEIGHT * TILESIZE + const


def redTurn():
    #Move
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
            n=min(enemy.max_moves,(closest_dist-1-(closest.max_moves+closest.range))%40)
            for x in range(n):
                nextPos=parent[(enemy.position[1],enemy.position[0])]
                if not [nextPos[1],nextPos[0]] == closest.position:
                    enemy.position=[nextPos[1],nextPos[0]]
                drawCharacters()
                pygame.display.update()
                time.sleep(0.4)
    text = testFont.render("OPPONENT ATTACK PHASE", 1, (250, 80, 94))
    textpos = text.get_rect()
    textpos.centerx = DISPLAYSURF.get_rect().centerx
    textpos.centery = DISPLAYSURF.get_rect().centery * 0.75
    DISPLAYSURF.blit(text, textpos)
    #DISPLAYSURF.blit(opponentAttack, (nextWidth / 2 - (5 * TILESIZE / 2), nextHeight / 2 - const))
    pygame.display.update()
    time.sleep(.5)
    for enemy in listENEMIES:
        for player in listPLAYERS:
            if gridDistance(player.position,enemy.position)==1:
                attack(enemy,player)
                enemy.giveHit()
                drawCharacters()
                pygame.display.update()
                time.sleep(0.4)
    text = testFont.render("PLAYER MOVE PHASE", 1, (80, 108, 250))
    textpos = text.get_rect()
    textpos.centerx = DISPLAYSURF.get_rect().centerx
    textpos.centery = DISPLAYSURF.get_rect().centery * 0.75
    DISPLAYSURF.blit(text, textpos)

    #DISPLAYSURF.blit(playerMove, (nextWidth / 2 - (5 * TILESIZE / 2), nextHeight / 2 - const))
    pygame.display.update()
    time.sleep(2)
    if len(listPLAYERS) != 0:
        drawCharacters()
        DISPLAYSURF.blit(playerMove, (nextWidth / 2 - (5 * TILESIZE / 2), nextHeight / 2 - const))
        pygame.display.update()
        time.sleep(.4)

        #if can_hit go to it
    #Attacks

turn='Green'
def drawCharacters():
    # Display map sprites
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(RescaleImage(textures[tilemap[row][column]]), (column * TILESIZE, row * TILESIZE))

    # Display players and cursor
    DISPLAYSURF.blit(RescaleImage(Cursor), (cursorPos[0] * TILESIZE, cursorPos[1] * TILESIZE))
    for player in listPLAYERS + listENEMIES:
        DISPLAYSURF.blit(RescaleImage(player.sprite), (player.position[0] * TILESIZE, player.position[1] * TILESIZE))
while True:

    if len(listENEMIES) == 0:
        DISPLAYSURF.blit(youWin, (nextWidth / 2 - (5 * TILESIZE / 2), nextHeight / 2 - const))
        pygame.display.update()
        time.sleep(5)
        break

    elif len(listPLAYERS) == 0:
        DISPLAYSURF.blit(youLose, (nextWidth / 2 - (5 * TILESIZE / 2), nextHeight / 2 - const))
        pygame.display.update()
        time.sleep(5)
        break

    if turn == 'Red':
        redTurn()
        turn ='Green'
        time.sleep(1)
        for enemy in listENEMIES:
            enemy.start_turn()
    if not PLAYER in listPLAYERS and len(listPLAYERS) != 0:
        PLAYER=listPLAYERS[0]
    TILESIZE = int(nextWidth / MAPWIDTH)

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
                    drawCharacters()
                    pygame.display.update()
                    phase = 'Attack'



                    text = testFont.render("PLAYER ATTACK PHASE", 1, (80, 108, 250))
                    textpos = text.get_rect()
                    textpos.centerx = DISPLAYSURF.get_rect().centerx
                    textpos.centery = DISPLAYSURF.get_rect().centery * 0.75
                    DISPLAYSURF.blit(text, textpos)

                    correctAnswer=Question('When was the first dot com domain registered?', ['1993', '1995', '1988', '1985'], 1).isCorrect
                    print(correctAnswer)
                  #  DISPLAYSURF.blit(playerAttack, (nextWidth/2 -(5*TILESIZE/2), nextHeight/2 - const))
                    pygame.display.update()
                    time.sleep(.5)
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
                text = testFont.render("OPPONENT MOVE PHASE", 1, (250, 80, 94))
                textpos = text.get_rect()
                textpos.centerx = DISPLAYSURF.get_rect().centerx
                textpos.centery = DISPLAYSURF.get_rect().centery * 0.75
                DISPLAYSURF.blit(text, textpos)
                #DISPLAYSURF.blit(opponentMove, (nextWidth / 2-(5*TILESIZE/2), nextHeight / 2 - const))
                pygame.display.update()
                time.sleep(2)
                if len(listENEMIES) != 0:
                    DISPLAYSURF.blit(opponentMove, (nextWidth / 2-(5*TILESIZE/2), nextHeight / 2 - const))
                    pygame.display.update()
                    time.sleep(.5)
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
        paperDialog = pygame.transform.scale(pygame.image.load(os.path.join(current_path, 'Textures/paper_dialog.png')), (nextWidth, nextHeight - MAPHEIGHT * TILESIZE))
        # pygame.draw.rect(DISPLAYSURF,(0,0,0),pygame.Rect(0,MAPHEIGHT * TILESIZE,nextWidth,nextHeight-MAPHEIGHT * TILESIZE))
        DISPLAYSURF.blit(paperDialog, (0,MAPHEIGHT * TILESIZE))

        placePosition = 5

        # Selected Character
        DISPLAYSURF.blit(RescaleImage(PLAYER.sprite), (placePosition, MAPHEIGHT * TILESIZE + 15))
        Text_Name_Coords = INVFONT.render(
            'Name: ' + str(PLAYER.name) + '  ', True, BLACK)
        DISPLAYSURF.blit(Text_Name_Coords, (placePosition + 75, MAPHEIGHT * TILESIZE + 15))
        Text_Health_Coords = INVFONT.render(
            'Health: ' + str(PLAYER.health) + '/' + str(PLAYER.max_health) + '  ', True, BLACK)
        DISPLAYSURF.blit(Text_Health_Coords, (placePosition + 75, MAPHEIGHT * TILESIZE + 30))
        Text_Move_Coords = INVFONT.render(
            'Moves: ' + str(PLAYER.moves_left) + '/' + str(PLAYER.max_moves) + '  ', True, BLACK)
        DISPLAYSURF.blit(Text_Move_Coords, (placePosition + 75, MAPHEIGHT * TILESIZE + 45))
        Text_Range_Coords = INVFONT.render(
            'Range: ' + str(PLAYER.range) + '  ', True, BLACK)
        DISPLAYSURF.blit(Text_Range_Coords, (placePosition + 75, MAPHEIGHT * TILESIZE + 60))
        Text_Damage_Coords = INVFONT.render(
            'Damage: ' + str(PLAYER.damage) + '  ', True, BLACK)
        DISPLAYSURF.blit(Text_Damage_Coords, (placePosition + 75, MAPHEIGHT * TILESIZE + 75))

        # Moused over character
        new_coord = [int(pygame.mouse.get_pos()[0] / TILESIZE), int(pygame.mouse.get_pos()[1] / TILESIZE)]
        for player in listPLAYERS + listENEMIES:
            if new_coord == player.position:
                DISPLAYSURF.blit(RescaleImage(player.sprite), (placePosition + 275, MAPHEIGHT * TILESIZE + 15))
                Text_Name_Coords = INVFONT.render(
                    'Name: ' + str(player.name) + '  ', True, BLACK)
                DISPLAYSURF.blit(Text_Name_Coords, (placePosition + 350, MAPHEIGHT * TILESIZE + 15))
                Text_Health_Coords = INVFONT.render('Health: ' + str(player.health) + '/' + str(player.max_health) + '  ', True, BLACK)
                DISPLAYSURF.blit(Text_Health_Coords, (placePosition + 350, MAPHEIGHT * TILESIZE + 30))
                Text_Move_Coords = INVFONT.render('Moves: ' + str(player.moves_left) + '/' + str(player.max_moves) + '  ', True, BLACK)
                DISPLAYSURF.blit(Text_Move_Coords, (placePosition + 350, MAPHEIGHT * TILESIZE + 45))
                Text_Range_Coords = INVFONT.render(
                    'Range: ' + str(player.range) + '  ', True, BLACK)
                DISPLAYSURF.blit(Text_Range_Coords, (placePosition + 350, MAPHEIGHT * TILESIZE + 60))
                Text_Damage_Coords = INVFONT.render(
                    'Damage: ' + str(player.damage) + '  ', True, BLACK)
                DISPLAYSURF.blit(Text_Damage_Coords, (placePosition + 350, MAPHEIGHT * TILESIZE + 75))

                #Do blue stuff
                blue_image = pygame.Surface((TILESIZE,TILESIZE))
                blue_image.set_alpha(45)
                blue_image.fill((0,0,180))
                red_image = pygame.Surface((TILESIZE, TILESIZE))
                red_image.set_alpha(45)
                red_image.fill((180, 0, 0))
                for row in range(MAPHEIGHT):
                    for column in range(MAPWIDTH):
                        if gridDistance(player.position, [column,row])<= player.moves_left:
                            DISPLAYSURF.blit(blue_image,
                                         (column * TILESIZE, row * TILESIZE))
                        elif gridDistance(player.position, [column,row])<= player.moves_left+player.range:
                            DISPLAYSURF.blit(red_image,
                                         (column * TILESIZE, row * TILESIZE))



        error_cases = {
            1: 'OUT OF BOUNDS',
            2: 'IMPASSABLE TERRAIN',
            3: 'CHARACTER OCCUPYING TILE',
            4: 'MOVEMENT COOLDOWN'
        }
        Text_Valid = INVFONT.render(1000 * ' ', True, BLACK)
        if case != 0:
            Text_Valid = INVFONT.render('INVALID COMMAND: {}'.format(error_cases[case]) + 10 * '   ', True, RED, BLACK)
        DISPLAYSURF.blit(Text_Valid, (placePosition, MAPHEIGHT * TILESIZE + 105))
    pygame.display.update()
