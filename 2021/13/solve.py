raw = [x.strip() for x in open('resources/input.txt')]
split = raw.index('')
grid = [[int(y) for y in x.split(',')] for x in raw[:split]]
folds = [x.replace('fold along','').strip().split('=') for x in raw[split+1:]]

def count_dots(grid):
	out = []
	for (x, y) in grid:
		if (x, y) not in out:
			out.append((x, y))
	print(len(out))

first = True
for fold in folds:
	if fold[0] == 'y':
		for i in range(len(grid)):
			x,y = grid[i]
			if y > int(fold[1]):
				grid[i][1] = 2*int(fold[1]) - y
			#	print(f"{x},{y} -> {x},{2*int(fold[1])-y}")
			else:
				pass
			
	if fold[0] == 'x':
		# fold along x axis
		for i in range(len(grid)):
			x,y = grid[i]
			if x > int(fold[1]):
				grid[i][0] = 2*int(fold[1]) - x
		pass


	if first:
		count_dots(grid)
		first = False

biggest_x = 0
biggest_y = 0
for x,y in grid:
	if x > biggest_x:
		biggest_x = x
	if y > biggest_y:
		biggest_y = y
print_g = [['.' for y in range(biggest_y + 1)] for x in range(biggest_x + 1)]
for x,y in grid:
	print_g[x][y] = '#'

for x in list(zip(*print_g)):
	for y in x:
		print(y,end='')
	print('')
