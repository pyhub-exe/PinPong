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

class Racketka(Main):
    def update(self):
        keys=key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed
        self.reset()

class Racketka1(Main):
    def update(self):
        keys=key.get_pressed()
        if keys[K_p]:
            self.rect.y -= self.speed
        if keys[K_l]:
            self.rect.y += self.speed
        self.reset()

class Wall(sprite.Sprite):  

    def __init__(self,x,y,w,h,color):  
        self.image = Surface((w,h))   
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        win.blit(self.image,( self.rect.x,self.rect.y))
    def update(self):
#        if sprite.collide_rect(self,ball):
#            global end_game
#            end_game = lose_text       
        self.reset()

ball = Ball( x= 200,y = 540,filename="Ball.png",speed = 10,v = 50,n = 50)
racketka = Racketka(x = 10,y=540,filename="racketka1.png",speed = 10,v = 50,n = 160)
racketka1 = Racketka1(x = 1860,y = 540,filename="racketka.png",speed = 10,v = 50,n = 160)

CornflowerBlue = (100,149,237)   
DarkSlateBlue = (72,61,139)  
PeachPuff = (255,218,185)   

side_stena = Wall(0,0,1,1080,PeachPuff)     
side_stena1 = Wall(1919,0,1,1080,PeachPuff)   

resolution = [w,h]

win = display.set_mode((resolution),flags = FULLSCREEN)
display.set_caption("ПинПонг")

timer = time.Clock()
FPS = 60

mixer.init()
mixer.music.load("Music.mp3")
mixer.music.play()

fon=image.load("fon.png")

font.init()
shirift = font.SysFont("Arial",48)
lose_text = shirift.render("ТЫ ПРОИГРАЛ",False,DarkSlateBlue)

game = True
end_game = False
while game:
    for e in event.get():
        if e.type == 2:
            keys=key.get_pressed()
            if keys[K_ESCAPE]:
                game = False

    win.blit(fon,(0,0))
    timer.tick(FPS)   

    if end_game == False:
        ball.update() 
        racketka.update()
        racketka1.update()
        side_stena.update()
        side_stena1.update()
    if end_game == lose_text:
        win.blit(lose_text,(800,500))
    display.update()
