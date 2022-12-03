import sys; sys.path.insert(0, '/home/raine/programming/python/aoc/aoc'); import aoc

raw = aoc.open_file('resources/input.txt')

poly = raw[0]
rules = {}
for x in raw[2:]:
	rule = x.split(' -> ')
	rules[rule[0]] = rule[1]

def part_one(n, poly, rules):
	for i in range(n):
		output = ''

		for x in range(len(poly) - 1):
			output = f'{output}{poly[x]}'
			if poly[x:(x+2)] in rules:
				output = f'{output}{rules[poly[x:(x+2)]]}'
		output = f'{output}{poly[len(poly) - 1]}'
		poly = output

	counts = {}
	for x in poly:
		aoc.increment(counts, x, 1)

	counts = counts.values()
	return poly, max(counts) - min(counts)

def part_two(n, poly, rules, extra):
	for ignored in range(n):
		new_poly = {}
		deletes = []

		for rule in rules:
			if rule in poly:
				first = f'{rule[0]}{rules[rule]}'
				second = f'{rules[rule]}{rule[1]}'
				aoc.increment(new_poly, first, poly[rule])
				aoc.increment(new_poly, second, poly[rule])
				deletes.append(rule)

		for x in deletes:
			if x in poly:
				del poly[x]

		for x in new_poly:
			aoc.increment(poly, x, new_poly[x])

	counts = {}

	for p in poly:
		aoc.increment(counts, p[0], poly[p])

	counts[extra] += 1
	counts = counts.values()
	return poly, max(counts) - min(counts)


poly, one = part_one(10, poly, rules)
polym = {}
last = ''
for x in poly:
	if last != '':
		el = f'{last}{x}'
		aoc.increment(polym, el, 1)
	last = x
print('Part One:' , one)
print('Part Two:', part_two(30, polym, rules, poly[-1])[1])
