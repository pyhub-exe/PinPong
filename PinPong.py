from pygame import *
w=1920
n=1080

resolution = [w,n]

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





    display.update()