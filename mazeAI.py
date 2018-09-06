#from Tkinter import *

import time

import random

###root = Tk()

#screen_width = #root.winfo_screenwidth()
#screen_height = #root.winfo_screenheight()

#canvas = Canvas(#root,width = screen_width,height = screen_height)
#canvas.pack()


creatureList = []

notStarted = True

generation = 0

fitnesses = []

def createNewGen():
    global creatureList
    global generation
    global fitnesses

    createCreatures = 0
    generation += 1

    if generation == 1:
        while createCreatures < 10:
            _1 = [10,10,110,110,[],0]

            creatureList.append(_1)
            createCreatures += 1
    else:
        creatureList = []
        while createCreatures < 1:
            l = 0
            while l < 10:
                directions = fitnesses[createCreatures][4]
                z = 0
        #        print(directions)
                while z < 1:
                    changedDirection = random.randint(0,19)
                    directions[changedDirection] = random.randint(1,4)
                    z += 1
        #        print(directions)
                _1 = [10,10,110,110,directions,0]
                l += 1

                creatureList.append(_1)
            createCreatures += 1
    #    print(creatureList[999])

    game = True
    print(generation)

def moveRight(player):
    if len(player[4]) < 100 and not player[2] + 100 > 1310:
#        canvas.delete(player[6])


        player[0] = player[0] + 100
        player[2] = player[2] + 100

#        player[6] = [canvas.create_rectangle(player[0],player[1],player[2],player[3],fill = "gray")]

def moveLeft(player):
    if len(player[4]) < 100 and not player[0] - 100 < 0:

#        canvas.delete(player[6])


        player[0] = player[0] - 100
        player[2] = player[2] - 100

#        player[6] = [canvas.create_rectangle(player[0],player[1],player[2],player[3],fill = "gray")]

def moveUp(player):
    if len(player[4]) < 100 and not player[1] - 100 < 0:
#        canvas.delete(player[6])


        player[1] = player[1] - 100
        player[3] = player[3] - 100

#        player[6] = [canvas.create_rectangle(player[0],player[1],player[2],player[3],fill = "gray")]

def moveDown(player):
    if len(player[4]) < 100 and not player[3] + 100 > 810:
#        canvas.delete(player[6])


        player[1] = player[1] + 100
        player[3] = player[3] + 100

#        player[6] = [canvas.create_rectangle(player[0],player[1],player[2],player[3],fill = "gray")]

def isDone(player):
    if player[0] == 1210 and player[1] == 710 and player[2] == 1310 and player[3] == 810:
        player[5] = len(player[4])
        #print("done")
        #print(len(player[4]))

def sort(original):
    end = []

    x = 0
    y = 0

    bigest = False

    while x < len(original):

        num = original[x][5]

        if x==0:
            end += [original[x]]
        #    print(str(len(end)) + "," + "begining")
        elif num < end[0][5]:
            end.insert(0,original[x])
#            print(str(len(end)) + "," + "begining")
        elif num >= end[0][5]:
            bigest = True
            while y < len(end):
                if num<end[y][5]:
#                    print(str(len(end)) + "," + "middle")
                    end.insert(y,original[x])
                    bigest = False
                    break
                y += 1
            if bigest:
#                print(str(len(end)) + "," + "end")
                end.append(original[x])
        else:
            print("what the hay is happening")

        x+=1
        y = 0

    while y < 9:
        end.remove(end[0])
        y += 1
    #print(len(end))
    original = []
    return(end)

def brain(player,generation,playernum):

    global fitnesses

    startTime = time.time()

    done = False

    e = 1

    where = []

    if generation == 1:
        while e < 20:
            where += [random.randint(1,4)]
            e = e + 1

        while len(player[4]) < 20:

            done = False
            if where[len(player[4])-1] == 1:
                moveRight(player)
                player[4] += [1]
            elif where[len(player[4]) -1] == 2:
                moveLeft(player)
                player[4] += [2]
            elif where[len(player[4]) - 1] == 3:
                moveUp(player)
                player[4] += [3]
            elif where[len(player[4]) - 1] == 4:
                moveDown(player)
                player[4] += [4]
            else:
                print("what")
            isDone(player)

            x = player[2] - 10
            y = player[3] - 10
            #print(str(playernum) + "(" + str(x/100) + "," + str(y/100) + ")")
        player[5] = ((player[2] - 1310) + (player[3] - 810))/100
    elif not generation == 1:
        n = 0
        while n < 20:
            if player[4][n] == 1:
                moveRight(player)
            elif player[4][n] == 2:
                moveLeft(player)
            elif player[4][n] == 3:
                moveUp(player)
            elif player[4][n] == 4:
                moveDown(player)
            else:
                print("okay srsly what is happening")
            n += 1

        player[5] = ((player[2] - 1310) + (player[3] - 810))/100

def start():
    global generation
    global fitnesses
    global creatureList
    moveCreatures = 0
    fitnesses = []

    while moveCreatures < len(creatureList):
    #    print(moveCreatures)
    #    print(creatureList[moveCreatures])
        brain(creatureList[moveCreatures],generation,moveCreatures)

        fitnesses += [creatureList[moveCreatures]]

        moveCreatures += 1
    fitnesses = sort(fitnesses)

    k = 0

    while k < 10:
        print(creatureList[k])
        k += 1

    print('''



    ''')

    if generation < 10:
        createNewGen()
        start()


createNewGen()
start()
