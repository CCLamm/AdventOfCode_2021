# PART 1 solved simply in Excel (only formulas, no VBA)

# PART 2

def mapElement(code):
    return {
        "8-6":"a",
        "6-4":"b",
        "8-4":"c",
        "7-5":"d",
        "4-3":"e",
        "9-5":"f",
        "7-6":"g",
    }[code]

def mapPosition(code):
    return {
        "a":0,
        "b":1,
        "c":2,
        "d":3,
        "e":4,
        "f":5,
        "g":6,
    }[code]

def mapFigure(code):
    return {
        "abcefg":0,
        "cf":1,
        "acdeg":2,
        "acdfg":3,
        "bcdf":4,
        "abdfg":5,
        "abdefg":6,
        "acf":7,
        "abcdefg":8,
        "abcdfg":9,
    }[code]

# Read input 
lines = []
linesCountAll = []
linesCountLim = []
linesCountCombo = []
linesMap = []
numbers = []
numbersMapped = []
figures=[]
with open("input.txt") as file:
    nextLine = file.readline()
    while nextLine:    
        nextLine = nextLine.split(" | ")
        lines.append(sorted(["".join(sorted(x)) for x in nextLine[0].split(" ")], key=len))
        linesCountAll.append([len([x for x in lines[-1] if x.find("a") >= 0]), 
                              len([x for x in lines[-1] if x.find("b") >= 0]), 
                              len([x for x in lines[-1] if x.find("c") >= 0]), 
                              len([x for x in lines[-1] if x.find("d") >= 0]), 
                              len([x for x in lines[-1] if x.find("e") >= 0]), 
                              len([x for x in lines[-1] if x.find("f") >= 0]), 
                              len([x for x in lines[-1] if x.find("g") >= 0])])
        linesCountLim.append([len([x for x in lines[-1][3:9] if x.find("a") >= 0]),
                              len([x for x in lines[-1][3:9] if x.find("b") >= 0]),
                              len([x for x in lines[-1][3:9] if x.find("c") >= 0]),
                              len([x for x in lines[-1][3:9] if x.find("d") >= 0]),
                              len([x for x in lines[-1][3:9] if x.find("e") >= 0]),
                              len([x for x in lines[-1][3:9] if x.find("f") >= 0]),
                              len([x for x in lines[-1][3:9] if x.find("g") >= 0])])
        linesCountCombo.append([str(a)+"-"+str(b) for a,b in zip(linesCountAll[-1], linesCountLim[-1])])
        linesMap.append(list(map(mapElement, linesCountCombo[-1])))
        numbers.append(["".join(sorted(x.strip())) for x in nextLine[1].split(" ")])
        numbers[-1]=[list(map(mapPosition, list(x))) for x in numbers[-1]]
        numbers[-1]=["".join(sorted("".join([linesMap[-1][x] for x in y]))) for y in numbers[-1]]
        numbers[-1] = int("".join([str(x) for x in list(map(mapFigure, numbers[-1]))]))
        nextLine = file.readline()

print("PART 2: ", sum(numbers))
