import random

creatureList = []
numOfGens = 10
generation = 1
fitnesses = []
numCreatures = 10
numMoves = 20

creatureXPos = 0
creatureYPos = 1
creatureDirections = 2
creatureFitness = 3

right = 1
left = 2
up = 3
down = 4

playFieldX = 10
playFieldY  = 10

def move(creature):
    i = 0
    while i < numMoves:
        direction = creature[creatureDirections][i]

        if direction == right:
            if creature[creatureXPos] < playFieldX:
                creature[creatureXPos] += 1
        elif direction == left:
            if creature[creatureXPos] > 0:
                creature[creatureXPos] -= 1
        elif direction == up:
            if creature[creatureYPos] > 0:
                creature[creatureXPos] += 1
        else:
            if creature[creatureYPos] > 0:
                creature[creatureXPos] += 1

i = 0
while i < numCreatures
    directions = []
    j  = 0
    while j < numMoves:
        directions.append(random.randint(1,4))
    creature = [0,0,directions,0]

    creatureList.append(creature)
    i += 1

i = 0

while i < numCreatures:
    i += 1
    move()
