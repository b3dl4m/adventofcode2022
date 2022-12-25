text_file = open("input.txt", "r")
lines = text_file.read().splitlines()

def getPriority(inStr):
    if(inStr.isupper()):
        #A-Z 27-52 -38
        return ord(inStr)-38
    else:
        #a-z 1-26 -96
        return ord(inStr)-96

# # first task
# priorityTotal=0
# for line in lines:
#     line= [line,line[:len(line)//2],line[len(line)//2:]]
#     line+= [''.join(set(line[1]).intersection(line[2]))]
#     line+= [getPriority(line[3])]
#     priorityTotal+=line[4]
#     print line

# print priorityTotal

# second task
threeElfGroups = []
singleGroup = []
ticker=0
for line in lines:
    singleGroup+=[line]
    ticker = (ticker+1) % 3
    if(ticker==0):
        threeElfGroups.append(singleGroup)
        singleGroup=[]

priorityTotal=0
for group in threeElfGroups:
    group+= [''.join(set(group[0]) & set(group[1]) & set(group[2]))]
    group+= [getPriority(''.join((set(group[0]) & set(group[1]) & set(group[2]))))]
    priorityTotal+=group[4]

print(priorityTotal)
