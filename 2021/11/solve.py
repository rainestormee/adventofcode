raw = [[int(y) for y in x.strip()] for x in open('resources/input.txt')]

def get_around(x, y):
	around = []
	for i in range(x - 1, x + 2):
		for j in range(y - 1, y + 2):
			if (not ((i == x) and (j == y))) and (0 <= i and i < len(raw)) and (0 <= j and j < len(raw[0])):
				around.append((i, j))
	return around

def step(raw):
	flashes = []
	for line in range(len(raw)):
		for octu in range(len(raw[line])):
			raw[line][octu] = raw[line][octu] + 1
	flashed = True
	while flashed:
# 		print("looping")
		flashed = False
		for line in range(len(raw)):
			for octu in range(len(raw[line])):
				if 9 < raw[line][octu] and not (line, octu) in flashes:
					flashed = True
					flashes.append((line, octu))
					for (n, m) in get_around(line, octu):
						raw[n][m] = raw[n][m] + 1
	for (n, m) in flashes:
		raw[n][m] = 0
	return len(flashes)

def pprint(raw):
	for line in raw:
		for n in line:
			print(n, end='')
		print('')
flashes = 0

octopi = len(raw) ** 2
i = 0
flashed = 0
while flashed != octopi:
    flashed = step(raw)
    flashes += flashed
    i += 1
    if i == 99:
        print(flashes)
print(i)
pprint(raw)
