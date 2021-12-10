# PART 1, find lows
floor = []
floorLows = []

with open("input.txt") as file:
    nextLine = file.readline()
    while nextLine:    
        floor.append([10] + [int(x) for x in nextLine.strip()] + [10])
        nextLine = file.readline()

floor.insert(0, [10 for x in range(len(floor[-1]))])
floor.append([10 for x in range(len(floor[-1]))])

result = 0

for x in range(1,len(floor)):
    for y in range(1,len(floor[0])):
        if floor[x][y-1]>floor[x][y] and floor[x][y+1]>floor[x][y] and floor[x+1][y]>floor[x][y] and floor[x-1][y]>floor[x][y]:
            result = result + floor[x][y]+1
            floorLows.append([x,y,0])

print ("Part 1: ", result)

# PART 2, use recursive function calls
floorBasins = [[0 if x>=9 else 1 for x in floor[y]] for y in range(len(floor))]

def checkBasin(x, y, basins):
    if basins[x][y] == 1:
        basins[x][y] = 0
        result = 1 + checkBasin(x-1, y, basins) + checkBasin(x+1, y, basins) + checkBasin(x, y-1, basins) + checkBasin(x, y+1, basins)
    else:
        result = 0
    return result

for low in floorLows:
    low[2] = low[2] + checkBasin(low[0], low[1], floorBasins)

a, b, c = sorted([x[2] for x in floorLows])[-3:]
print ("Part 2: ", a * b * c)
