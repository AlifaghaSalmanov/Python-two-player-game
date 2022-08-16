from Map import *
from Bullet import *


class Character(Map):

    jumpDistance = 5
    isJump = False
    jumpCount = 0
    bullet = Bullet()
    maxBullet = 4
    bulletCount = 0

    def __init__(self, health, x, y, lSymbol, rSymbol, cSymbol):
        super(Character, self).__init__()
        self.health = health
        self.x = x
        self.y = y
        self.lSymbol = lSymbol
        self.rSymbol = rSymbol
        self.cSymbol = cSymbol

    def right(self):
        location = self.x + 1
        try:
            if not Map.map[self.y][location] in Map.foribdden:
                self.x += 1
                self.cSymbol = self.rSymbol
        except:
            pass

    def left(self):
        location = self.x - 1
        try:
            if not Map.map[self.y][location] in Map.foribdden:
                self.x -= 1
                self.cSymbol = self.lSymbol
        except:
            pass

    def up(self):
        location = self.y - 1
        try:
            if (not Map.map[location][self.x] in Map.foribdden) and (
                Map.map[location + 2][self.x] == "═"
            ):
                self.isJump = True
        except:
            pass

    def down(self):
        location = self.y + 1
        try:
            if Map.map[location][self.x] == " " and not self.isJump:
                self.y += 1
        except:
            pass

    def jump(self):
        if self.isJump:
            location = self.y - 1
            try:
                if (not Map.map[location][self.x] in Map.foribdden) and (
                    self.jumpCount != self.jumpDistance
                ):
                    self.y -= 1
                    self.jumpCount += 1
                else:
                    self.isJump = False
                    self.jumpCount = 0
            except:
                pass

    def shout(self, palyerIndex):
        for value in self.bullet.location:
            if value[3] == palyerIndex:
                self.bulletCount += 1
        if self.maxBullet > self.bulletCount:
            if self.cSymbol == self.rSymbol:
                if not Map.map[self.y][self.x + 1] in Map.foribdden:
                    self.bullet.addBullet(self.x + 1, self.y, "right", palyerIndex)
            else:
                if not Map.map[self.y][self.x - 1] in Map.foribdden:
                    self.bullet.addBullet(self.x - 1, self.y, "left", palyerIndex)
        else:
            self.bulletCount = 0
