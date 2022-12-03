inp = [[int(y) for y in x.split("\n") if y != ''] for x in open("input.txt").read().split("\n\n") if x != '']

most = 0
second = 0
third = 0

for x in inp:
    summ = 0
    for y in x:
        summ += y
    if summ > most:
        third = second
        second = most
        most = summ
    elif summ > second:
        third = second
        second = summ
    elif summ > third:
        third = summ

print(most)
print(most + second + third)
