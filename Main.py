from Map import *
from Character import *
from keyboard import is_pressed
from Bullet import *
import time
import os

player1 = Character(100, 1, Map.upHeight + Map.downHeight, "☚", "☛", "☛")  # ☛ ☚ uWu
player2 = Character(
    100, Map.mapWidth - 3, Map.upHeight + Map.downHeight, "☜", "☞", "☜"  # ☞ ☜ UwU
)
gameMap = Map.map
bullet = Bullet()
bulletSymbol = "•"
bulletDamage = 5


def Change(liste, x, y, symbol):
    new = list(liste[y])
    new[x] = symbol
    return "".join(new)


def bulletMovement(tempMap):
    temp = bullet.location
    for i, value in enumerate(temp):
        tempMap[value[1]] = Change(tempMap, value[0], value[1], " ")
        if (not tempMap[value[1]][value[0] + 1] in Map.foribdden) and (
            not tempMap[value[1]][value[0] - 1] in Map.foribdden
        ):
            if value[2] == "right":
                value[0] += 1
            else:
                value[0] -= 1
            tempMap[value[1]] = Change(tempMap, value[0], value[1], bulletSymbol)
        else:
            try:
                bullet.location.pop(i)
            except:
                pass
    return tempMap


def damage():
    for value in bullet.location:
        if (
            value[0] == player1.x
            or (value[0] - 1 == player1.x and value[2] == "left")
            or (value[0] + 1 == player1.x and value[2] == "right")
        ) and value[1] == player1.y:
            player1.health -= bulletDamage
        if (
            value[0] == player2.x
            or (value[0] - 1 == player2.x and value[2] == "left")
            or (value[0] + 1 == player2.x and value[2] == "right")
        ) and value[1] == player2.y:
            player2.health -= bulletDamage


def Movement():
    # Player 1
    gameMap[player1.y] = Change(gameMap, player1.x, player1.y, " ")
    player1.down()
    player1.jump()
    if is_pressed("a"):
        player1.left()
    if is_pressed("d"):
        player1.right()
    if is_pressed("w"):
        player1.up()
    if is_pressed("f"):
        player1.shout("player1")

    # Player 2
    gameMap[player2.y] = Change(gameMap, player2.x, player2.y, " ")
    player2.down()
    player2.jump()
    if is_pressed("left"):  # left
        player2.left()
    if is_pressed("right"):  # right
        player2.right()
    if is_pressed("up"):
        player2.up()
    if is_pressed("down"):
        player2.shout("player2")


while player1.health > 0 and player2.health > 0:
    # time.sleep(0.25)
    os.system("cls" if os.name == "nt" else "clear")
    Movement()
    gameMap[player1.y] = Change(gameMap, player1.x, player1.y, player1.cSymbol)
    gameMap[player2.y] = Change(gameMap, player2.x, player2.y, player2.cSymbol)
    gameMap = bulletMovement(gameMap)
    damage()
    Map.MapPrint(gameMap, player1.health, player2.health)
if player1.health > player2.health:
    print("Player1 Qazandı")
else:
    print("Player2 Qazandı")
