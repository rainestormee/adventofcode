from functools import reduce
print("" if (c := [[a.split("\n")] for a in open("./input/day6.txt").read()[:-1].split("\n\n")]) and print("Part 1:", sum(sum(len(reduce(lambda x, y: set(x) & set(y), list(a))) for a in b) for b in c)) else "Part 2:", sum(sum(len(reduce(lambda x, y: set(x) | set(y), list(a))) for a in b) for b in c))
