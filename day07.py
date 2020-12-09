rulesRaw = [x for x in open("input/day07-test.txt").read().split(".\n")]

print(rulesRaw)

rules = {

}
amounts = {

}
bags = {

}

def walk(start_point):
    if start_point not in rules:
        return False
    if "shiny gold bag" in rules[start_point] or "shiny gold bags" in rules[start_point]:
        return True
    if rules[start_point][0] == "":
        return False
    return any(walk(x) for x in rules[start_point])

bagList = []

def count(outer_bag, multiplier):
    return 0 if "" in bags[outer_bag] else sum([multiplier * (bags[outer_bag][bag] + count(bag, bags[outer_bag][bag])) for bag in bags[outer_bag]])

for x in rulesRaw:
    rule = x.split("contain")
    container = rule[0].strip().replace("bags", "bag")
    inside = [x.strip()[2:].strip().replace(".", "").replace("other bags", "").replace("bags", "bag") for x in rule[1].split(", ")]
    amount = []
    for y in rule[1].split(", "):
        try:
            amount.append(int(y[:2].strip()))
        except ValueError:
            amount.append(0)

    rules[container] = inside
    baggage = {}
    for i in range(len(inside)):
        baggage[inside[i]] = amount[i]
    bags[container] = baggage
counter = 0
correct = []

for x in rules:
    if walk(x):
        correct.append(x)
        counter += 1

print(bags)

if __name__ == "__main__":
    print(count("shiny gold bag", 1))