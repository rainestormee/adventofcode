raw = [[int(x) for x in line.strip()] for line in open("input.txt")]

def corners(i, j):
  allp = []
  if not i == 0:
    allp.append(((i - 1), j))
  if not i + 1 == len(raw): 
    allp.append(((i + 1), j))
  if not j + 1 == len(raw[0]):
    allp.append((i, j + 1))
  if not j == 0:
    allp.append((i, j - 1))
  return allp

lows = []
for i in range(len(raw)):
  for j in range(len(raw[i])):
    dip = True
    for (p, q) in corners(i, j):
        if raw[p][q] <= raw[i][j]:
          dip = False
    if dip:
      lows.append((i, j))

score = 0
for (i, j) in lows:
  score += raw[i][j] + 1

print("Part One:", score)

def get_corners(i, j):
  temp = corners(i, j)
  to_check = []
  for (x, y) in temp:
    if not raw[x][y] == 9 and raw[x][y] > raw[i][j]:
      to_check.append((x, y))
  return to_check
  
sizes = []

for (i, j) in lows:

  temp = get_corners(i, j)
  members = []
  size = len(temp) + 1
  
  while not len(temp) == 0:
    (a, b) = temp.pop()
    is_in = False
    for (n, m) in members:
      if n == a and m == b:
        is_in = True
        size = size - 1
    
    t = get_corners(a, b)
    size += len(t)
    temp.extend(t)
    if not is_in:
      members.append((a, b))

  sizes.append(size)


answer = 1
for n in sorted(sizes, reverse=True)[:3]:
  answer *= n
print("Part Two:", answer)


    
