from functools import reduce
print("" if (c := [[a.split("\n")] for a in open("./input/day6.txt").read()[:-1].split("\n\n")]) and print("Part 1:", sum(sum(len(reduce(lambda x, y: set(list(x) + list(y)), list(a))) for a in b) for b in c), "\nPart 2:", sum(sum(len(reduce(lambda x, y: list([v for v in x if v in y]), list(a))) for a in b) for b in c)) else "- Ryan Arrowsmith")