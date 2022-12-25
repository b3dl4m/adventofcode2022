text_file = open("input.txt", "r")
lines = text_file.readlines()

# Rock      A and X - 1
# Paper     B and Y - 2
# Scissor   C and Z - 3

def cleanInputPair(inputString):
    inputString = inputString.replace('\n','')
    inputString = inputString.replace('A','1')
    inputString = inputString.replace('B','2')
    inputString = inputString.replace('C','3')
    inputString = inputString.replace('X','1')
    inputString = inputString.replace('Y','2')
    inputString = inputString.replace('Z','3')
    strArr = inputString.split(' ')
    return [int(strArr[0]),int(strArr[1])]

# def didYouWin(int0,int1):
#     if int0 == 3 and int1 == 1:
#         return True
#     elif int1 > int0:
#         return True
#     else:
#         return False
    
# pairs = []
# runningScore = 0
# for line in lines:
#     pairs.append(cleanInputPair(line))
#     pair = cleanInputPair(line)
#     readout = str(pair[0]) +' '+str(pair[1])+': '
#     runningScore+=pair[1]
#     if pair[0]==pair[1]: #tied
#         runningScore+=3
#         readout+='tied - Score: '+str(pair[1]+3)+' ('+str(runningScore)+')'
#     elif didYouWin(pair[0],pair[1]):
#         runningScore+=6
#         readout+='won - Score: '+str(pair[1]+6)+' ('+str(runningScore)+')'
#     else:
#         runningScore+=0
#         readout+='lost - Score: '+str(pair[1]+0)+' ('+str(runningScore)+')'
#     print readout

# print runningScore



# def pointPair(int0,int1):
#     if(int0==int1):
#         return int1+3
#     elif(int1==1 and int0==3):
#         return int1+6
#     elif(int1>int0):
#         return int1+6
#     else:
#         return int1+0

# pairs = []
# runningScore = 0
# for line in lines:
#     pairs.append(cleanInputPair(line))
#     pair = cleanInputPair(line)
#     runningScore+=pointPair(pair[0],pair[1])

    
# def pointPair(int0,int1):
#     if(int0==int1): #tie
#         return int1+3
#     elif(int1==1 and int0==3): #rock beats scissors
#         return int1+6
#     elif(int1==2 and int0==1): #paper beats rock
#         return int1+6
#     elif(int1==3 and int0==2): #scissors beats paper
#         return int1+6
#     elif(int1==1 and int0==2): #rock loses to paper
#         return int1+0
#     elif(int1==2 and int0==3): #paper loses to scissors
#         return int1+0
#     elif(int1==3 and int0==1): #scissors loses to rock
#         return int1+0
#     else:
#         return int1+0

# pairs = []
# runningScore = 0
# for line in lines:
#     pairs.append(cleanInputPair(line))
#     pair = cleanInputPair(line)
#     runningScore+=pointPair(pair[0],pair[1])


def pointPair(int0,int1):
    if(int1==1 and int0==1): #lose
        return 3
    elif(int1==1 and int0==2): 
        return 1
    elif(int1==1 and int0==3): 
        return 2
    elif(int1==2 and int0==1): #draw
        return 1+3
    elif(int1==2 and int0==2): 
        return 2+3
    elif(int1==2 and int0==3): 
        return 3+3
    elif(int1==3 and int0==1): #win
        return 2+6
    elif(int1==3 and int0==2): 
        return 3+6
    elif(int1==3 and int0==3): 
        return 1+6
    else:
        return 0

pairs = []
runningScore = 0
for line in lines:
    pairs.append(cleanInputPair(line))
    pair = cleanInputPair(line)
    runningScore+=pointPair(pair[0],pair[1])

print(runningScore)