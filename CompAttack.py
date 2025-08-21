import pygame
import random
import os, sys, math
sys.path.insert(0, "/home/deck/Documents") # needed to load LEDlib and Highscorelib
import LEDlib, Highscorelib


# Computers Attack!
# TODO
# draw computers: ZX81, C64, etc. They are the robots and shoot disks and CD-ROMs
# create cute creatures to rescue - GitHub furry, Linux Penguin, etc, look for Linux Icons

# Keep LED graphics for special effects, particle explosions, etc
# full game
# read joystciks - simple ..? see copilot
# write brief history at button of screen ZX80 RAM:4k, CPU: Z80, etc
# upload to GitHub

# Initialize Pygame
pygame.init()

# mark sure sprites are drawn rectangular (not isometric diagonal) for easy collision rectangles
charZX80 = [(0,0,"#DDDDDD"), (0,1,"#DDDDDD"), (0,2,"#DDDDDD"), (0,3,"#DDDDDD"), (0,4,"#DDDDDD"), (0,5,"#DDDDDD"), (0,6,"#DDDDDD"), (0,7,"#DDDDDD"), (0,8,"#DDDDDD"), (0,9,"#DDDDDD"), (0,10,"#DDDDDD"), (0,11,"#DDDDDD"), (0,12,"#DDDDDD"), (0,13,"#DDDDDD"), (1,0,"#DDDDDD"), (1,1,"#DDDDDD"), (1,2,"#DDDDDD"), (1,3,"#DDDDDD"), (1,4,"#DDDDDD"), (1,5,"#FFFF00"), (1,6,"#FFFF00"), (1,7,"#FFFF00"), (1,8,"#FFFF00"), (1,9,"#FFFF00"), (1,10,"#0000FF"), (1,11,"#4C3A23"), (1,12,"#0000FF"), (1,13,"#DDDDDD"), (2,0,"#AAAAAA"), (2,1,"#AAAAAA"), (2,2,"#AAAAAA"), (2,3,"#AAAAAA"), (2,4,"#AAAAAA"), (2,5,"#FFFF00"), (2,6,"#DDDDDD"), (2,7,"#FFFF00"), (2,8,"#DDDDDD"), (2,9,"#FFFF00"), (2,10,"#4C3A23"), (2,11,"#4C3A23"), (2,12,"#4C3A23"), (2,13,"#DDDDDD"), (3,0,"#AAAAAA"), (3,1,"#4C3A23"), (3,2,"#AAAAAA"), (3,3,"#4C3A23"), (3,4,"#AAAAAA"), (3,5,"#FFFF00"), (3,6,"#FFFF00"), (3,7,"#FFFF00"), (3,8,"#FFFF00"), (3,9,"#FFFF00"), (3,10,"#0000FF"), (3,11,"#4C3A23"), (3,12,"#0000FF"), (3,13,"#DDDDDD"), (4,0,"#AAAAAA"), (4,1,"#4C3A23"), (4,2,"#AAAAAA"), (4,3,"#4C3A23"), (4,4,"#AAAAAA"), (4,5,"#DDDDDD"), (4,6,"#DDDDDD"), (4,7,"#DDDDDD"), (4,8,"#DDDDDD"), (4,9,"#DDDDDD"), (4,10,"#4C3A23"), (4,11,"#4C3A23"), (4,12,"#4C3A23"), (4,13,"#DDDDDD"), (5,0,"#AAAAAA"), (5,1,"#4C3A23"), (5,2,"#AAAAAA"), (5,3,"#4C3A23"), (5,4,"#AAAAAA"), (5,5,"#FFFF00"), (5,6,"#FFFF00"), (5,7,"#FFFF00"), (5,8,"#FFFF00"), (5,9,"#FFFF00"), (5,10,"#0000FF"), (5,11,"#4C3A23"), (5,12,"#0000FF"), (5,13,"#DDDDDD"), (6,0,"#AAAAAA"), (6,1,"#4C3A23"), (6,2,"#AAAAAA"), (6,3,"#4C3A23"), (6,4,"#AAAAAA"), (6,5,"#FFFF00"), (6,6,"#DDDDDD"), (6,7,"#DDDDDD"), (6,8,"#DDDDDD"), (6,9,"#FFFF00"), (6,10,"#4C3A23"), (6,11,"#4C3A23"), (6,12,"#4C3A23"), (6,13,"#DDDDDD"), (7,0,"#AAAAAA"), (7,1,"#AAAAAA"), (7,2,"#AAAAAA"), (7,3,"#AAAAAA"), (7,4,"#AAAAAA"), (7,5,"#FFFF00"), (7,6,"#FFFF00"), (7,7,"#FFFF00"), (7,8,"#FFFF00"), (7,9,"#FFFF00"), (7,10,"#0000FF"), (7,11,"#4C3A23"), (7,12,"#0000FF"), (7,13,"#DDDDDD"), (8,0,"#DDDDDD"), (8,1,"#DDDDDD"), (8,2,"#DDDDDD"), (8,3,"#DDDDDD"), (8,4,"#DDDDDD"), (8,5,"#DDDDDD"), (8,6,"#DDDDDD"), (8,7,"#DDDDDD"), (8,8,"#DDDDDD"), (8,9,"#DDDDDD"), (8,10,"#4C3A23"), (8,11,"#4C3A23"), (8,12,"#4C3A23"), (8,13,"#DDDDDD"), (9,0,"#DDDDDD"), (9,1,"#DDDDDD"), (9,2,"#DDDDDD"), (9,3,"#DDDDDD"), (9,4,"#DDDDDD"), (9,5,"#DDDDDD"), (9,6,"#DDDDDD"), (9,7,"#DDDDDD"), (9,8,"#DDDDDD"), (9,9,"#DDDDDD"), (9,10,"#DDDDDD"), (9,11,"#DDDDDD"), (9,12,"#DDDDDD"), (9,13,"#DDDDDD")]
charHuman = [(0,4,"#C19153"), (0,5,"#C19153"), (0,6,"#BE1CBE"), (0,7,"#FFFF00"), (1,4,"#C19153"), (1,5,"#C19153"), (1,6,"#BE1CBE"), (1,7,"#FFFF00"), (1,8,"#FF0000"), (2,4,"#C19153"), (2,5,"#C19153"), (2,6,"#BE1CBE"), (2,7,"#FFFF00"), (3,3,"#C19153"), (3,4,"#C19153"), (3,5,"#C19153"), (3,11,"#FFFF00"), (4,3,"#C19153"), (4,4,"#C19153"), (4,5,"#C19153"), (4,6,"#C19153"), (4,7,"#C19153"), (4,8,"#C19153"), (4,9,"#C19153"), (4,10,"#C19153"), (4,11,"#FFFF00"), (5,0,"#C19153"), (5,1,"#FFFF00"), (5,2,"#FFFF00"), (5,3,"#FFFF00"), (5,4,"#C19153"), (5,5,"#FF0000"), (5,6,"#C19153"), (5,7,"#FF0000"), (5,8,"#FF0000"), (5,9,"#FF0000"), (5,10,"#C19153"), (5,11,"#FFFF00"), (6,0,"#C19153"), (6,1,"#FFFF00"), (6,2,"#0000FF"), (6,3,"#FFFF00"), (6,4,"#FFFF00"), (6,5,"#C19153"), (6,6,"#C19153"), (6,7,"#C19153"), (6,8,"#C19153"), (7,0,"#C19153"), (7,1,"#FFFF00"), (7,2,"#FFFF00"), (7,3,"#FFFF00"), (7,4,"#FFFF00"), (7,5,"#C19153"), (7,6,"#C19153"), (7,7,"#C19153"), (7,8,"#C19153"), (8,0,"#C19153"), (8,1,"#FFFF00"), (8,2,"#0000FF"), (8,3,"#FFFF00"), (8,4,"#FFFF00"), (8,5,"#C19153"), (8,6,"#C19153"), (8,7,"#C19153"), (8,8,"#C19153"), (9,0,"#C19153"), (9,1,"#FFFF00"), (9,2,"#FFFF00"), (9,3,"#FFFF00"), (9,4,"#C19153"), (9,5,"#FF0000"), (9,6,"#C19153"), (9,7,"#FF0000"), (9,8,"#FF0000"), (9,9,"#FF0000"), (9,10,"#C19153"), (9,11,"#FFFF00"), (10,3,"#C19153"), (10,4,"#C19153"), (10,5,"#C19153"), (10,6,"#C19153"), (10,7,"#C19153"), (10,8,"#C19153"), (10,9,"#C19153"), (10,10,"#C19153"), (10,11,"#FFFF00"), (11,3,"#C19153"), (11,4,"#C19153"), (11,5,"#C19153"), (11,11,"#FFFF00"), (12,4,"#C19153"), (12,5,"#C19153"), (12,6,"#BE1CBE"), (12,7,"#FFFF00"), (13,4,"#C19153"), (13,5,"#C19153"), (13,6,"#BE1CBE"), (13,7,"#FFFF00"), (13,8,"#FF0000"), (14,4,"#C19153"), (14,5,"#C19153"), (14,6,"#BE1CBE"), (14,7,"#FFFF00")]



# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Computers Attack!")

current_script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_script_directory)




# Colors
WHITE = (255, 255, 255)
BLUE = (0, 102, 204)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Paddle
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 7

# Ball
BALL_RADIUS = 8
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_dx, ball_dy = 4, -4

# Bricks
BRICK_ROWS, BRICK_COLS = 5, 10
BRICK_WIDTH = WIDTH // BRICK_COLS
BRICK_HEIGHT = 30
bricks = [pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT, BRICK_WIDTH - 2, BRICK_HEIGHT - 2)
          for row in range(BRICK_ROWS) for col in range(BRICK_COLS)]

# Font
font = pygame.font.SysFont("Arial", 24)

def checkcollisionrect(object1,object2):
     x1,y1,x2,y2 = object1.collisionrect 
     a1,b1,a2,b2 = object2.collisionrect
     x1 = x1 + object1.x
     y1 = y1 + object1.y
     x2 = x2 + object1.x
     y2 = y2 + object1.y 
     a1 = a1 + object2.x
     b1 = b1 + object2.y
     a2 = a2 + object2.x
     b2 = b2 + object2.y 
     if x2 < a1 or x1 > a2 or y2 < b1 or y1 > b2:
          return False
     else:
          return True
     
def checkcollisionPointsinRect(object1,object2,pixelsize):
    a1,b1,a2,b2 = object2.collisionrect
    a1 = a1 + object2.x
    b1 = b1 + object2.y
    a2 = a2 + object2.x
    b2 = b2 + object2.y
    for p in object1.RotatedCollisionPoints:
        x1 = p[0]*pixelsize + object1.x
        y1 = p[1]*pixelsize + object1.y
        if x1 >= a1 and x1 <= a2 and y1 >= b1 and y1 <= b2:
            return True
    return False


def rotatepoints(points,angle,center):
         newpoints = []
         anglerad = math.radians(angle)
         cx,cy = center
         for x,y,z in points:
              x = x - cx
              y = y - cy
              newx = x* math.cos(anglerad)- y*math.sin(anglerad) + cx
              newy = x * math.sin(anglerad) + y*math.cos(anglerad) + cy
              newpoints.append((newx,newy,z))
         return newpoints

def pygameCreateCharColourSolid(screen,x,y,colourpoints,pixelsize):
  for p in colourpoints:
    pygame.draw.rect(screen, p[2], (x+p[0]*pixelsize,y+p[1]*pixelsize, pixelsize, pixelsize)) # p[2]=colour, (xloc,yloc,width,height)=rect

class pygameLEDobj:
    def __init__(self, screen,x=0,y=0,dx=0,dy=0, CharPoints = [], pixelsize = 2):
         self.alive = True
         self.x = x
         self.y = y
         self.dx = dx
         self.dy = dy
         self.screen = screen
         self.OriginalCharPoints = CharPoints
         self.CharPoints = CharPoints.copy()
         self.collisionrect = (0,0,0,0)  # top left to bottom right
         self.CollisionPoints = [(0,0,0)]
         self.RotatedCollisionPoints = [(0,0,0)]
         self.collisionimage = 0
         self.collisionlinesimage = 0
         self.collisionrectshow = False
         self.collisionlinesshow = False
         self.pixelsize = pixelsize
         pygameCreateCharColourSolid(screen,x,y,CharPoints,self.pixelsize)
    def resetposition(self,x,y):
        self.x, self.y = x,y
        self.dx, self.dy = 0,0
        self.draw()
    def draw(self):
        pygameCreateCharColourSolid(self.screen,self.x,self.y,self.CharPoints,self.pixelsize)
    def move(self): 
         self.x = self.x + self.dx
         self.y = self.y + self.dy
    def rotate(self,angledeg):
         centerx = sum(x for x,y,z in self.OriginalCharPoints)/len(self.OriginalCharPoints)
         centery = sum(y for x,y,z in self.OriginalCharPoints)/len(self.OriginalCharPoints)
         self.CharPoints = rotatepoints(self.OriginalCharPoints,angle=angledeg,center=(centerx,centery))
         self.RotatedCollisionPoints = rotatepoints(self.CollisionPoints,angle=angledeg,center=(centerx,centery))
         self.draw()



# Game loop
running = True
clock = pygame.time.Clock()

pygame.mixer.init()
shootsound = pygame.mixer.Sound("shoot.wav")


myship = pygameLEDobj(screen,200,300,dx = 0,dy = 0,CharPoints=charHuman, pixelsize = 2)


displayscore = LEDlib.pygameLEDscoreobj(screen,x=180,y=400,score=0,colour="white",pixelsize=3, charwidth = 24,numzeros=7, solid = False)
displaytextscore = LEDlib.pygameLEDtextobj(screen,x=227,y=435,text="SCORE",colour="yellow",pixelsize = 2, charwidth=14, solid = True)

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
PlayerAlive = False
CanFire = True
RobotSpeed = 0.2
HUMANSPEED = 0.3


def randyloc():
    return random.randint(53,HEIGHT-100)
def randxloc():
    return random.randint(20,WIDTH-20)

def createplayfield():
    for i in range(LEVELSTART+4):
        x = randxloc()
        y = randyloc()
        myrobot = pygameLEDobj(screen,x,y,dx = 0,dy = 0,CharPoints=charZX80, pixelsize = 2)
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

def drawscreen():
    myship.draw()
    displayscore.draw()
    displaytextscore.draw()
    for r in robotlist:
        r.draw()

createplayfield()
while running:
    screen.fill(BLACK)
    moverobots()
    drawscreen()
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # Ball movement
    ball.x += ball_dx
    ball.y += ball_dy

    # Wall collision
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx *= -1
    if ball.top <= 0:
        ball_dy *= -1
    if ball.bottom >= HEIGHT:
        ball.x, ball.y = WIDTH // 2, HEIGHT // 2
        ball_dy *= -1

    # Paddle collision
    if ball.colliderect(paddle):
        ball_dy *= -1

    # Brick collision
    hit_index = ball.collidelist(bricks)
    if hit_index != -1:
        hit_brick = bricks.pop(hit_index)
        ball_dy *= -1
        shootsound.play()

    # Draw paddle
    pygame.draw.rect(screen, BLUE, paddle)

    # Draw ball
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw bricks
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)

    # Draw score
    score_text = font.render(f"Bricks left: {len(bricks)}", True, GREEN)
    screen.blit(score_text, (10, HEIGHT - 30))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        myship.y -= STEPD
    if keys[pygame.K_s]:
        myship.y += STEPD
    if keys[pygame.K_a]:
        myship.x -= STEPD
    if keys[pygame.K_d]:
        myship.x += STEPD

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
