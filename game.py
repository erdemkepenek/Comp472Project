import copy

wordCounter = 0
matriceSize = 0
maxd = 0
maxl = 0
inputBoard = 0
gameOver = False
stack =[]
visited = []
child = 0
depth = 0
dfsSolution = open("dfsSsolution.txt", "w")
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
    print("game Over", gameOver)
    if gameOver is False:
        sortedBoards = sortArrayDFS(boards)
        reversed_list = sortedBoards[::-1]
        print("Reversed List",reversed_list)
        print("counter", counter)
        if counter < maxd:
            for board in reversed_list:
                print("stack append",(board,counter))
                stack.append((board,counter))
                if "1" not in board:
                    gameOver = True
                    break
            if gameOver is False:
                counter += 1
                top = stack.pop()
                string = ""
                print("hello"+str(top[1])+" "+string.join(top[0])+"\n")
                dfsSolution.write(str(top[1])+" "+string.join(top[0])+"\n")
                print("stack pop",top)
                dfs(playForAllScenarios(top,counter),counter)
            else:
                top = stack.pop()
                string = ""
                dfsSolution.write(str(top[1] + 1) + " " + string.join(top[0]) + "\n")
                dfsSolution.close()
                dfs(reversed_list,0)
        elif counter == maxd:
            for board in reversed_list:
                if "1" not in board:
                    gameOver = True
                    break
            if gameOver is False:
                if len(stack) == 0:
                    print("No solution")
                    print("finish")
                    dfsSolution.close()
                    dfsSolution2 = open("dfsSsolution.txt", "w")
                    dfsSolution2.write("No Solution")
                    dfsSolution2.close()
                else:
                    top = stack.pop()
                    string = ""
                    dfsSolution.write(str(top[1]+1) + " " + string.join(top[0]) + "\n")
                    print("stack pop", top)
                    counter = top[1]
                    dfs(playForAllScenarios(top,counter),top[1])
            else:
                top = stack.pop()
                string = ""
                dfsSolution.write(str(top[1] + 1) + " " + string.join(top[0]) + "\n")
                dfsSolution.close()
                dfs(reversed_list,counter)

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


