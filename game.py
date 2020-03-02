import copy

wordCounter = 0
matriceSize = 0
maxd = 0
maxl = 0
inputBoard = 0
gameOver = False
stopEditing = False
exit = False
stack =[]
visited = []
child = 0
depth = 0
dfsSolution = open("dfsSolution.txt", "w")
dfsSearch = open("dfsSearch.txt","w")
bfsSolution = open("bfsSolution.txt", "w")
bfsSearch = open("bfsSearch.txt","w")
astarSolution = open("astarSolution.txt", "w")
astarSearch = open("astarSearch.txt","w")
with open('textInputFile.txt','r') as f:
    for line in f:
        print(line.split())
        matriceSize = int(line.split()[0])
        maxd = int(line.split()[1])
        maxl = int(line.split()[2])
        inputBoard = list(line.split()[3])
print(matriceSize)
print(maxd)
print(maxl)
print(inputBoard)

def changeDot(dot):
    if dot == '0':
        return '1'
    else:
        return '0'

def flip(board,index):
    newBoard = copy.deepcopy(board)
    newBoard[index] = changeDot(newBoard[index])
    if (index+matriceSize)%matriceSize == 0:
        if index == 0:
            newBoard[index+1] = changeDot(newBoard[index+1])
            newBoard[index + matriceSize] = changeDot(newBoard[index + matriceSize])
        elif index == len(newBoard) - matriceSize:
            newBoard[index + 1] = changeDot(newBoard[index + 1])
            newBoard[index - matriceSize] = changeDot(newBoard[index - matriceSize])
        else:
            newBoard[index + 1] = changeDot(newBoard[index + 1])
            newBoard[index + matriceSize] = changeDot(newBoard[index + matriceSize])
            newBoard[index - matriceSize] = changeDot(newBoard[index - matriceSize])
    elif (index+matriceSize)%matriceSize == matriceSize-1:
        if index == matriceSize-1:
            newBoard[index - 1] = changeDot(newBoard[index - 1])
            newBoard[index + matriceSize] = changeDot(newBoard[index + matriceSize])
        elif index == len(newBoard)-1:
            newBoard[index - 1] = changeDot(newBoard[index - 1])
            newBoard[index - matriceSize] = changeDot(newBoard[index - matriceSize])
        else:
            newBoard[index - 1] = changeDot(newBoard[index - 1])
            newBoard[index + matriceSize] = changeDot(newBoard[index + matriceSize])
            newBoard[index - matriceSize] = changeDot(newBoard[index - matriceSize])
    else:
        if index < matriceSize:
            newBoard[index - 1] = changeDot(newBoard[index - 1])
            newBoard[index + 1] = changeDot(newBoard[index + 1])
            newBoard[index + matriceSize] = changeDot(newBoard[index + matriceSize])
        elif index > (len(board) - matriceSize):
            newBoard[index - 1] = changeDot(newBoard[index - 1])
            newBoard[index + 1] = changeDot(newBoard[index + 1])
            newBoard[index - matriceSize] = changeDot(newBoard[index - matriceSize])
        else:
            newBoard[index - 1] = changeDot(newBoard[index - 1])
            newBoard[index + 1] = changeDot(newBoard[index + 1])
            newBoard[index - matriceSize] = changeDot(newBoard[index - matriceSize])
            newBoard[index + matriceSize] = changeDot(newBoard[index + matriceSize])

    return(newBoard)

def generateChar(index):
    character = 0
    if index < matriceSize:
        number = (index+matriceSize)%matriceSize
        character = "A"+str(number+1)
    else:
        number = index % matriceSize
        if(int(index/matriceSize) == 1):
            character = "B" + str(number + 1)
        elif(int(index/matriceSize) == 2):
            character = "C" + str(number + 1)
        elif (int(index / matriceSize) == 3):
            character = "D" + str(number + 1)
        elif (int(index / matriceSize) == 4):
            character = "E" + str(number + 1)
        elif (int(index / matriceSize) == 5):
            character = "F" + str(number + 1)
        elif (int(index / matriceSize) == 6):
            character = "G" + str(number + 1)
        elif (int(index / matriceSize) == 7):
            character = "H" + str(number + 1)
        elif (int(index / matriceSize) == 8):
            character = "I" + str(number + 1)
        else:
            character = "J" + str(number + 1)
    return character

def sortArrayDFS(boards):
    priorities =[]
    # print("boards",boards)
    for board in boards:
        x = (board[0],[i for i, val in enumerate(board[0]) if val == '0' and val != '1'])
        # print("x",x)
        priorities.append(x)
    return [i[0] for i in sorted(priorities, key=lambda nodes: nodes[1])]


def playForAllScenarios(board,depth):
    allPlays = []
    for x in range(len(inputBoard)):
        play = flip(board[0],x)
        char = generateChar(x)
        allPlays.append((play,depth,0,char))
    return allPlays

def h(boards):
    priorities = []
    # print("boards",boards)
    for board in boards:
        x = (board[0], board[1], board[0].count('1'), board[3])
        # print("x",x)
        priorities.append(x)
    sortedBoards = sorted(priorities, key=lambda nodes: nodes[2])
    return sortedBoards[::-1]

def g(boards):
    priorities = []
    # print("boards",boards)
    for board in boards:
        x = (board[0], board[1],board[0].count('1'))
        # print("x",x)
        priorities.append(x)
    return sorted(priorities, key=lambda nodes: nodes[1])

def f(boards):
    priorities = []
    # print("boards",boards)
    for board in boards:
        x = (board[0], board[1],board[0].count('1'), board[3])
        # print("x",x)
        priorities.append(x)
    sortedBoards = sorted(priorities, key=lambda nodes: nodes[1]+nodes[2])
    return sortedBoards[::-1]


def astar(boards):
    global gameOver
    global stopEditing
    openedList = []
    closedList = []
    childNodeBoards = boards
    while gameOver is False:
        openedList = openedList + childNodeBoards
        openedList = f(openedList)
        top = openedList.pop()
        nodeBoard = ''.join(top[0])
        astarSearch.write(str(top[2]+top[1]) + " " + str(top[2]) + " " + str(top[1]) + " " + nodeBoard + "\n")
        if ("1" not in top[0] and stopEditing is False):
            astarSolution.write(str(top[3]) + " " + nodeBoard + "\n")
            stopEditing = True
        else:
            if (stopEditing is False):
                astarSolution.write(str(top[3]) + " " + nodeBoard + "\n")
        while nodeBoard in closedList or top[1] >= maxl:
            if len(openedList) != 0:
                top = openedList.pop()
                nodeBoard = ''.join(top[0])
                # print(top)
                astarSearch.write(str(top[2]+top[1]) + " " + str(top[2]) + " " + str(top[1]) + " " + nodeBoard + "\n")
                if ("1" not in top[0] and stopEditing is False):
                    astarSolution.write(str(top[3]) + " " + nodeBoard + "\n")
                    stopEditing = True
                else:
                    if (stopEditing is False):
                        astarSolution.write(str(top[3]) + " " + nodeBoard + "\n")
            else:
                gameOver = True
                break
        if (nodeBoard not in closedList and gameOver is False):
            closedList.append(nodeBoard)
            childNodeBoards = playForAllScenarios(top, top[1] + 1)
    astarSearch.close()
    astarSolution.close()
    print(stopEditing)
    if (stopEditing is False):
        astarSolution2 = open("astarSolution.txt", "w")
        astarSolution2.write("No Solution")
        astarSolution2.close()



def bfs(boards):
    global gameOver
    global stopEditing
    openedList = []
    closedList = []
    childNodeBoards = boards
    while gameOver is False:
        # print(closedList)
        openedList = openedList + childNodeBoards
        openedList = h(openedList)
        # print(stopEditing)
        # print(openedList)
        top = openedList.pop()
        nodeBoard=''.join(top[0])
        # print(top)
        bfsSearch.write(str(top[2]) + " " + str(top[2]) + " 0 " + nodeBoard + "\n")
        if ("1" not in top[0] and stopEditing is False):
            bfsSolution.write(str(top[3]) + " " + nodeBoard + "\n")
            stopEditing = True
        else:
            if (stopEditing is False):
                bfsSolution.write(str(top[3]) + " " + nodeBoard + "\n")
        while nodeBoard in closedList or top[1] >= maxl:
            if len(openedList) != 0:
                top = openedList.pop()
                nodeBoard = ''.join(top[0])
                # print(top)
                bfsSearch.write(str(top[2]) + " " + str(top[2]) + " 0 " + nodeBoard + "\n")
                if ("1" not in top[0] and stopEditing is False):
                    bfsSolution.write(str(top[3]) + " " + nodeBoard + "\n")
                    stopEditing = True
                else:
                    if (stopEditing is False):
                        bfsSolution.write(str(top[3]) + " " + nodeBoard + "\n")
            else:
                gameOver = True
                break
        #     print(len(openedList))
        # print("node",nodeBoard)
        # print(nodeBoard)
        # print(openedList)
        if (nodeBoard not in closedList and gameOver is False):
            closedList.append(nodeBoard)
            childNodeBoards = playForAllScenarios(top, top[1] + 1)
    #     print(childNodeBoards)
    bfsSearch.close()
    bfsSolution.close()
    print(stopEditing)
    if(stopEditing is False):
        bfsSolution2 = open("bfsSolution.txt", "w")
        bfsSolution2.write("No Solution")
        bfsSolution2.close()
    # print(gameOver)
    # print(closedList)
    # print(openedList)







def dfs(boards):
    global gameOver
    global stopEditing
    global exit
    counter = 1
    boards = boards
    while exit is False:
        print(stack)
        print(counter)
        sortedBoards = sortArrayDFS(boards)
        reversed_list = sortedBoards[::-1]
        # print("stack", stack)
        # print("game Over", gameOver)
        # print("Reversed List", reversed_list)
        # print("counter", counter)
        if counter < maxd:
            for board in reversed_list:
                # print("stack append",(board,counter))
                string = ""
                stack.append((board,counter))
                # dfsSearch.write((str(0) + " " + str(0) + " " + str(0) + " " + string.join(board) + "\n"))
                dfsSearch.write((str(counter) + " " + string.join(board) + "\n"))
                if "1" not in board:
                    gameOver = True
                    if gameOver is True and stopEditing is False:
                        string = ""
                        dfsSolution.write(str(counter) + " " + string.join(board) + "\n")
                        stopEditing = True
            counter += 1
            top = stack.pop()
            # print("stack pop", top)
            if gameOver is False:
                string = ""
                dfsSolution.write(str(top[1]) + " " + string.join(top[0]) + "\n")
            boards = playForAllScenarios(top, counter)
        elif counter == maxd:
            for board in reversed_list:
                # dfsSearch.write((str(0) + " " + str(0) + " " + str(0) + " " + string.join(board) + "\n"))
                dfsSearch.write((str(counter) + " " + string.join(board) + "\n"))
                if "1" not in board:
                    gameOver = True
                    if gameOver is True and stopEditing is False:
                        string = ""
                        dfsSolution.write(str(counter) + " " + string.join(board) + "\n")
                        stopEditing = True
            if len(stack) == 0:
                exit = True
                if gameOver is False:
                    # print("No solution")
                    dfsSolution.close()
                    dfsSolution2 = open("dfsSolution.txt", "w")
                    dfsSolution2.write("No Solution")
                    dfsSolution2.close()
                else :
                    dfsSolution.close()
                print("finish")
            else:
                top = stack.pop()
                # print("stack pop", top)
                if gameOver is False:
                    string = ""
                    dfsSolution.write(str(top[1]) + " " + string.join(top[0]) + "\n")
                if(top[1] == maxd-1):
                    counter = maxd
                else:
                    counter = top[1]+1
                print(counter)
                boards = playForAllScenarios(top,counter)



secondDimension = []
secondDimension.append((inputBoard,1,0,0))
astar(secondDimension)
# stack.append((inputBoard,1))
# dfs(secondDimension)



