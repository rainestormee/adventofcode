from collections import Counter

raw = [[y for y in x.strip().split("-")] for x in open('resources/input.txt')]

connections = {}

for (a, b) in raw:
	if a in connections:
		connections[a].append(b)
	else:
		connections[a] = [b]	
	if b in connections:
		connections[b].append(a)
	else:
		connections[b] = [a]

def find_paths(start, end, arr, paths):
	for dirr in connections[start]:
		if ((dirr in arr) and dirr.islower()) or (not dirr in connections and dirr != end):
			continue
		temp = arr[:]
		temp.append(dirr)
		if dirr == end:
			paths.append(temp)
		else:
			paths.extend(find_paths(dirr, end, temp, []))
	return paths		

def path_two(start, end, arr, paths, real_start):
	for dirr in connections[start]:
		if dirr == real_start:
#			print(dirr)
			continue
		if dirr.islower() and (dirr in arr):
			counts = Counter(arr)
			list = [c for c in counts.elements() if c.islower() and counts[c] > 1]
			if len(list) > 1:
#				print(len(list))
				continue
		if (not dirr in connections and dirr != end):
			continue
		temp = arr[:]
		temp.append(dirr)
		if dirr == end:
			paths.append(temp)
		else:
			paths.extend(path_two(dirr, end, temp, [], real_start))
	return paths
# print(connections)
a = path_two('start', 'end', ['start'], [], 'start')
b = []
for x in a:
	if x not in b:
		b.append(x)
print(len(b))
# print(b)
