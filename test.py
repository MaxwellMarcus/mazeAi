import random

numOfTopFittnesses = 1
creatureRepeats = 2
creatureMoveChanges = 1
numMoves = 10

fitnesses = [[1,1,1,1,1,1,1,1,1,1]]

creatureList = []

i = 0
while i < numOfTopFittnesses:
    l = 0

    directions = fitnesses[i]
    while l < creatureRepeats:
        z = 0
        while z < creatureMoveChanges:
            changedDirection = random.randint(0,numMoves - 1)
            print("Creature" + str(l) + ": " + str(changedDirection))
            directions[changedDirection] = random.randint(1,4)
            print("Creature" + str(l) + ":   " + str(directions))
            z += 1

        directions = fitnesses[i]

        creature = directions
        l += 1

        print("Directions: " + str(directions))

        creatureList.append(creature)
    i += 1
