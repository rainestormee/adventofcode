inputs = [int(line) for line in open("resources/input.txt")]


def part_one():
  start = inputs[0]
  changes = 0
  for x in range(1, len(inputs)):
    if inputs[x] > start:
      changes += 1
      start = inputs[x]
    else:
      start = inputs[x]
  return changes

def part_two():
  changes = 0
  start = inputs[0] + inputs[1] + inputs[2]
  for x in range(3, len(inputs) - 2):
    temp = inputs[x] + inputs[x + 1] + inputs[x + 2]
    if temp > start:
      changes += 1
    start = temp
  return changes

print(part_one())
print(part_two())
