import random

creatureList = []
numOfGens = 10
generation = 1
fitnesses = []
numCreatures = 1000
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

finnish = [playFieldX,playFieldY]

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
            if creature[creatureYPos] < playFieldY:
                creature[creatureYPos] += 1
        else:
            if creature[creatureYPos] > 0:
                creature[creatureYPos] -= 1
        i += 1

i = 0
while i < numCreatures:
    directions = []
    j  = 0
    while j < numMoves:
        directions.append(random.randint(1,4))
        j += 1
    creature = [0,0,directions,0]

    creatureList.append(creature)
    i += 1

i = 0

while i < numCreatures:
    creature = creatureList[i]
    move(creature)
    creature[creatureFitness] = (creature[creatureXPos] - playFieldX) + (creature[creatureYPos] - playFieldY)
    fitnesses.append(creature[creatureFitness])

    i += 1

end = []
i = 0
while i < numCreatures:

    creature = fitnesses[i]
    fitnessNum = creature[creatureFitness]

    if i == 0:
        end += [creature]

    elif fitnessNum < end[0][creatureFitness]:
        end.insert(0,creature)

    elif fitnessNum >= end[0][creatureFitness]:
        isBigest = True
        y = 0
        while y < len(end):
            if num<end[y][5]:
                end.insert(y,original[x])
                bigest = False
                break
            y += 1
        if bigest:
            end.append(original[x])

    x+=1
    y = 0
