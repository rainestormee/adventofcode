raw = [[[int(y) for y in x.split(",")] for x in line.strip().split(" -> ")] for line in open("resources/input.txt")]

def printg(grid):
  return
  for x in grid:
    for n in x:
      if n == 0:
        print('.',end='')
      else:
        print(n,end='')
    print("")
  print("")
    
max_x = 0
max_y = 0

processed = []
part_two = []

for a in raw:
  if a[0][0] == a[1][0] or a[0][1] == a[1][1]:
    processed.append(a)
  else:
    part_two.append(a)  
    
  l_max_x = max(a[0][0],a[1][0]) 
  l_max_y = max(a[0][1],a[1][1])
    
  if l_max_x > max_x:
    max_x = l_max_x
  if l_max_y > max_y:
    max_y = l_max_y
    
# x then -y

# grid = [[0 for x in range(1000000)] for y in range(1000000)]
# grid = [[0 for x in range(max_y + 1)] for y in range(max_x + 1)]
grid = {}

def increment(i, j):
  if (i, j) in grid:
    grid[(i,j)] = grid[(i,j)] + 1
  else:
    grid[(i,j)] = 1

for line in processed:


  if line[0][0] == line[1][0]:
    smaller = min(line[0][1],line[1][1])
    bigger = max(line[0][1],line[1][1])
    
    for i in range(smaller, bigger + 1):
      increment(i,line[0][0])
      
      
     
  elif line[0][1] == line[1][1]:
    smaller = min(line[0][0],line[1][0])
    bigger = max(line[0][0],line[1][0])
    for i in range(smaller, bigger + 1):
      increment(line[0][1],i)
      
#   printg(grid)
count = 0
count = 0
for line in grid:
  if (grid[line] >= 2):
    count += 1

print("Part One:",count)
# printg(grid)

errors = 0 
for line in part_two:

  y_m = 1
  x_m = 1
  if (line[0][0] > line[1][0]):
    y_m = -1
  if (line[1][0] > line[1][1]):
    x_m = -1
  
  start = line[0][0]
  s_2 = line[0][1]
  end = line[1][0] + y_m
  
  while (not start == end):
    increment(s_2,start)
    start += y_m
    s_2 += x_m

 
count = 0
for line in grid:
  if (grid[line] >= 2):
    print(line)
    count += 1

print("Part Two:", count)
print(errors)
