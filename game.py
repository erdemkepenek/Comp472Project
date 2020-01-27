counter = 0
matriceSize = 0
maxd = 0
maxl = 0
board = 0
with open('textInputFile.txt','r') as f:
    for line in f:
        for word in line.split():
            if(counter==0):
                matriceSize = word
            if(counter==1):
                maxd = word
            if(counter==2):
                maxl = word
            if(counter==3):
                board = word
            counter+=1
print(matriceSize)
print(maxd)
print(maxl)
print(board)
