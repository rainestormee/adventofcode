lines, letter, password, least, most = [i[:-1] for i in open("input/day02.txt")], [], [], [], []

# Parsing the input file into variables
for i in lines:
    line = i.split(" ")
    numbs = line[0].split("-")
    least.append(int(numbs[0]))
    most.append(int(numbs[1]))
    letter.append(line[1][0])
    password.append(line[2])

def part_one():
    valid = 0
    for i in range(0, len(lines)):
        matches = 0
        for c in password[i]:
            if str(c) == str(letter[i]):
                matches += 1
        if matches in range(least[i], most[i] + 1):
            valid += 1
    return valid

def part_two():
    out = 0
    for i in range(0, len(lines)):
        pw = password[i]
        # exclusive or
        if ((pw[least[i] - 1] == letter[i]) != (pw[most[i] - 1] == letter[i])):
            out += 1
    return out

print("Part 1:", part_one())
print("Part 2:", part_two())
