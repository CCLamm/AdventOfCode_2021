paths = []
links = []

# Recursive function to find allowed paths based on links
def step(pathf, linksf, pathsf):
    # Find all links leading from the last step in current path
    matchLinks = [link for link in linksf if (link[0]==pathf[0][-1] or link[1]==pathf[0][-1])] 
    bFirstPath = True
    pathInternal = []
    pathCopy = pathf[0].copy()
    part1Status = pathf[1] # remember part 1 status
    path1st = pathf[2] # remember matched lower cave with two visits

    # Loop all links from last path step
    for matchLink in matchLinks:
        # Get next link name
        linkName = matchLink[0] if matchLink[1] == pathCopy[-1] else matchLink[1]
        # if first time link is added, add it to the input path otherwise add a new path with the link added
        if bFirstPath:
            bFirstPath = False
            pathInternal = pathf
        else:
            pathsf.append([pathCopy.copy(), part1Status, path1st, 0])
            pathInternal = pathsf[-1]
            pathf=pathsf[-1]

        pathInternal[0].append(linkName)

        # PART 1: If the link is small and already in path, then mark path as failed (-1 in second array slot)
        if len([link for link in pathInternal[0] if link==linkName])>1 and linkName.islower() and pathInternal[1]==0:
            pathInternal[1] = -1

        # PART 2: Allow ONE lower cave to appear twice, all other lower caves can only appear once. (If failed, set -1 in fourth array slot)
        if linkName.islower():
            linkCount = len([link for link in pathInternal[0] if link==linkName])
            if (linkCount>1 and pathf[2]!="") or (linkCount>2) or (linkName == "start" and linkCount>1):
                pathInternal[3] = -1
            if pathInternal[3] == 0 and linkCount==2:
                if pathf[2]=="":
                    pathf[2] = linkName

        # If just added "end", then mark path as completed (1 in second/fourth array slot)
        if linkName == "end":
            if pathInternal[1] == 0: # remember if Part 1 status has already failed
                pathInternal[1] = 1
            pathInternal[3] = 1

        # If path has not failed or finished, make a recursive call to continue path to next step...
        if pathInternal[3] == 0:
            step(pathf, linksf, pathsf)

# MAIN PROGRAM - Load input
with open("day12/input.txt") as file:
    nextLine = file.readline()
    while nextLine:    
        links.append([x.strip() for x in nextLine.split("-")])
        nextLine = file.readline()

# ADD "start" as first step, then call recursive function to explore steps until fail/finish
paths.append([["start"],0, '', 0]) #Array of paths [path step array, Part 1 status, lower cave used 2 times, Part 2 status]
step(paths[-1], links, paths)
    
print("Part 1:", len([p for p in paths if p[1]==1]))
print("Part 2:", len([p for p in paths if p[3]==1]))



