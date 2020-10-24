import math


def force(p, list_planets):
    f = [0.0, 0.0]
    G = 10.0
    for planete in list_planets:
        if p != planete:
            distance = math.sqrt((planete.x - p.x) ** 2 + (planete.y - p.y) ** 2)
            distance = max(distance, 10)

            coeff = G * p.m * planete.m / (distance ** (3))
            f[0] += coeff * (planete.x - p.x)
            f[1] += coeff * (planete.y - p.y)
    return f


class Planete:

    def __init__(self, x, y, vx, vy, m):
        self.x = float(x)
        self.y = float(y)
        self.vx = float(vx)
        self.vy = float(vy)
        self.m = float(m)

    def afficher(self, affichage):
        affichage.affichePoint(math.floor(self.x), math.floor(self.y), self.m)

        # print("affichage planete,x,y=",self.x,self.y)

    def deplacer(self, list_planets):
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

        dt = 0.1

        f = force(self, list_planets)
        ax = f[0] / self.m
        ay = f[1] / self.m

        self.x = self.x + self.vx * dt + ax * dt * dt * (1 / 2)
        self.y = self.y + self.vy * dt + ay * dt * dt * (1 / 2)

        self.vx = frottements * (self.vx + ax * dt)
        self.vy = frottements * (self.vy + ay * dt)
