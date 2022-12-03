numbers = [17,1,3,16,19,0]

def add_to_dict(lastSeen, k, v):
    if k in lastSeen:
        lastSeen[k] = lastSeen[k] + [v]
    else:
        lastSeen[k] = [v]

def part_one():
    lastSeen = {} # number = turn
    turn = 0
    lastNumber = 0

    for i in range(len(numbers)):
        add_to_dict(lastSeen, numbers[i], turn)
        lastNumber = numbers[i]
        turn += 1

    while turn != 2020:
        if len(lastSeen[lastNumber]) == 1:
            add_to_dict(lastSeen, 0, turn)
            lastNumber = 0
            turn += 1
        elif len(lastSeen[lastNumber]) > 1:
            lastNumber = turn - 1 - lastSeen[lastNumber][-2]
            add_to_dict(lastSeen, lastNumber, turn)
            turn += 1
    return lastNumber

def part_two():
    lastPosition = {}
    turn = 0
    lastNumber = 0
    for _ in range(len(numbers)):
        lastPosition[numbers[turn]] = turn
        lastNumber = numbers[turn]
        turn += 1
        # print(turn, lastNumber)
    while turn != 30000000:
        if lastNumber not in lastPosition:
            # print("not seen", lastNumber)
            lastPosition[lastNumber] = turn - 1
            lastNumber = 0
        else:
            lastLast = lastPosition[lastNumber]
            # print("Last Seen", lastNumber, lastLast)
            lastPosition[lastNumber] = turn - 1
            lastNumber = (turn - 1 - lastLast)
        turn += 1
        # print(turn, lastNumber)
    print(lastNumber)

print("Part 1:", part_one())
print("Part 2:" ,part_two())
