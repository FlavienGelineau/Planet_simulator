import pygame
import planet

class Screen:
    black = [0, 0, 0]
    white = [255, 255, 255]
    xmax = 1000
    ymax = 700

    def __init__(self):  # truc qui va etre apellé a la création de tout objet affichage
        pygame.init()
        pygame.display.set_caption("Systeme solaire")
        taille = [Screen.xmax, Screen.ymax]
        self.screen = pygame.display.set_mode(taille)
        self.clock = pygame.time.Clock()

    def effacer(self):
        self.screen.fill(Screen.black)

    def actualiser(self):
        pygame.display.flip()
        self.clock.tick(80)

    def evenement(self, listePlanetes):
        # récupere la valeur des frottements

        file = open("frottements.txt")
        chaine = ""
        for line in file:
            chaine += line
        if chaine == '0.99':
            chaine = 0.99
        elif chaine == '1.0':
            chaine == 1.0
        frottements = float(chaine)

        for event in pygame.event.get():  # permet de savoir si on veut sortir du programme(accessoirement sans ca, sa plante)

            if event.type == pygame.QUIT:
                return True

            pos = pygame.mouse.get_pos()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    p = planet.Planete(pos[0], pos[1], 0, 0, 800)
                    listePlanetes.append(p)
                elif event.key == pygame.K_c:
                    p = planet.Planete(pos[0], pos[1], 0, 0, 3000)
                    listePlanetes.append(p)
                elif event.key == pygame.K_f:

                    if frottements == 1.0:
                        frottements = 0.99


                    else:
                        frottements = 1.0

                    mon_fichier = open("frottements.txt", "w")
                    frottements = str(frottements)
                    mon_fichier.write(frottements)
                    mon_fichier.close()



            elif event.type == pygame.MOUSEBUTTONDOWN:
                p = planet.Planete(pos[0], pos[1], 8, 0, 20)
                listePlanetes.append(p)

        return False

    def affichePoint(self, x, y, m):
        red = max(0, 255 - int(m / 5))

        pygame.draw.circle(self.screen, [red, 255, 255], [x, y], 5 + int(m / 100))

