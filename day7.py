rulesRaw = [x for x in open("./input/day7.txt").read().split(".\n")]

print(rulesRaw)

rules = {

}

def walk(start_point):
    if start_point not in rules:
        print(start_point, "not in")
        return False
    if "shiny gold bag" in rules[start_point] or "shiny gold bags" in rules[start_point]:
        print(start_point, "found shiny")
        return True
    if rules[start_point][0] == "":
        print(start_point, "dead end")
        return False
    return any(walk(x) for x in rules[start_point])

for x in rulesRaw:
    rule = x.split("contain")
    container = rule[0].strip().replace("bags", "bag")
    inside = [x.strip()[2:].strip().replace(".", "").replace("other bags", "").replace("bags", "bag") for x in rule[1].split(", ")]
    print(container, inside)
    rules[container] = inside

counter = 0
correct = []

for x in rules:
    print(x, rules[x])
    print("Starting to walk for {}".format(x))
    if walk(x):
        print("True")
        correct.append(x)
        counter += 1

if __name__ == "__main__":
    print(counter)