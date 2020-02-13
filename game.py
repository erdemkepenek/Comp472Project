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
        allPlays.append((play,depth))
    # print("allPlays",allPlays)
    return allPlays


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
secondDimension.append((inputBoard,1))
# stack.append((inputBoard,1))
dfs(secondDimension)


