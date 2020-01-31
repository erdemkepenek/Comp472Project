counter = 0
matriceSize = 0
maxd = 0
maxl = 0
board = 0
gameOver = False
with open('textInputFile.txt','r') as f:
    for line in f:
        for word in line.split():
            if(counter==0):
                matriceSize = int(word)
            if(counter==1):
                maxd = int(word)
            if(counter==2):
                maxl = int(word)
            if(counter==3):
                board = list(word)
            counter+=1
print(matriceSize)
print(maxd)
print(maxl)
print(board)

class Board:
    def __init__(self, placements, priorities):
        self.placements = placements
        self.priorities = priorities
    def __repr__(self):
        return repr((self.placements))


def sortArrayDFS(boards):
    priorities =[]
    for board in boards:
        x = Board(board,[i for i, val in enumerate(board) if val == '0'])
        priorities.append(x)
    print(priorities)
    return sorted(priorities, key=lambda nodes: nodes.priorities)


def changeDot(dot):
    if dot == '0':
        return '1'
    else:
        return '0'

def flip(board,index):
    board[index] = changeDot(board[index])
    if (index+matriceSize)%matriceSize == 0:
        if index == 0:
            board[index+1] = changeDot(board[index+1])
            board[index + matriceSize] = changeDot(board[index + matriceSize])
        elif index == len(board) - matriceSize:
            board[index + 1] = changeDot(board[index + 1])
            board[index - matriceSize] = changeDot(board[index - matriceSize])
        else:
            board[index + 1] = changeDot(board[index + 1])
            board[index + matriceSize] = changeDot(board[index + matriceSize])
            board[index - matriceSize] = changeDot(board[index - matriceSize])
    elif (index+matriceSize)%matriceSize == matriceSize-1:
        if index == matriceSize-1:
            board[index - 1] = changeDot(board[index - 1])
            board[index + matriceSize] = changeDot(board[index + matriceSize])
        elif index == len(board)-1:
            board[index - 1] = changeDot(board[index - 1])
            board[index - matriceSize] = changeDot(board[index - matriceSize])
        else:
            board[index - 1] = changeDot(board[index - 1])
            board[index + matriceSize] = changeDot(board[index + matriceSize])
            board[index - matriceSize] = changeDot(board[index - matriceSize])
    else:
        if index < matriceSize:
            board[index - 1] = changeDot(board[index - 1])
            board[index + 1] = changeDot(board[index + 1])
            board[index + matriceSize] = changeDot(board[index + matriceSize])
        elif index > (len(board) - matriceSize):
            board[index - 1] = changeDot(board[index - 1])
            board[index + 1] = changeDot(board[index + 1])
            board[index - matriceSize] = changeDot(board[index - matriceSize])
        else:
            board[index - 1] = changeDot(board[index - 1])
            board[index + 1] = changeDot(board[index + 1])
            board[index - matriceSize] = changeDot(board[index - matriceSize])
            board[index + matriceSize] = changeDot(board[index + matriceSize])

    return(board)

new_board = flip(board,1)
print(new_board)
print([i for i,val in enumerate(new_board) if val=='0'])

list12 = ['1', '1', '1', '0', '1', '0', '0', '1', '0', '1', '0', '0', '1', '0', '1', '1']
list13 = ['1', '1', '1', '1', '1', '0', '0', '1', '0', '1', '0', '0', '1', '0', '1', '1']
list1 = ['0', '0', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1']
list2 = ['0', '0', '0', '0', '1', '1', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1']
list3 = ['0', '0', '0', '1', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1']

lists = []
lists.append(list1)
lists.append(list2)
lists.append(list12)
lists.append(list13)
lists.append(list3)

print(sortArrayDFS(lists))

