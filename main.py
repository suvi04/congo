import pygame
import sys
import time
import random

pygame.init()
font_type=pygame.font.Font(None,32)
scr_ht=1366;scr_wd=768
midpt=(scr_ht/2,scr_wd/2)
gen_frnd=1
game_active=1
pts=0
count=1

screen = pygame.display.set_mode((scr_ht,scr_wd))
pygame.display.set_caption(" Conga! ")
clk = pygame.time.Clock()
sheet=pygame.image.load("assets/character_sheet.png").convert_alpha()


def collision():
    if pygame.sprite.spritecollide(mc.sprite,frst,True):
        return 1
        
    else:
        return 0
    
def getimage(ix,iy,fx,fy):
    image=pygame.Surface((fx-ix,fy-iy)).convert_alpha()
    image.blit(sheet,(0,0),(ix,iy,fx,fy))
    image=pygame.transform.rotozoom(image,0,2)
    image.set_colorkey("black")
    return image

class spawn(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image=getimage(65,172,78,192)
        self.rect=self.image.get_rect(center=frnd_posn_gen())

def frnd_posn_gen():
    x=random.randint(50,scr_wd+500)
    y=random.randint(50,scr_ht/2-25)
    return (x,y)

class friend(pygame.sprite.Sprite):

    def __init__(self,player):
        super().__init__()
        self.image=getimage(65,172,78,192)
        self.rect=self.image.get_rect(center=(player.sprite.rect.x,player.sprite.rect.y))
        self.index=0
        self.inc=0
        

    def locn_update(self,player,count):
        self.inc=count
        self.rect=self.image.get_rect(center=(player.sprite.rect.x+20,player.sprite.rect.y+20*count))

    def player_input(self):
        self.keys=pygame.key.get_pressed()
        if  self.rect.y>65:
            if self.keys[pygame.K_UP]:
                self.rect.y-=5
        if  self.rect.y<scr_ht/2-25:
            if self.keys[pygame.K_DOWN]:
                self.rect.y+=5
        if  self.rect.x>65:
            if self.keys[pygame.K_LEFT]:
                self.rect.x-=5
        if  self.rect.x<(scr_wd+500):
            if self.keys[pygame.K_RIGHT]:
                self.rect.x+=5
    





    def down(self):
        self.image1=getimage(65,124,78,144)
        self.image2=getimage(65,148,78,168)
        self.image3=getimage(65,172,78,192)
        self.stand=[self.image1,self.image2,self.image3]
        self.index+=0.05
        if self.index>=2:self.index=0
        self.image=self.stand[int(self.index)]

    def left(self):
        self.imageL1=getimage(34,124,46,144)
        self.imageL2=getimage(34,148,46,168)
        self.imageL3=getimage(34,172,46,192)
        self.lft=[self.imageL1,self.imageL2,self.imageL3]
        self.index+=0.05
        if self.index>=2:self.index=0
        self.image=self.lft[int(self.index)]
    
    def right(self):
        self.imageR1=getimage(96,124,110,144)
        self.imageR2=getimage(96,148,110,168)
        self.imageR3=getimage(96,172,110,192)
        self.rt=[self.imageR1,self.imageR2,self.imageR3]
        self.index+=0.05
        if self.index>=2:self.index=0
        self.image=self.rt[int(self.index)]
    
    def upp(self):
        self.imageU1=getimage(1,124,14,144)
        self.imageU2=getimage(1,148,14,168)
        self.imageU3=getimage(1,172,14,192)
        self.up=[self.imageU1,self.imageU2,self.imageU3]
        self.index+=0.05
        if self.index>=2:self.index=0
        self.image=self.up[int(self.index)]
            
    def urr(self):
        self.imageUR1=getimage(16,124,32,144)
        self.imageUR2=getimage(16,148,32,168)
        self.imageUR3=getimage(16,172,32,192)
        self.ur=[self.imageUR1,self.imageUR2,self.imageUR3]
        self.index+=0.05
        if self.index>=2:self.index=0
        self.image=self.ur[int(self.index)]
    
    def ull(self):
        self.imageUL1=getimage(112,124,126,144)
        self.imageUL2=getimage(112,148,126,168)
        self.imageUL3=getimage(112,172,126,192)
        self.ul=[self.imageUL1,self.imageUL2,self.imageUL3]
        self.index+=0.05
        if self.index>=2:self.index=0
        self.image=self.ul[int(self.index)]
    
    def dll(self):
        self.imageDL1=getimage(80,124,94,144)
        self.imageDL2=getimage(80,148,94,168)
        self.imageDL3=getimage(80,172,94,192)
        self.dl=[self.imageDL1,self.imageDL2,self.imageDL3]
        self.index+=0.05
        if self.index>=2:self.index=0
        self.image=self.dl[int(self.index)]
    
    def drr(self):
        self.imageDR1=getimage(48,124,64,144)
        self.imageDR2=getimage(48,148,64,168)
        self.imageDR3=getimage(48,172,64,192)
        self.dr=[self.imageDR1,self.imageDR2,self.imageDR3]
        self.index+=0.05
        if self.index>=2:self.index=0
        self.image=self.dr[int(self.index)]
    

        
    def update(self,player,count):
        
        self.locn_update(player,count)
        self.player_input()
        self.keys=pygame.key.get_pressed()
        #self.colln()
        if self.keys[pygame.K_UP] and self.keys[pygame.K_LEFT]:
            self.ull()
        elif self.keys[pygame.K_UP] and self.keys[pygame.K_RIGHT]:
            self.urr()
        elif self.keys[pygame.K_DOWN] and self.keys[pygame.K_LEFT]:
            self.dll()
        elif self.keys[pygame.K_DOWN] and self.keys[pygame.K_RIGHT]:
            self.drr()
        elif self.keys[pygame.K_LEFT]:
            self.right()
        elif self.keys[pygame.K_RIGHT]:
            self.left()
        elif self.keys[pygame.K_UP]:
            self.upp()
        elif self.keys[pygame.K_DOWN]:
            self.down()
        else:
            self.index=0
          
class player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image=getimage(65,222,78,240)
        self.rect=self.image.get_rect(center=midpt)
        self.index=0
    
    def player_input(self):
        self.keys=pygame.key.get_pressed()
        if  self.rect.y>65:
            if self.keys[pygame.K_UP]:
                self.rect.y-=5
        if  self.rect.y<scr_ht/2-25:
            if self.keys[pygame.K_DOWN]:
                self.rect.y+=5
        if  self.rect.x>65:
            if self.keys[pygame.K_LEFT]:
                self.rect.x-=5
        if  self.rect.x<(scr_wd+500):
            if self.keys[pygame.K_RIGHT]:
                self.rect.x+=5
    
    def down(self):
        self.image1=getimage(65,220,78,242)
        self.image2=getimage(65,244,78,266)
        self.image3=getimage(65,270,78,290)
        self.stand=[self.image1,self.image2,self.image3]
        self.index+=0.05
        if self.index>=2:self.index=0
        self.image=self.stand[int(self.index)]

    def left(self):
        self.imageL1=getimage(34,220,46,242)
        self.imageL2=getimage(34,244,46,266)
        self.imageL3=getimage(34,270,46,290)
        self.lft=[self.imageL1,self.imageL2,self.imageL3]
        self.index+=0.05
        if self.index>=2:self.index=0
        self.image=self.lft[int(self.index)]
    
    def right(self):
        self.imageR1=getimage(96,220,110,242)
        self.imageR2=getimage(96,244,110,266)
        self.imageR3=getimage(96,270,110,290)
        self.rt=[self.imageR1,self.imageR2,self.imageR3]
        self.index+=0.05
        if self.index>=2:self.index=0
        self.image=self.rt[int(self.index)]
    
    def upp(self):
        self.imageU1=getimage(1,220,14,242)
        self.imageU2=getimage(1,244,14,266)
        self.imageU3=getimage(1,270,14,290)
        self.up=[self.imageU1,self.imageU2,self.imageU3]
        self.index+=0.05
        if self.index>=2:self.index=0
        self.image=self.up[int(self.index)]
            
    def urr(self):
        self.imageUR1=getimage(16,220,32,242)
        self.imageUR2=getimage(16,244,32,266)
        self.imageUR3=getimage(16,270,32,290)
        self.ur=[self.imageUR1,self.imageUR2,self.imageUR3]
        self.index+=0.05
        if self.index>=2:self.index=0
        self.image=self.ur[int(self.index)]
    
    def ull(self):
        self.imageUL1=getimage(110,220,126,242)
        self.imageUL2=getimage(110,244,126,266)
        self.imageUL3=getimage(110,270,126,290)
        self.ul=[self.imageUL1,self.imageUL2,self.imageUL3]
        self.index+=0.05
        if self.index>=2:self.index=0
        self.image=self.ul[int(self.index)]
    
    def dll(self):
        self.imageDL1=getimage(80,220,94,242)
        self.imageDL2=getimage(80,244,94,266)
        self.imageDL3=getimage(80,270,94,290)
        self.dl=[self.imageDL1,self.imageDL2,self.imageDL3]
        self.index+=0.05
        if self.index>=2:self.index=0
        self.image=self.dl[int(self.index)]
    
    def drr(self):
        self.imageDR1=getimage(48,220,64,242)
        self.imageDR2=getimage(48,244,64,266)
        self.imageDR3=getimage(48,270,64,290)
        self.dr=[self.imageDR1,self.imageDR2,self.imageDR3]
        self.index+=0.05
        if self.index>=2:self.index=0
        self.image=self.dr[int(self.index)]
         
    def update(self):
        self.player_input()


        if self.keys[pygame.K_UP] and self.keys[pygame.K_LEFT]:
            self.ull()
        elif self.keys[pygame.K_UP] and self.keys[pygame.K_RIGHT]:
            self.urr()
        elif self.keys[pygame.K_DOWN] and self.keys[pygame.K_LEFT]:
            self.dll()
        elif self.keys[pygame.K_DOWN] and self.keys[pygame.K_RIGHT]:
            self.drr()
        elif self.keys[pygame.K_LEFT]:
            self.right()
        elif self.keys[pygame.K_RIGHT]:
            self.left()
        elif self.keys[pygame.K_UP]:
            self.upp()
        elif self.keys[pygame.K_DOWN]:
            self.down()
        else:
            self.index=0
        


mc=pygame.sprite.GroupSingle()
mc.add(player())
fren=pygame.sprite.Group()
conga_line=pygame.sprite.Group()
frst=pygame.sprite.Group()
frst.add(spawn())


bg=(255,255,255)
gnd=pygame.Surface((scr_ht-100,scr_wd-100))
txt=font_type.render("Conga, Conga, Conga!",True,"black")
gnd_rect=gnd.get_rect(center=midpt)
txt_rect=txt.get_rect(center=(scr_ht/2,25))
gnd.fill("#B2FBA5")



while game_active:
    score=font_type.render(f"followers {pts}",True,"black")
    score_rect=score.get_rect(center=(scr_ht/2,scr_wd-25))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    
    screen.fill(bg)


    #blits
    screen.blit(gnd,gnd_rect)
    screen.blit(txt,txt_rect)
    screen.blit(score,score_rect)
    
    mc.draw(screen)
   

    frst.draw(screen)
    frst.update()
    
    fren.draw(screen)
    fren.update(mc,count)

    if collision():
        frst.add(spawn())
        pts+=1
        fren.add(friend(mc))
        count+=2
    
    mc.update()
    print()
    pygame.display.update()
    clk.tick(60)
