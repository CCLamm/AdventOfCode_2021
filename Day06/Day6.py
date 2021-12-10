# MAIN RUN CODE

# Read input and parse line definitions
with open("input.txt") as file:
    fishSchool = [int(x) for x in file.readline().split(",")]

fishAge=[]
fishAge.append(sum([1 for x in fishSchool if x==0]))
fishAge.append(sum([1 for x in fishSchool if x==1]))
fishAge.append(sum([1 for x in fishSchool if x==2]))
fishAge.append(sum([1 for x in fishSchool if x==3]))
fishAge.append(sum([1 for x in fishSchool if x==4]))
fishAge.append(sum([1 for x in fishSchool if x==5]))
fishAge.append(sum([1 for x in fishSchool if x==6]))
fishAge.append(sum([1 for x in fishSchool if x==7]))
fishAge.append(sum([1 for x in fishSchool if x==8]))

# Populate straight lines into map
#for x in range(256):
#    for fish in range(len(fishSchool)):
#        if fishSchool[fish]==0:
#            fishSchool[fish]=6
#            fishSchool.append(8)
#        else:
#            fishSchool[fish]=fishSchool[fish]-1

#result = len(fishSchool)
#print("Part 1:", result)

for x in range(256):
    fish0 = fishAge[0]
    fishAge.pop(0)
    fishAge[6] = fishAge[6] + fish0
    fishAge.append(fish0)



result = sum(fishAge)
print("Part 2:", result)

