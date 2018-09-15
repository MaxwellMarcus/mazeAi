import random

numOfTopFittnesses = 1
creatureRepeats = 2
creatureMoveChanges = 1
numMoves = 10

fitnesses = [[1,1,1,1,1,1,1,1,1,1]]

#creatureList = []

i = 0
while i < numOfTopFittnesses:
    l = 0

    while l < creatureRepeats:
        print("Starting creature " + str(l + 1) + "...")
        directions = list(fitnesses[0])
        print("  starting directions: " + str(directions))
        z = 0
        while z < creatureMoveChanges:
            changedDirection = random.randint(0,numMoves - 1)
            print("  Creature " + str(l + 1) + " changed item: " + str(changedDirection))
            directions[changedDirection] = random.randint(1,4)
            print("  Creature " + str(l + 1) + ":   " + str(directions))
            z += 1

        #creature = directions
        print("  fitnesses: " + str(fitnesses))
        print(" ")
        l += 1

        #creatureList.append(creature)
    i += 1
