file = [line.split("\n") for line in open("./input/day16.txt").read().split("\n\n")]
rules = [rule.split(":")[1].strip().split(" or ") for rule in file[0]]
ruleDict = {}

for rule in file[0]:
    ranges = rule.split(":")[1].strip().split(" or ")
    outList = []
    for rangee in ranges:
        outList.append(lambda x : x in range(int(rangee[0]), int(rangee[1]) + 1))
    ruleDict[rule.split(":")[0].strip()] = outList


tickets = [ticket.split(",") for ticket in file[2][1:]]
realTickets = []

def checkNumberInRules(rules, number):
    for line in rules:
        for rule in line:
            rrange = rule.split("-")
            if number in range(int(rrange[0]), int(rrange[1]) + 1):
                return True
    return False

def part_one():
    n = 0
    for ticket in tickets:
        valid = True
        for value in ticket:
            if not checkNumberInRules(rules, int(value)):
                valid = False
                n += int(value)
        if valid:
            realTickets.append(ticket)
    return n

indexes = [x for x in ruleDict.keys()]
possibleValues = []

for i in range(len(tickets[0])):
    possibleValues.append(indexes)


print(len(possibleValues))

for ticket in realTickets[4:5]:
    for i in range(len(ticket)): # for the numbers in the ticket
        validField = False
        print(ticket[i])
        for test in ruleDict[indexes[i]]: # for the tests in that ticket number
            validField = validField or test(ticket[i])
            # print(validField)
        if not validField:
            print("")
            # print("not valid")
        else:
            print("valid")

if __name__ == "__main__":
    print("Part 1:", part_one())