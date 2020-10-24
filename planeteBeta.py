import pygame
import show_screen
import planet

listePlanetes = []
nbPlanete = 50

black = [0, 0, 0]
white = [255, 255, 255]
xmax = 1000
ymax = 700

taille = [xmax, ymax]
screen = pygame.display.set_mode(taille)


def initDonnees():
    automatique = True
    for i in range(nbPlanete):
        if automatique == False:

            x = input("x" + str(i) + ":")
            y = input("y" + str(i) + ":")
            vx = input("vx" + str(i) + ":")
            vy = input("vy" + str(i) + ":")
            m = input("masse" + str(i) + ":")
        else:
            if i == 0:
                m = 900
                x = 600.0
                y = 400.0
                vx = 0
                vy = 0
            else:
                m = 2.0
                x = 600.0  # random.randrange(200,300)+1/float(i)
                y = 400.0 - 20 * i  # random.randrange(200,300)+1/float(i)
                vx, vy = (20.0 - i) * (-1) ** i, 0

        x = int(x)
        y = int(y)
        vx = int(vx)
        vy = int(vy)
        m = int(m)

def boucleAffichage(affichage):
    done = False
    while done == False:

        done = affichage.evenement(listePlanetes)

        affichage.effacer()

        for planete in listePlanetes:
            planete.afficher(affichage)
        for planete in listePlanetes:
            planete.deplacer(listePlanetes)

        # on affiche a l utilisateur si les frottements sont présents ou non

        file = open("frottements.txt")
        chaine = ""
        for line in file:
            chaine += line
        file.close()
        if chaine == '0.99':
            chaine = 0.99
        elif chaine == '1.0':
            chaine = 1.0
        frottements = chaine

        if frottements == 1.0:
            font = pygame.font.Font(None, 25)
            text1 = font.render("frottements desactives   ", True, white)
            screen.blit(text1, [730, 100])
        elif frottements == 0.99:
            font = pygame.font.Font(None, 25)
            text1 = font.render("frottements activés   ", True, white)
            screen.blit(text1, [730, 100])

        affichage.actualiser()


def main():
    affichage = show_screen.Screen()
    initDonnees()
    boucleAffichage(affichage)


if __name__ == '__main__':
    main()
