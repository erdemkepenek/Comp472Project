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
    print("boards",boards)
    for board in boards:
        x = (board[0],[i for i, val in enumerate(board[0]) if val == '0' and val != '1'])
        print("x",x)
        priorities.append(x)
    return [i[0] for i in sorted(priorities, key=lambda nodes: nodes[1])]

def playForAllScenarios(board,depth):
    allPlays = []
    for x in range(len(inputBoard)):
        play = flip(board[0],x)
        allPlays.append((play,depth))
    print("allPlays",allPlays)
    return allPlays

def dfs(boards,counter):
    print("stack",stack)
    global gameOver
    global stopEditing
    global exit
    print("game Over", gameOver)
    sortedBoards = sortArrayDFS(boards)
    reversed_list = sortedBoards[::-1]
    print("Reversed List",reversed_list)
    print("counter", counter)
    if exit is False:
        if counter < maxd:
            for board in reversed_list:
                print("stack append",(board,counter))
                stack.append((board,counter))
                if "1" not in board:
                    gameOver = True
                    if gameOver is True and stopEditing is False:
                        string = ""
                        dfsSolution.write(str(counter) + " " + string.join(board) + "\n")
                        stopEditing = True
            counter += 1
            top = stack.pop()
            if gameOver is False:
                string = ""
                dfsSolution.write(str(top[1]) + " " + string.join(top[0]) + "\n")
                print("stack pop", top)
            dfs(playForAllScenarios(top, counter), counter)
            print("stack", stack)
        elif counter == maxd:
            for board in reversed_list:
                if "1" not in board:
                    gameOver = True
                    if gameOver is True and stopEditing is False:
                        string = ""
                        dfsSolution.write(str(counter) + " " + string.join(board) + "\n")
                        stopEditing = True
            if len(stack) == 0:
                if gameOver is False:
                    print("No solution")
                    dfsSolution.close()
                    dfsSolution2 = open("dfsSolution.txt", "w")
                    dfsSolution2.write("No Solution")
                    dfsSolution2.close()
                    exit = True
                else :
                    dfsSolution.close()
                print("finish")
            else:
                top = stack.pop()
                print(counter)
                if gameOver is False:
                    string = ""
                    dfsSolution.write(str(top[1]) + " " + string.join(top[0]) + "\n")
                    print("stack pop", top)
                counter = top[1]
                dfs(playForAllScenarios(top,counter),top[1])
                print("top[1]", top[1])
    else:
        print("finish")



# list12 = ['1', '1', '1', '0', '1', '0', '0', '1', '0', '1', '0', '0', '1', '0', '1', '1']
# list13 = ['1', '1', '1', '1', '1', '0', '0', '1', '0', '1', '0', '0', '1', '0', '1', '1']
# list1 = ['0', '0', '1', '0']
# list2 = ['0', '0', '0', '0', '1', '1', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1']
# list3 = ['0', '0', '0', '1', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1']
#
# lists = []
# lists.append(list1)
# lists.append(list2)
# lists.append(list12)
# lists.append(list13)
# lists.append(list3)

# print(sortArrayDFS(lists))
secondDimension = []
secondDimension.append((inputBoard,1))
stack.append((inputBoard,1))
# secondDimension.append(list1)
dfs(secondDimension,1)


