def mapScore(code):
    return {
        ")":3,
        "]":57,
        "}":1197,
        ">":25137,
    }[code]

def mapPoints(code):
    return {
        "(":1,
        "[":2,
        "{":3,
        "<":4,
    }[code]

def mapOpener(code):
    return {
        ")":"(",
        "]":"[",
        "}":"{",
        ">":"<",
    }[code]

def parse(line):
    parser = []
    for c in line:
        if "([{<>}])".find(c) >=0:
            if "([{<".find(c) >= 0:
                parser.append(c) 
            else:
                if parser[-1] == mapOpener(c):
                    parser.pop()
                else:
                    return c, parser
    return "", parser

def parseEnd(line):
    score = 0
    for i in range(len(line)-1,-1,-1):
        score = score * 5 + mapPoints(line[i])
    return score

lines = []
errors = []
parserErr = []
scores = []
parserOut = []

with open("input.txt") as file:
    nextLine = file.readline()
    while nextLine:    
        lines.append([x for x in nextLine])
        result, parserOut = parse(lines[-1])
        if result != "":
            parserErr.append(mapScore(result))
        else:
            scores.append(parseEnd(parserOut))
        nextLine = file.readline()

scores.sort()

print("PART 1: ", sum(parserErr))
print("PART 2: ", scores[int((len(scores)-1) / 2)])