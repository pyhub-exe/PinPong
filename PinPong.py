from pygame import *
w=1920
h=1080

class Main(sprite.Sprite):

    def __init__(self,x,y,filename,speed,v,n):
        self.image = image.load(filename)
        self.image = transform.scale(self.image,(v,n))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.n = n
        self.v = v
        self.hface = "right"
        self.nface = "up"
        self.speed = speed

    def reset(self):
        win.blit(self.image,( self.rect.x,self.rect.y))

class Ball(Main):
    def update(self):
        if self.hface == "right":
            self.rect.x += self.speed
            if self.rect.x + self.v > w:
                self.hface="left"
        else:
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.hface="right" 
        
        if self.nface == "up":
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.nface="down"
        else:
            self.rect.y += self.speed
            if self.rect.y + self.n > h:
                self.nface="up" 
        self.reset()

ball=Ball(x=200,y=200,filename="Ball.png",speed = 30,v = 50,n = 50)

resolution = [w,h]

win = display.set_mode((resolution),flags = FULLSCREEN)
display.set_caption("ПинПонг")

timer = time.Clock()
FPS = 60

fon=image.load("fon.png")

game = True

while game:
    for e in event.get():
        if e.type == 2:
            keys=key.get_pressed()
            if keys[K_ESCAPE]:
                game = False

    win.blit(fon,(0,0))

    ball.update() 



    display.update()
