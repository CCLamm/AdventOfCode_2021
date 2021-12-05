# MAIN RUN CODE
map = [[0 for x in range(1000)] for y in range(1000)] 
lines = []

# Read input and parse line definitions
with open("input.txt") as file:
    nextLine = file.readline()
    while nextLine:    
        nextLine = nextLine.split("->")
        lines.append([[int(x) for x in nextLine[0].split(",")],[int(x) for x in nextLine[1].split(",")]])
        nextLine = file.readline()

# Populate straight lines into map
for line in lines:
    if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
        for x in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0])+1):
            for y in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1])+1):
                map[x][y] = map[x][y] + 1

result = 0
for row in map:
    hits = [tile for tile in row if tile > 1]
    result = result + len(hits)

print("Part 1:", result)

# Populate diagonal lines into map
for line in lines:
    if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
        xStep = 1 if line[0][0]<line[1][0] else -1
        yStep = 1 if line[0][1]<line[1][1] else -1
        for cnt in range(max(line[0][0], line[1][0])-min(line[0][0], line[1][0])+1):
            map[line[0][0]+cnt*xStep][line[0][1]+cnt*yStep] = map[line[0][0]+cnt*xStep][line[0][1]+cnt*yStep] + 1

result = 0
for row in map:
    hits = [tile for tile in row if tile > 1]
    result = result + len(hits)

print("Part 2:", result)
