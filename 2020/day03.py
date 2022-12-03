from functools import reduce

inputa = [[j for j in i[:-1]] for i in open("input/day03.txt")]

def part_one():
    return get_trees((1, 3))

def part_two():
    starts = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    return reduce(lambda x, y: x * y, [get_trees(i) for i in starts])
    

def get_trees(startPos):
    pos = startPos
    count = 0
    bottom = len(inputa)
    while pos[0] < bottom:
        space = inputa[min(pos[0], bottom - 1)][pos[1]]
        if space == '#':
           count += 1
        pos = (pos[0] + startPos[0], (pos[1] + startPos[1]) % len(inputa[0]))
    return count

print("Part 1:", part_one())
print("Part 2:", part_two())
