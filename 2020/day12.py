from math import cos, sin, radians
instructions = [(x[0], int(x[1:])) for x in open("./input/day12.txt").read().split("\n")]
# print(instructions)

def part_one():
    ship = [0, 0, 90] # North, East, Angle
    for instruction in instructions:
        op, arg = instruction
        if op == "E":
            ship[1] += arg
        elif op == "N":
            ship[0] += arg
        elif op == "W":
            ship[1] -= arg
        elif op == "S":
            ship[0] -= arg
        elif op == "F":
            if ship[2] == 90:
                ship[1] += arg
            elif ship[2] == 180:
                ship[0] -= arg
            elif ship[2] == 270:
                ship[1] -= arg
            elif ship[2] == 0:
                ship[0] += arg
            else:
                print("Unexpected direction, ", ship[3])
        elif op in ["L", "R"]:
            ship[2] = (ship[2] + (arg if op == "R" else -arg)) % 360
    return ship

def part_two():
    ship = [0, 0] # North, East
    waypoint = [1, 10] # North, East
    # print("({}, {}) ({}, {})".format(ship[0], ship[1], waypoint[0], waypoint[1]))
    for instruction in instructions:
        op, arg = instruction
        if op == "F":
            ship[0], ship[1] = ship[0] + arg * waypoint[0], ship[1] + arg * waypoint[1]
        elif op == "N":
            waypoint[0] += arg
        elif op == "S":
            waypoint[0] -= arg
        elif op == "E":
            waypoint[1] += arg
        elif op == "W":
            waypoint[1] -= arg
        elif op in ["L", "R"]:
            theta = radians(arg if op == "L" else -arg)
            waypoint[0], waypoint[1] = round(sin(theta) * waypoint[1] + cos(theta) * waypoint[0]), round(cos(theta) * waypoint[1] - sin(theta) * waypoint[0])
        # print("{}{} : ({}, {}) ({}, {})".format(op, arg, ship[0], ship[1], waypoint[0], waypoint[1]))
    return ship

def answer(r):
    return abs(r[0]) + abs(r[1])

if __name__ == "__main__":
    print("Part 1:", answer(part_one()))
    print("Part 2:", answer(part_two()))