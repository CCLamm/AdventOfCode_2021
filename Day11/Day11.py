map = []
mapStep = []
flashes = []

# Recursive function to trigger flashes
def step(xf, yf, mapf, mapStepf, flashesf, sf):
    if xf >= 0 and xf < len(mapf) and yf >= 0 and yf < len(mapf):
        if mapStepf[xf][yf] == 0: 
            mapf[xf][yf] = mapf[xf][yf] + 1
            if mapf[xf][yf] == 10:
                flashesf.append([1, sf])
                mapf[xf][yf] = 0
                mapStepf[xf][yf] = 1
                step(xf-1, yf-1, mapf, mapStepf, flashesf, sf)
                step(xf, yf-1, mapf, mapStepf, flashesf, sf)
                step(xf+1, yf-1, mapf, mapStepf, flashesf, sf)
                step(xf-1, yf, mapf, mapStepf, flashesf, sf)
                step(xf+1, yf, mapf, mapStepf, flashesf, sf)
                step(xf-1, yf+1, mapf, mapStepf, flashesf, sf)
                step(xf, yf+1, mapf, mapStepf, flashesf, sf)
                step(xf+1, yf+1, mapf, mapStepf, flashesf, sf)

# MAIN PROGRAM - Load input
with open("day11/input.txt") as file:
    nextLine = file.readline()
    while nextLine:    
        map.append([int(x) for x in nextLine.strip()])
        nextLine = file.readline()

# Loop until at least 100 steps OR until simultaneous flash occurrs
s=0
fullFlash = 0
while s<=100 or fullFlash == 0:
    mapStep = [[0 for x in map[y]] for y in range(len(map))]
    for x in range(len(map)):
        for y in range(len(map[0])):
            step(x, y, map, mapStep, flashes, s)
    if sum([x[0] for x in flashes if x[1]==s]) == 100:
        fullFlash = s+1
    s = s + 1
    
print("Part 1:", sum([x[0] for x in flashes if x[1]<100]))
print("Part 2:", fullFlash)

