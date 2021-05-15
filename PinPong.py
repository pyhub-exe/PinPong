from pygame import *
from random import random
w=1920
h=1080
q = 10
a = 10

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
from pygame import *
from random import random
w=1366
h=768
q = 15
a = 15

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
    def __init__(self,x,y,filename,speed,v,n):
        super().__init__(x,y,filename,speed,v,n)
        self.need_change_speed = False
        self.last_touch_racket = False

    def change_speed(self):
        self.speed += 1
        self.need_change_speed = True

    def update(self):
        if self.need_change_speed:
            self.speed -= 0.1
            if self.speed < q:
                self.speed = 10
                self.need_change_speed = False

        if self.hface == "right":
            self.rect.x += self.speed
            if sprite.collide_rect(self,racketka_right):
                self.last_touch_racket = "right"
                self.change_speed()
                self.hface="left"
                if random() > 0.5:
                    self.nface = "up"
        else:
            self.rect.x -= self.speed
            if sprite.collide_rect(self,racketka_left):
                self.last_touch_racket = "left"
                self.change_speed()
                self.hface="right" 
                if random() > 0.5:
                    self.nface = "down" 
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
    def __init__(self,x,y,filename,speed,v,n):
        super().__init__(x,y,filename,speed,v,n)
        self.need_change_speed = False

    def change_speed(self):
        self.speed -= 5
        self.need_change_speed = True

    def update(self):
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y + 160 > h:
            self.rect.y = h - 160
        if self.need_change_speed:
            self.speed += 0.01
            if self.speed > a:
                self.speed = a
                self.need_change_speed = False

        keys=key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed
        
        self.reset()

class Racketka1(Main):
    def __init__(self,x,y,filename,speed,v,n):
        super().__init__(x,y,filename,speed,v,n)
        self.need_change_speed = False

    def change_speed(self):
        self.speed -= 5
        self.need_change_speed = True

    
    def update(self):
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y + 160 > h:
            self.rect.y = h - 160
        if self.need_change_speed:
            self.speed += 0.01
            if self.speed > a:
                self.speed = a
                self.need_change_speed = False

        keys=key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
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
        if sprite.collide_rect(self,ball):
            global end_game
            end_game = lose_text       
        self.reset()




        self.reset()

ball = Ball(x= 200,y = 540,filename="Ball.png",speed = q,v = 50,n = 50)
racketka_left = Racketka(x = 10,y=540,filename="racketka1.png",speed = a,v = 50,n = 160)
racketka_right = Racketka1(x = 1165,y = 540,filename="racketka.png",speed = a,v = 50,n = 160)


CornflowerBlue = (100,149,237)   
DarkSlateBlue = (72,61,139)  
PeachPuff = (255,218,185)   

side_stena = Wall(0,0,1,1080,PeachPuff)     
side_stena1 = Wall(1366,0,1,1080,PeachPuff)   

resolution = [w,h]

win = display.set_mode((resolution),flags = FULLSCREEN)
display.set_caption("ПинПонг")

timer = time.Clock()
FPS = 40

mixer.init()
mixer.music.load("3.mp3")
mixer.music.play()

fon=image.load("fon.png")
w
font.init()
shirift = font.SysFont("Impact",148)

lose_text = shirift.render("2 ИГРОК ПРОИГРАЛ",False,DarkSlateBlue)

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
      
        racketka_left.update()
        racketka_right.update()
        side_stena.update()
        side_stena1.update()
    if end_game == lose_text:
        win.blit(lose_text,(200,200))
        exit()
    display.update()
