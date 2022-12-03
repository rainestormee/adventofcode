raw = [line.strip() for line in open("input.txt")]

match = {
  ')': '(',
  '}': '{',
  '>': '<',
  ']': '[',
  '(': ')',
  '{': '}',
  '<': '>',
  '[': ']'
}
points = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137
}

def checkline(line):
  brackets = []
  for x in line:
    if x in ['(', '<', '{', '[']:
      brackets.append(x)
    if x in [')', '>', '}', ']']:
      if not brackets.pop() == match[x]:
        return x

def complete(line):
  brackets = []
  for x in line:
    if x in ['(', '<', '{', '[']:
      brackets.append(x)
    if x in [')', '>', '}', ']']:
      if not brackets.pop() == match[x]:
        return (False, [])
  return (True, [match[x] for x in brackets][::-1])
 
illegals = {')': 0, ']': 0, '}': 0, '>': 0}
p = 0

comp_score = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4
}  
all_scores = []

for line in raw:
  (a, b) = complete(line)
  if a:
    final = 0
    for c in b:
      final *= 5
      final += comp_score[c]
    all_scores.append(final)

  x = checkline(line)
  if x in [')', '>', '}', ']']:
    p += points[x]

print('Part One', p)
 
all_scores.sort()

print('Part Two',all_scores[int((len(all_scores) + 1) / 2) - 1])
