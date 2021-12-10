with open("input.txt") as file:
    lines = file.readlines()

result = 0
for x in range(len(lines)-1):
    if int(lines[x])<int(lines[x+1]):
        result=result+1

print("Part 1:", result)

result = 0
for x in range(len(lines)-3):
    avg1 = int(lines[x])+int(lines[x+1])+int(lines[x+2])
    avg2 = int(lines[x+1])+int(lines[x+2])+int(lines[x+3])
    if avg1<avg2:
        result=result+1

print("Part 2:", result)
