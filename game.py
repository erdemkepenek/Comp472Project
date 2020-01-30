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

new_board = flip(board,12)
print(new_board)
