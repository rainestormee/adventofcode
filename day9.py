import sys

inputList = [int(x) for x in open("./input/day9.txt").read().split("\n")]

preambleLength = 25
preamble = []
data = [inputList[x] for x in range(preambleLength + 1, len(inputList))]

def refresh_pre(start):
    global preamble
    preamble = [inputList[x] for x in range(start, start + preambleLength + 1)]

if __name__ == "__main__":
    target = 23278925
    numbers = []
    for x in data:
        numbers.append(x)
        while sum(numbers) > target:
            numbers.remove(numbers[0])
        if sum(numbers) == target:
            print(sum(numbers))
            print(numbers)
            print(min(numbers))
            print(max(numbers))
            print(min(numbers) + max(numbers))
            break


if __name__ == "__pain__":
    refresh_pre(0)
    print(preamble)
    print(data)
    for x in range(len(data)):
        found = False
        refresh_pre(x)
        print("x", data[x])
        print("pre", preamble)
        for y in preamble:
            print("-", data[x] - y)
            for z in preamble:
                print("z", z)
                if z == (data[x] - y):
                    print("found", y, "+", (data[x] - y), "=", x)
                    found = True
        if not found:
            print("not found", data[x])
            sys.exit()
