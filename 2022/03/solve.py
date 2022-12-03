inp = [x for x in open("input.txt").read().split("\n") if x != '']

score = 0

def scores(a):
	if a.isupper():
		return ord(a) - 36 - 2
	return  ord(a) - 96

for x in inp:
	items = len(x) // 2
	common = []
	print(x)
	print(x[:items], x[items:])
	for i in x[:items]:
		if i in x[items:]:
			if i not in common:
				common.append(i)

	for a in common:
		score += scores(a)

print(score)


n = 0
ns = 0
while True:
	try:
		fst = inp[n]
		snd = inp[n + 1]
		thr = inp[n + 2]

		main = ''
		sub = []

		for i in fst:
			if i in snd:
				if i not in sub:
					sub.append(i)
				if i in thr:
					main = i
			elif i in thr:
				if i not in sub:
					sub.append(i)
		for i in snd:
			if i in thr:
				sub.append(i)
		
		ns += scores(main)
		n += 3
	except:
		break
print(ns)
