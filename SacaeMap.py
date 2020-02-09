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
BLEACHERS = 13
BLEACHERSUPSIDE = 14
HOOPCOURT = 15
HOOPCOURTUPSIDE = 16
HOOPCOURTRIGHT = 17
HOOPCOURTUPSIDERIGHT = 18

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
    13: 'BLEACHERS',
    14: 'BLEACHERSUPSIDE',
    15: 'HOOPCOURT',
    16: 'HOOPCOURTUPSIDE',
    17: 'HOOPCOURTRIGHT',
    18: 'HOOPCOURTUPSIDERIGHT'
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
    BLEACHERS: pygame.image.load(os.path.join(current_path,'Textures/bleachers.png')),
    BLEACHERSUPSIDE: pygame.image.load(os.path.join(current_path,'Textures/bleachersupside.png')),
    HOOPCOURT: pygame.image.load(os.path.join(current_path,'Textures/hoopcourt.png')),
    HOOPCOURTUPSIDE: pygame.image.load(os.path.join(current_path,'Textures/hoopcourtupside.png')),
    HOOPCOURTRIGHT: pygame.transform.rotate(pygame.image.load(os.path.join(current_path, 'Textures/hoopcourt.png')), 180),
    HOOPCOURTUPSIDERIGHT: pygame.transform.rotate(pygame.image.load(os.path.join(current_path,'Textures/hoopcourtupside.png')), 180)

}

# Tilemap
tilemap = [
    [OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT],
    [OUTERCOURT, OUTERCOURT, OUTERCOURT, BLEACHERSUPSIDE, BLEACHERSUPSIDE, BLEACHERSUPSIDE, BLEACHERSUPSIDE, BLEACHERSUPSIDE, OUTERCOURT, OUTERCOURT, OUTERCOURT],
    [OUTERCOURT, CORNER, EDGE, EDGE, EDGE, TLINE, EDGE, EDGE, EDGE, TRCORNER, OUTERCOURT],
    [OUTERCOURT, LEFTEDGE, COURT, COURT, COURT, HALFCOURT, COURT, COURT, COURT, RIGHTEDGE, OUTERCOURT],
    [OUTERCOURT, HOOPCOURT, COURT, COURT, COURT, HALFCOURT, COURT, COURT, COURT, HOOPCOURTUPSIDERIGHT, OUTERCOURT],
    [OUTERCOURT, HOOPCOURTUPSIDE, COURT, COURT, COURT, HALFCOURT, COURT, COURT, COURT, HOOPCOURTRIGHT, OUTERCOURT],
    [OUTERCOURT, LEFTEDGE, COURT, COURT, COURT, HALFCOURT, COURT, COURT, COURT, RIGHTEDGE, OUTERCOURT],
    [OUTERCOURT, BLCORNER, BOTTOMEDGE, BOTTOMEDGE, BOTTOMEDGE, BOTTOMLINE, BOTTOMEDGE, BOTTOMEDGE, BOTTOMEDGE, BRCORNER, OUTERCOURT],
    [OUTERCOURT, OUTERCOURT, OUTERCOURT, BLEACHERS, BLEACHERS, BLEACHERS, BLEACHERS, BLEACHERS, OUTERCOURT, OUTERCOURT, OUTERCOURT],
    [OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT, OUTERCOURT]
]

# Walls
PASSABLE = [COURT,OUTERCOURT,CORNER,HALFCOURT,TLINE,EDGE,RIGHTEDGE,BOTTOMEDGE,LEFTEDGE,BOTTOMLINE,TRCORNER,BRCORNER,BLCORNER]
NOT_PASSABLE = [HOOPCOURT, HOOPCOURTUPSIDE, BLEACHERS, BLEACHERSUPSIDE]

# Game Dimensions
TILESIZE = 64
MAPWIDTH = 11
MAPHEIGHT = 10
