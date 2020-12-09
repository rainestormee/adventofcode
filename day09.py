inputList = [int(x) for x in open("input/day09.txt").read().split("\n")]

preambleLength = 25
data = [inputList[x] for x in range(preambleLength + 1, len(inputList))]
preamble = [inputList[x] for x in range(0, preambleLength + 1)]

def part_one():
    for x in range(len(data)):
        preamble.append(data[x])
        preamble.remove(preamble[0])
        found = False
        for y in preamble:
            if (data[x] - y) in preamble:
                found = True
        if not found:
            return data[x]

def part_two(target):
    numbers = []
    for x in data:
        numbers.append(x)
        while sum(numbers) > target:
            numbers.remove(numbers[0])
        if sum(numbers) == target:
            return min(numbers) + max(numbers)


if __name__ == "__main__":
    one = part_one()
    print("Part 1:", one)
    print("Part 2:", part_two(one))


