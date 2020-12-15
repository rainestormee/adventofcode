inputList = [x.split("\n") for x in open("input/day11-test.txt").read().split("\n\n")][0]

def get_states_around(x, y, before):
    if before[y][x] == ".":

        return "."
    occupiedAdj = 0
    emptyAdj = 0
    for i in range(-1, 2):
        if y + i not in range(0, len(before)):
            continue
        for j in range(-1, 2):
            if (i == 0 and j == 0) or (x + j not in range(0, len(before[i]))):
                continue
            if before[y + i][x + j] == "L":
                emptyAdj += 1
            elif before[y + i][x + j] == "#":
                occupiedAdj += 1
    if before[y][x] == "L" and occupiedAdj == 0:
        # if it is empty and there are no occupied adj, it becomes occupied
        return "#"
    if before[y][x] == "#" and occupiedAdj >= 4:
        return "L"
    return before[y][x]

def check_seats_in_vector(startX, startY, deltaX, deltaY, data):
    x, y = startX, startY
    if (x == 0 and y == 0) or (y not in range(0, len(data[x]))):
        return 0
    while x in range(0, len(data)):
        while y in range(0, len(data[x])):
            if data[x][y] == "L":
                return 1
            if data[x][y] == "#":
                return -1
            x += deltaX
            y += deltaY
    return 0

def get_states_around_direction(x, y, before):
    if before[y][x] == ".":

        return "."
    occupiedAdj = 0
    emptyAdj = 0

    for i in range(-1, 2):
        if y + i not in range(0, len(before)):
            continue
        for j in range(-1, 2):
            vectorX, vectorY = i, j
            ans = check_seats_in_vector(y, x, i, j, before)
            if ans == 1:
                emptyAdj += 1
            elif ans == -1:
                occupiedAdj += 1
    if before[y][x] == "L" and occupiedAdj == 0:
        # if it is empty and there are no occupied adj, it becomes occupied
        return "#"
    if before[y][x] == "#" and occupiedAdj >= 5:
        return "L"
    return before[y][x]

def part_one():
    global inputList
    before = inputList
    outputList = [""] * len(inputList)
    changed = True
    print(before)
    while changed:
        for x in range(0, len(before)):
            outString = ""
            for y in range(0, len(before[0])):
                #
                # outString += get_states_around(y, x, before)
                outString += get_states_around_direction(y, x, before)
            outputList[x] = outString
        if before == outputList:
            changed = False
        before = outputList
        outputList = [""] * len(before)
    print(before)
    unocc = 0
    for x in range(0, len(before)):
        for y in range(0, len(before[0])):
            if before[x][y] == "#":
                unocc += 1
    print(unocc)

if __name__ == "__main__":
    part_one()
