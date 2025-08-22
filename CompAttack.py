import pygame
import random
import os, sys, math
sys.path.insert(0, "/home/deck/Documents") # needed to load LEDlib and Highscorelib
import LEDpygamelib, Highscorelib


# Computers Attack!
# TODO
# draw computers: ZX81, C64, etc. They are the robots and shoot disks and CD-ROMs
# create cute creatures to rescue - GitHub furry, Linux Penguin, etc, look for Linux Icons

# Keep LED graphics for special effects, particle explosions, etc
# full game
# read joystciks - simple ..? see copilot
# write brief history at button of screen ZX80 RAM:4k, CPU: Z80, etc

# Initialize Pygame
pygame.init()

# mark sure sprites are drawn rectangular (not isometric diagonal) for easy collision rectangles
charZX80 = [(0,0,"#DDDDDD"), (0,1,"#DDDDDD"), (0,2,"#DDDDDD"), (0,3,"#DDDDDD"), (0,4,"#DDDDDD"), (0,5,"#DDDDDD"), (0,6,"#DDDDDD"), (0,7,"#DDDDDD"), (0,8,"#DDDDDD"), (0,9,"#DDDDDD"), (0,10,"#DDDDDD"), (0,11,"#DDDDDD"), (0,12,"#DDDDDD"), (0,13,"#DDDDDD"), (1,0,"#DDDDDD"), (1,1,"#DDDDDD"), (1,2,"#DDDDDD"), (1,3,"#DDDDDD"), (1,4,"#DDDDDD"), (1,5,"#FFFF00"), (1,6,"#FFFF00"), (1,7,"#FFFF00"), (1,8,"#FFFF00"), (1,9,"#FFFF00"), (1,10,"#0000FF"), (1,11,"#4C3A23"), (1,12,"#0000FF"), (1,13,"#DDDDDD"), (2,0,"#AAAAAA"), (2,1,"#AAAAAA"), (2,2,"#AAAAAA"), (2,3,"#AAAAAA"), (2,4,"#AAAAAA"), (2,5,"#FFFF00"), (2,6,"#DDDDDD"), (2,7,"#FFFF00"), (2,8,"#DDDDDD"), (2,9,"#FFFF00"), (2,10,"#4C3A23"), (2,11,"#4C3A23"), (2,12,"#4C3A23"), (2,13,"#DDDDDD"), (3,0,"#AAAAAA"), (3,1,"#4C3A23"), (3,2,"#AAAAAA"), (3,3,"#4C3A23"), (3,4,"#AAAAAA"), (3,5,"#FFFF00"), (3,6,"#FFFF00"), (3,7,"#FFFF00"), (3,8,"#FFFF00"), (3,9,"#FFFF00"), (3,10,"#0000FF"), (3,11,"#4C3A23"), (3,12,"#0000FF"), (3,13,"#DDDDDD"), (4,0,"#AAAAAA"), (4,1,"#4C3A23"), (4,2,"#AAAAAA"), (4,3,"#4C3A23"), (4,4,"#AAAAAA"), (4,5,"#DDDDDD"), (4,6,"#DDDDDD"), (4,7,"#DDDDDD"), (4,8,"#DDDDDD"), (4,9,"#DDDDDD"), (4,10,"#4C3A23"), (4,11,"#4C3A23"), (4,12,"#4C3A23"), (4,13,"#DDDDDD"), (5,0,"#AAAAAA"), (5,1,"#4C3A23"), (5,2,"#AAAAAA"), (5,3,"#4C3A23"), (5,4,"#AAAAAA"), (5,5,"#FFFF00"), (5,6,"#FFFF00"), (5,7,"#FFFF00"), (5,8,"#FFFF00"), (5,9,"#FFFF00"), (5,10,"#0000FF"), (5,11,"#4C3A23"), (5,12,"#0000FF"), (5,13,"#DDDDDD"), (6,0,"#AAAAAA"), (6,1,"#4C3A23"), (6,2,"#AAAAAA"), (6,3,"#4C3A23"), (6,4,"#AAAAAA"), (6,5,"#FFFF00"), (6,6,"#DDDDDD"), (6,7,"#DDDDDD"), (6,8,"#DDDDDD"), (6,9,"#FFFF00"), (6,10,"#4C3A23"), (6,11,"#4C3A23"), (6,12,"#4C3A23"), (6,13,"#DDDDDD"), (7,0,"#AAAAAA"), (7,1,"#AAAAAA"), (7,2,"#AAAAAA"), (7,3,"#AAAAAA"), (7,4,"#AAAAAA"), (7,5,"#FFFF00"), (7,6,"#FFFF00"), (7,7,"#FFFF00"), (7,8,"#FFFF00"), (7,9,"#FFFF00"), (7,10,"#0000FF"), (7,11,"#4C3A23"), (7,12,"#0000FF"), (7,13,"#DDDDDD"), (8,0,"#DDDDDD"), (8,1,"#DDDDDD"), (8,2,"#DDDDDD"), (8,3,"#DDDDDD"), (8,4,"#DDDDDD"), (8,5,"#DDDDDD"), (8,6,"#DDDDDD"), (8,7,"#DDDDDD"), (8,8,"#DDDDDD"), (8,9,"#DDDDDD"), (8,10,"#4C3A23"), (8,11,"#4C3A23"), (8,12,"#4C3A23"), (8,13,"#DDDDDD"), (9,0,"#DDDDDD"), (9,1,"#DDDDDD"), (9,2,"#DDDDDD"), (9,3,"#DDDDDD"), (9,4,"#DDDDDD"), (9,5,"#DDDDDD"), (9,6,"#DDDDDD"), (9,7,"#DDDDDD"), (9,8,"#DDDDDD"), (9,9,"#DDDDDD"), (9,10,"#DDDDDD"), (9,11,"#DDDDDD"), (9,12,"#DDDDDD"), (9,13,"#DDDDDD")]
charHuman = [(0,4,"#C19153"), (0,5,"#C19153"), (0,6,"#BE1CBE"), (0,7,"#FFFF00"), (1,4,"#C19153"), (1,5,"#C19153"), (1,6,"#BE1CBE"), (1,7,"#FFFF00"), (1,8,"#FF0000"), (2,4,"#C19153"), (2,5,"#C19153"), (2,6,"#BE1CBE"), (2,7,"#FFFF00"), (3,3,"#C19153"), (3,4,"#C19153"), (3,5,"#C19153"), (3,11,"#FFFF00"), (4,3,"#C19153"), (4,4,"#C19153"), (4,5,"#C19153"), (4,6,"#C19153"), (4,7,"#C19153"), (4,8,"#C19153"), (4,9,"#C19153"), (4,10,"#C19153"), (4,11,"#FFFF00"), (5,0,"#C19153"), (5,1,"#FFFF00"), (5,2,"#FFFF00"), (5,3,"#FFFF00"), (5,4,"#C19153"), (5,5,"#FF0000"), (5,6,"#C19153"), (5,7,"#FF0000"), (5,8,"#FF0000"), (5,9,"#FF0000"), (5,10,"#C19153"), (5,11,"#FFFF00"), (6,0,"#C19153"), (6,1,"#FFFF00"), (6,2,"#0000FF"), (6,3,"#FFFF00"), (6,4,"#FFFF00"), (6,5,"#C19153"), (6,6,"#C19153"), (6,7,"#C19153"), (6,8,"#C19153"), (7,0,"#C19153"), (7,1,"#FFFF00"), (7,2,"#FFFF00"), (7,3,"#FFFF00"), (7,4,"#FFFF00"), (7,5,"#C19153"), (7,6,"#C19153"), (7,7,"#C19153"), (7,8,"#C19153"), (8,0,"#C19153"), (8,1,"#FFFF00"), (8,2,"#0000FF"), (8,3,"#FFFF00"), (8,4,"#FFFF00"), (8,5,"#C19153"), (8,6,"#C19153"), (8,7,"#C19153"), (8,8,"#C19153"), (9,0,"#C19153"), (9,1,"#FFFF00"), (9,2,"#FFFF00"), (9,3,"#FFFF00"), (9,4,"#C19153"), (9,5,"#FF0000"), (9,6,"#C19153"), (9,7,"#FF0000"), (9,8,"#FF0000"), (9,9,"#FF0000"), (9,10,"#C19153"), (9,11,"#FFFF00"), (10,3,"#C19153"), (10,4,"#C19153"), (10,5,"#C19153"), (10,6,"#C19153"), (10,7,"#C19153"), (10,8,"#C19153"), (10,9,"#C19153"), (10,10,"#C19153"), (10,11,"#FFFF00"), (11,3,"#C19153"), (11,4,"#C19153"), (11,5,"#C19153"), (11,11,"#FFFF00"), (12,4,"#C19153"), (12,5,"#C19153"), (12,6,"#BE1CBE"), (12,7,"#FFFF00"), (13,4,"#C19153"), (13,5,"#C19153"), (13,6,"#BE1CBE"), (13,7,"#FFFF00"), (13,8,"#FF0000"), (14,4,"#C19153"), (14,5,"#C19153"), (14,6,"#BE1CBE"), (14,7,"#FFFF00")]
charBullet = [(0,11,"#FFFF00"), (1,11,"#C19153"), (2,11,"#FFFF00"), (3,11,"#FF0000"), (4,11,"#FFFF00"), (5,11,"#C19153"), (6,11,"#F498EC"), (7,11,"#C19153"), (8,11,"#FFFF00"), (9,11,"#FFFF00"), (10,11,"#FF0000"), (11,11,"#FFFF00"), (12,11,"#FFFF00"), (13,11,"#FF0000"), (14,11,"#F498EC"), (15,11,"#FFFF00"), (16,11,"#FF0000"), (17,11,"#FF0000"), (18,11,"#FFFF00"), (19,11,"#F498EC"), (20,11,"#AAAAAA"), (21,11,"#FFFF00"), (22,11,"#C19153"), (23,11,"#FFFF00")]


# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Computers Attack!")

current_script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_directory)

font = pygame.font.SysFont("Arial", 24)

running = True
clock = pygame.time.Clock()
pygame.mixer.init()
shootsound = pygame.mixer.Sound("shoot.wav")

STEPD = 2 # speed of ship. 
STARTX = WIDTH//2  # start location of human
STARTY = HEIGHT//2
LEVELSTART = 1   # change with start keys 1,2,3,...,9
BONUSMAN = 20000
BONUSMANSTEP = 20000
scoreddisplay = []
enemylist = []
solidlist = []
bulletlist = []
robotlist = []
humanlist  = []
liveslist = []
score = 0
bonusscore = 1000
highscore = Highscorelib.load_high_score("highscore.txt")
PlayerAlive = True
CanFire = True
RobotSpeed = 0.2
HUMANSPEED = 0.3

myship = LEDpygamelib.pygameLEDobj(screen,200,300,dx = 0,dy = 0,CharPoints=charHuman, pixelsize = 2)
displayscore = LEDpygamelib.pygameLEDscoreobj(screen,x=180,y=10,score=0,colour="white",pixelsize=3, charwidth = 24,numzeros=7, solid = False)
displaytextscore = LEDpygamelib.pygameLEDtextobj(screen,x=227,y=35,text="SCORE",colour="yellow",pixelsize = 2, charwidth=14, solid = True)
displayhighscore = LEDpygamelib.pygameLEDscoreobj(screen,x=WIDTH-171,y=10,score=highscore,colour="white",pixelsize=3, charwidth = 24,numzeros=7)
displaytexthighscore = LEDpygamelib.pygameLEDtextobj(screen,x=WIDTH-135,y=35,text="HISCORE",colour="yellow",pixelsize = 2, charwidth=14, solid = True)
dlx = 70
displaylevel = LEDpygamelib.pygameLEDscoreobj(screen,x=WIDTH//2+14+dlx,y=10,score=LEVELSTART,colour="white",pixelsize=3, charwidth = 24,numzeros=2)
displaytextlevel = LEDpygamelib.pygameLEDtextobj(screen,x=WIDTH//2+dlx,y=35,text="LEVEL",colour="yellow",pixelsize = 2, charwidth=14, solid = True)


def randyloc():
    return random.randint(53,HEIGHT-100)
def randxloc():
    return random.randint(20,WIDTH-20)

def createplayfield():
    for i in range(LEVELSTART+4):
        x = randxloc()
        y = randyloc()
        myrobot = LEDpygamelib.pygameLEDobj(screen,x,y,dx = 0,dy = 0,CharPoints=charZX80, pixelsize = 2)
        myrobot.collisionrect = (0,0,21,25)
        #myrobot.showcollisionrect()
        robotlist.append(myrobot)

def moverobots():
    for r in robotlist:
        if r.x < myship.x:
            r.x = r.x + RobotSpeed
        if r.y < myship.y:
            r.y = r.y + RobotSpeed
        if r.x > myship.x:
            r.x = r.x - RobotSpeed
        if r.y > myship.y:
            r.y = r.y - RobotSpeed
        r.draw()

def movebullets():
    bulletstoremove = []
    for b in bulletlist:
       b.move()
       if b.x > WIDTH or b.x < 0 or b.y < 0 or b.y > HEIGHT:
           bulletstoremove.append(b)
    for b in bulletstoremove:
           if b in bulletlist: # b could have been added more than once to bulletstoremove, if it hits multiple enemies
             bulletlist.remove(b)
             del b
    bulletstoremove.clear()
    
def drawscreen():
    myship.draw()
    displayscore.draw()
    displaytextscore.draw()
    displayhighscore.draw()
    displaytexthighscore.draw()
    displaylevel.draw()
    displaytextlevel.draw()
    for b in bulletlist:
        b.draw()
    for r in robotlist:
        r.draw()

def makebullet(x,y,dx,dy,rotateangle):
    global CanFire  
    bullet = LEDpygamelib.pygameLEDobj(screen,x,y,dx,dy,CharPoints=charBullet, pixelsize = 2)
    bullet.CollisionPoints = [(0,11,0),(5,11,0),(10,11,0),(15,11,0),(20,11,0),(24,11,0)] # z is colour (ignored) for rotation
    bullet.RotatedCollisionPoints = bullet.CollisionPoints.copy()
    bullet.rotate(rotateangle)
    #bullet.showcollisionlines()
    bulletlist.append(bullet)
    CanFire = False

def readkeys():
    global PlayerAlive,score, highscore, LEVELSTART, CanFire
    keys = pygame.key.get_pressed()
    if not PlayerAlive: return
    if keys[pygame.K_w]:
        myship.y -= STEPD
    if keys[pygame.K_s]:
        myship.y += STEPD
    if keys[pygame.K_a]:
        myship.x -= STEPD
    if keys[pygame.K_d]:
        myship.x += STEPD
    if keys[pygame.K_UP] and CanFire:
        makebullet(x=myship.x-12,y=myship.y-30,dx=0,dy=-24,rotateangle=90)
    if keys[pygame.K_RIGHT] and CanFire:
        makebullet(x=myship.x-12,y=myship.y-12,dx=24,dy=0,rotateangle=0)
    if keys[pygame.K_LEFT] and CanFire:
        makebullet(x=myship.x-12,y=myship.y-12,dx=-24,dy=0,rotateangle=0)
    if keys[pygame.K_DOWN] and CanFire:
        makebullet(x=myship.x-12,y=myship.y+24,dx=0,dy=24,rotateangle=90)


RELOAD = pygame.USEREVENT
# NEXTEVENT = pygame.USEREVENT+1 # etc up to 9 events

pygame.time.set_timer(RELOAD,200)
createplayfield()
while running:
    screen.fill("black")
    drawscreen()
    moverobots()
    movebullets()
    readkeys()
    for event in pygame.event.get():
        if event.type == RELOAD:
            CanFire = True
        if event.type == pygame.QUIT:
            running = False
    fps = int(clock.get_fps())
    fps_text = font.render("FPS: "+str(fps), True, "white")
    screen.blit(fps_text, (WIDTH-100,HEIGHT-30))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
