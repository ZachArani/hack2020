import pygame, sys
import os


current_path = os.path.dirname(__file__)

# Constants representing different resouces
COURT = 0
OUTERCOURT = 1
CORNER = 2
HALFCOURT = 3
TLINE = 4
EDGE = 5
RIGHTEDGE = 6
BOTTOMEDGE = 7
LEFTEDGE = 8
BOTTOMLINE = 9
TRCORNER = 10
BRCORNER = 11
BLCORNER = 12
LEDGE1 = 13
LEDGE2 = 14
LEDGE3 = 15
HUT = 16

terrains = {
    0: 'COURT',
    1: 'OUTERCOURT',
    2: 'CORNER',
    3: 'HALFCOURT',
    4: 'TLINE',
    5: 'EDGE',
    6: 'RIGHTEDGE',
    7: 'BOTTOMEDGE',
    8: 'LEFTEDGE',
    9: 'BOTTOMLINE',
    10: 'TRCORNER',
    11: 'BRCORNER',
    12: 'BLCORNER',
    13: 'LEDGE1',
    14: 'LEDGE2',
    15: 'LEDGE3',
    16: 'HUT'
}

# Dictionary linking resouces to textures
textures = {
    COURT: pygame.image.load(os.path.join(current_path,'Textures/court.png')),
    OUTERCOURT: pygame.image.load(os.path.join(current_path,'Textures/outercourt.png')),
    CORNER: pygame.image.load(os.path.join(current_path,'Textures/corner.png')),
    HALFCOURT: pygame.image.load(os.path.join(current_path,'Textures/halfcourt.png')),
    TLINE: pygame.image.load(os.path.join(current_path,'Textures/tline.png')),
    EDGE: pygame.image.load(os.path.join(current_path,'Textures/edge.png')),
    LEFTEDGE: pygame.transform.rotate(pygame.image.load(os.path.join(current_path,'Textures/edge.png')), 90),
    BOTTOMEDGE: pygame.transform.rotate(pygame.image.load(os.path.join(current_path,'Textures/edge.png')), 180),
    RIGHTEDGE: pygame.transform.rotate(pygame.image.load(os.path.join(current_path,'Textures/edge.png')), 270),
    BOTTOMLINE: pygame.transform.rotate(pygame.image.load(os.path.join(current_path,'Textures/tline.png')), 180),
    TRCORNER: pygame.transform.rotate(pygame.image.load(os.path.join(current_path,'Textures/corner.png')), 270),
    BRCORNER: pygame.transform.rotate(pygame.image.load(os.path.join(current_path,'Textures/corner.png')), 180),
    BLCORNER: pygame.transform.rotate(pygame.image.load(os.path.join(current_path,'Textures/corner.png')), 90),
    LEDGE1: pygame.image.load(os.path.join(current_path,'Textures/ledge1.png')),
    LEDGE2: pygame.image.load(os.path.join(current_path,'Textures/ledge2.png')),
    LEDGE3: pygame.image.load(os.path.join(current_path,'Textures/ledge3.png')),
    HUT: pygame.image.load(os.path.join(current_path,'Textures/hut.png'))
}

# Tilemap
tilemap = [
    [OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT],
    [OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT],
    [OUTERCOURT, CORNER, EDGE, EDGE, EDGE, TLINE, EDGE, EDGE, EDGE, TRCORNER, OUTERCOURT],
    [OUTERCOURT, LEFTEDGE, COURT, COURT, COURT, HALFCOURT, COURT, COURT, COURT, RIGHTEDGE, OUTERCOURT],
    [OUTERCOURT, LEFTEDGE, COURT, COURT, COURT, HALFCOURT, COURT, COURT, COURT, RIGHTEDGE, OUTERCOURT],
    [OUTERCOURT, LEFTEDGE, COURT, COURT, COURT, HALFCOURT, COURT, COURT, COURT, RIGHTEDGE, OUTERCOURT],
    [OUTERCOURT, LEFTEDGE, COURT, COURT, COURT, HALFCOURT, COURT, COURT, COURT, RIGHTEDGE, OUTERCOURT],
    [OUTERCOURT, BLCORNER, BOTTOMEDGE, BOTTOMEDGE, BOTTOMEDGE, BOTTOMLINE, BOTTOMEDGE, BOTTOMEDGE, BOTTOMEDGE, BRCORNER, OUTERCOURT],
    [OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT],
    [OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT]
]

# Walls
PASSABLE = [COURT,OUTERCOURT,CORNER,HALFCOURT,TLINE,EDGE,RIGHTEDGE,BOTTOMEDGE,LEFTEDGE,BOTTOMLINE,TRCORNER,BRCORNER,BLCORNER]
NOT_PASSABLE = []

# Game Dimensions
TILESIZE = 64
MAPWIDTH = 11
MAPHEIGHT = 10
