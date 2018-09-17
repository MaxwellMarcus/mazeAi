from tkinter import *
import time
import random

multiplier = 10#int(input("size multiplier: "))

root = Tk()

canvas = Canvas(root,width = 120 * multiplier,height = 120 * multiplier,background = "white")
canvas.pack()

creatureList = []
numOfGens = 2000#int(input("number of generations: "))
generation = 1
fitnesses = []
topFitnesses = []
numOfTopFittnesses = 1#int(input("number of surviving creatures: "))
numCreatures = 1000#int(input("number of creatures: "))
creatureRepeats = numCreatures/numOfTopFittnesses
creatureMoveChanges = 12#int(input("number of mutations: "))

creatureXPos = 0
creatureYPos = 1
creatureDirections = 2
creatureFitness = 3
creatureGraphics = 4

right = 1
left = 2
up = 3
down = 4

playFieldX = 100
playFieldY = 100

numMoves = playFieldX + playFieldY

finnish = [playFieldX,playFieldY]

finnishlLine = canvas.create_rectangle((playFieldX + 4)*multiplier,(playFieldY + 4)*multiplier,(playFieldX+14)*multiplier,(playFieldY+14)*multiplier,fill = "green")

def move(creature):
    i = 0
    while i < numMoves:
        direction = creature[creatureDirections][i]

        if direction == right:
            if creature[creatureXPos] < playFieldX:
                if creature[creatureYPos] > playFieldY/2 or not creature[creatureXPos] == playFieldX/2:
                    creature[creatureXPos] += 1
        elif direction == left:
            if creature[creatureXPos] > 0:
                if not creature[creatureYPos] > playFieldY/2 or not creature[creatureXPos] == playFieldX/2:
                    creature[creatureXPos] -= 1
        elif direction == up:
            if creature[creatureYPos] < playFieldY:
                creature[creatureYPos] += 1
        else:
            if creature[creatureYPos] > 0:
                creature[creatureYPos] -= 1
        i += 1

    creature[creatureGraphics] = canvas.create_rectangle((creature[0] + 5)*multiplier,(creature[1] + 5)*multiplier,(creature[0] - 5)*multiplier,(creature[1] - 5)*multiplier, fill = "red",width = multiplier)
    return creature
i = 0
while i < numCreatures:
    directions = []
    j  = 0
    while j < numMoves:
        directions.append(random.randint(1,4))
        j += 1
    creature = [0,0,directions,0]
    creature.append(0)
    creatureList.append(creature)
    i += 1

i = 0

while generation <= numOfGens:

    fitnesses = []
    print("generation: " + str(generation))
    i = 0
    while i < numCreatures:
        root.update()
    #    time.sleep(1/(numCreatures*10))
        creatureList[i] = move(creatureList[i])
        creatureList[i][creatureFitness] = (creatureList[i][creatureXPos] - playFieldX) + (creatureList[i][creatureYPos] - playFieldY)
        fitnesses.append(creatureList[i])

        i += 1

    i = 0
    while i < numCreatures:
        canvas.itemconfig(creatureList[i][creatureGraphics],fill = "blue")
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
        canvas.delete(fitnesses[0][creatureGraphics])
        fitnesses.remove(fitnesses[0])

    if fitnesses[0][creatureFitness] == 0:
        time.sleep(1)
        generation = numOfGens

    print("top fitness: " + str(fitnesses[0][creatureFitness]))

    generation += 1

    creatureRepeats = numCreatures/numOfTopFittnesses

    creatureList = []
    i = 0
    while i < numOfTopFittnesses:
        l = 0
        while l < creatureRepeats:
            directions = list(fitnesses[i][creatureDirections])

            z = 0
            while z < creatureMoveChanges:
                changedDirection = random.randint(0,numMoves - 1)
                directions[changedDirection] = random.randint(1,4)
                z += 1

            creature = [0,0,directions,0]
            creature.append(0)
            l += 1

            creatureList.append(creature)
        i += 1
