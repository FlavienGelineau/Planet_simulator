import pygame
import math
import random     #on a besoin ici des fonctions aleatoires, de pygame bien sur et de maths pour les arrondis/les racines carrees



listePlanetes=[]
nbPlanete=50

black = [  0,   0,   0]
white = [255, 255, 255]
xmax=1000
ymax=700

taille=[xmax,ymax]
screen = pygame.display.set_mode(taille)

class Affichage:# classe ayant toutes les données relatives a l'affichage que normalement tu aurais mis en variable globale, mais bon, c'est moche
    black = [  0,   0,   0]
    white = [255, 255, 255]
    xmax=1000
    ymax=700

    
    def __init__(self): #truc qui va etre apellé a la création de tout objet affichage
        pygame.init()
        pygame.display.set_caption("Systeme solaire")
        taille=[Affichage.xmax,Affichage.ymax]
        self.screen = pygame.display.set_mode(taille)
        self.clock = pygame.time.Clock()
        
    def effacer(self):
        self.screen.fill(Affichage.black)
    def actualiser(self):
        pygame.display.flip()
        self.clock.tick(80) 
    def evenement(self):
        #récupere la valeur des frottements
        
        
        
        
             
        file=open("frottements.txt")
        chaine=""
        for line in file:
            chaine+=line
        if chaine=='0.99':
            chaine=0.99
        elif chaine=='1.0':
            chaine==1.0
        frottements=float(chaine)
        
        
        
        
        
        
        for event in pygame.event.get():#permet de savoir si on veut sortir du programme(accessoirement sans ca, sa plante)
        
            if event.type == pygame.QUIT: 
                return True 
                
                
            pos = pygame.mouse.get_pos()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    p=Planete(pos[0],pos[1],0,0,800)
                    listePlanetes.append(p)
                elif event.key == pygame.K_c:
                    p=Planete(pos[0],pos[1],0,0,3000)
                    listePlanetes.append(p)
                elif event.key == pygame.K_f:
                    
                    if frottements==1.0:
                        frottements=0.99
                        
                        
                    else:
                        frottements=1.0
                        
                    mon_fichier = open("frottements.txt", "w") 
                    frottements=str(frottements)
                    mon_fichier.write(frottements)
                    mon_fichier.close()
                        
                

            elif event.type == pygame.MOUSEBUTTONDOWN:
                p=Planete(pos[0],pos[1],8,0,20)
                listePlanetes.append(p)

                
        return False
    def affichePoint(self,x,y,m):
        red=max(0,255-int(m/5))

        pygame.draw.circle(self.screen, [red,255,255], [x,y], 5+int(m/100))
    
        

def force(p):
    f=[0.0,0.0]
    G=10.0
    for planete in listePlanetes:
        if p!=planete:
            
            distance=math.sqrt((planete.x-p.x)**2+(planete.y-p.y)**2)
            distance=max(distance,10)
            
            coeff=G*p.m*planete.m/(distance**(3))
            #if ((math.sqrt((planete.x-p.x)**2+(planete.y-p.y)**2))**3<1000):
            #    print("vecteur distance :",((math.sqrt((planete.x-p.x)**2+(planete.y-p.y)**2))**3))   #affichage test
            f[0]+=coeff*(planete.x-p.x)
            f[1]+=coeff*(planete.y-p.y)
    return f
    

class Planete:
    
    def __init__(self,x,y,vx,vy,m):
        self.x=float(x)
        self.y=float(y)
        self.vx=float(vx)
        self.vy=float(vy)
        self.m=float(m)
        
    def afficher(self,affichage):
        affichage.affichePoint(math.floor(self.x),math.floor(self.y),self.m)
        
        #print("affichage planete,x,y=",self.x,self.y)
    
    def deplacer(self):
        file=open("frottements.txt")
        chaine=""
        for line in file:
            chaine+=line
        file.close()
        if chaine=='0.99':
            chaine=0.99
        elif chaine=='1.0':
            chaine=1.0
        frottements=chaine

        
        
        dt = 0.1
        
        
        f=force(self)
        ax=f[0]/self.m
        ay=f[1]/self.m
        
        
        self.x=self.x+self.vx*dt+ax*dt*dt*(1/2)
        self.y=self.y+self.vy*dt+ay*dt*dt*(1/2)
        
        
        self.vx=frottements*(self.vx+ax*dt)
        self.vy=frottements*(self.vy+ay*dt)



def initDonnees():
    
    automatique=True
    for i in range(nbPlanete):
        if automatique==False:
            
            x=input("x"+str(i)+":")
            y=input("y"+str(i)+":")
            vx=input("vx"+str(i)+":")
            vy=input("vy"+str(i)+":")
            m=input("masse"+str(i)+":")
        else:
            if i==0 :
                m=900
                x=600.0
                y=400.0
                vx=0
                vy=0
            else :
                m=2.0
                x=600.0#random.randrange(200,300)+1/float(i)
                y=400.0-20*i#random.randrange(200,300)+1/float(i)
                vx,vy=(20.0-i)*(-1)**i,0
        
        x=int(x)
        y=int(y)
        vx=int(vx)
        vy=int(vy)
        m=int(m)
        
        #p=Planete(x,y,vx,vy,m)
        #listePlanetes.append(p)
  
    
    
def boucleAffichage(affichage):
    done = False
    while done == False:
 
        done=affichage.evenement()
        

        affichage.effacer()
        
        for planete in listePlanetes:
            planete.afficher(affichage)
        for planete in listePlanetes:
            planete.deplacer()


#on affiche a l utilisateur si les frottements sont présents ou non

        file=open("frottements.txt")
        chaine=""
        for line in file:
            chaine+=line
        file.close()
        if chaine=='0.99':
            chaine=0.99
        elif chaine=='1.0':
            chaine=1.0
        frottements=chaine











        
        if frottements==1.0:
            font = pygame.font.Font(None, 25)
            text1 = font.render("frottements desactives   ", True, white)
            screen.blit(text1, [730,100])
        elif frottements==0.99:
            font = pygame.font.Font(None, 25)
            text1 = font.render("frottements activés   ", True, white)
            screen.blit(text1, [730,100])

        
        affichage.actualiser()
  

def principale():
    affichage=Affichage()
    initDonnees()
    boucleAffichage(affichage)
  
    
    
    
    
principale()


