code = []
maps = []
charNums = []

# Function used for PART 1 - OBSOLETE after solving PART 2
#def polyStep(codef, mapsf):
#    for i in range(len(codef)-1, 0, -1):
#        iMap = [map[0] for map in mapsf].index(codef[i-1]+codef[i])
#        code.insert(i, maps[iMap][1])

# PART 2 solution, adding one step to the polymere
def polyStep2(mapsf):
    # Add new counts based on step
    for map in mapsf:
        mapsf[[map[0] for map in mapsf].index(map[4])][3] = mapsf[[map[0] for map in mapsf].index(map[4])][3] + map[2]
        mapsf[[map[0] for map in mapsf].index(map[5])][3] = mapsf[[map[0] for map in mapsf].index(map[5])][3] + map[2]
    # Consolidate count
    for map in mapsf:
        map[2] = map[3]
        map[3] = 0

# MAIN PROGRAM - Load input
with open("day14/input.txt") as file:
    code = [x for x in file.readline().rstrip()]
    nextLine = file.readline()
    nextLine = file.readline()
    while nextLine:    
        # Build MAPS array containing all char pairs
        maps.append([x.strip() for x in nextLine.split("->")])  # Pos 0 is the input pair of chars, Pos 1 is the char to add between
        maps[-1].append(0)                                      # Pos 2 is the count of occurrences of the pair
        maps[-1].append(0)                                      # Pos 3 is the temporary count of new pairs when adding a step
        maps[-1].append(maps[-1][0][0:1] + maps[-1][1])         # Pos 4 is the new LEFT pair added in a step
        maps[-1].append(maps[-1][1] + maps[-1][0][1:2])         # Pos 5 is the new RIGHT pair added in a step
        nextLine = file.readline()

# Populate initial occurrences of char pairs in the MAPS array
for x in range(len(code)-1):
    maps[[map[0] for map in maps].index(code[x]+code[x+1])][2] = maps[[map[0] for map in maps].index(code[x]+code[x+1])][2] + 1

# Loop polymore steps
for x in range(40):                                             # SET NUMBER OF STEPS TO RUN
    polyStep2(maps)

# Add last character of original code
maps[[map[0] for map in maps].index(code[-1] + code[-1])][2] = maps[[map[0] for map in maps].index(code[-1] + code[-1])][2] + 1

# Get distinct list of characters with number of occurrences
for x in list(''.join(set([map[0][0:1] for map in maps]))):
    charNums.append(sum([y[2] for y in maps if y[0][0:1]==x]))

print("Part 1/2:", max(charNums), min(charNums), max(charNums)-min(charNums))



