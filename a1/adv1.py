text_file = open("input.txt", "r")
lines = text_file.readlines()
col = []
grp = []
for ln in lines:
    if ln == '\n':
        col.append(grp)
        grp = []
    else:
        grp.append(int(ln))
text_file.close()

# highestCalCount = 0
# for elfBackpack in col:
#     backPackCalTotal = 0
#     for eachItem in elfBackpack:
#         backPackCalTotal += eachItem
#     if backPackCalTotal > highestCalCount:
#         highestCalCount = backPackCalTotal



# print "Highest Cal Count: "+str(highestCalCount)

totalCalArray = []
for elfBackpack in col:
    backPackCalTotal = 0
    for eachItem in elfBackpack:
        backPackCalTotal += eachItem
    totalCalArray.append(backPackCalTotal)
totalCalArray.sort(reverse=True)
print(totalCalArray)
print("Total of Top 3 Elves: "+str(totalCalArray[0]+totalCalArray[1]+totalCalArray[2]))