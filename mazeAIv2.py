import random

creatureList = []
numOfGens = 2
generation = 1
fitnesses = []
topFitnesses = []
numOfTopFittnesses = 1
numCreatures = 2
numMoves = 20
creatureRepeats = numCreatures/numOfTopFittnesses
creatureMoveChanges = 1

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

    return creature
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

while generation <= numOfGens:
    fitnesses = []
    print("generation: " + str(generation))
    i = 0
    while i < numCreatures:
        creatureList[i] = move(creatureList[i])
        creatureList[i][creatureFitness] = (creatureList[i][creatureXPos] - playFieldX) + (creatureList[i][creatureYPos] - playFieldY)
        fitnesses.append(creatureList[i])

        i += 1

    end = []
    i = 0
    while i < numCreatures:

        creature = fitnesses[i]
        fitnessNum = creature[creatureFitness]

        if i == 0:
            end.append(creature)

        elif fitnessNum < end[0][creatureFitness]:
            end.insert(0,creature)

        elif fitnessNum >= end[0][creatureFitness]:
            isBigest = True
            j = 0
            while j < len(end):
                if fitnessNum < end[j][creatureFitness]:
                    end.insert(j,creature)
                    isBigest = False
                    break
                j += 1
            if isBigest:
                end.append(creature)
        else:
            print("what?")
        i += 1

    fitnesses = end

    i = 0
    while i < len(fitnesses) - numOfTopFittnesses:
        fitnesses.remove(fitnesses[0])

    print("top fitness: " + str(fitnesses[0]))
    generation += 1

    creatureList = []
    i = 0
    while i < numOfTopFittnesses:
        l = 0
        while l < creatureRepeats:
            directions = fitnesses[i][creatureDirections]

            z = 0
            while z < creatureMoveChanges:
                changedDirection = random.randint(0,numMoves - 1)
                print("Creature" + str(l) + ": " + str(changedDirection))
                directions[changedDirection] = random.randint(1,4)
                z += 1

            creature = [0,0,directions,0]
            l += 1

            creatureList.append(creature)
            print("Creature" + str(l) + ":   " + str(creature))
        i += 1
