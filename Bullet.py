class Bullet:

    location = list()

    def addBullet(self, x, y, direction, playerIndex):
        self.location.append([x, y, direction, playerIndex])
        # print(self.location)

    def getBullet(self):
        return self.location
