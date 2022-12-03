inputFile = [x for x in open("./input/day13.txt").read().split("\n")]
busTimes = [int(x) for x in inputFile[1].split(",") if x != 'x']
busTimesWithX = [x for x in inputFile[1].split(",")]

def part_one():
    startTime = int(inputFile[0])
    first = [True, 0, 0]
    for currentTime in range(startTime, startTime + max(busTimes)):
        for x in busTimes:
            if divmod(currentTime, x)[1] == 0:
                if first[0]:
                    first = [False, currentTime, x]
    return (first[1] - startTime) * first[2]

def part_two():
    startTime = 905694340256700
    while True:
        print(startTime)
        correct = True
        # verify if solution is correct
        for offset, x in enumerate(busTimesWithX):
            if x == 'x':
                continue
            if (startTime + offset) % int(x) != 0:
                correct = False
                break
        if correct:
            return startTime
        startTime += 1

if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())