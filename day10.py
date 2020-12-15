inputList = sorted([int(x) for x in open("input/day10.txt").read().split("\n")])
joltageRating = inputList[-1] + 3

def part_one():
    one = 0
    three = 1
    for i, x in enumerate(inputList):
        if i == 0:
            diff = x
        elif i == len(inputList):
            diff = 3
        else:
            diff = x - inputList[i - 1]
        if diff == 1:
            one += 1
        elif diff == 3:
            three += 1
    return three * one

mem = {}

def search_for_next(start):
    output = 0
    for i in range(0, 3):
        max = joltageRating - 3
        offset = start + i + 1
        if offset == max:
            output += 1
        elif offset in inputList:
            if offset in mem:
                output += mem[offset]
            else:
                amount = search_for_next(offset)
                mem[offset] = amount
                output += amount
    return output



def part_two():
    return search_for_next(0)

if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())
