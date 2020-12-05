inputa = [a for a in open("./input/day5.txt").read().split("\n")[:-1]]

highest = 0
seats = []

for i in inputa:
    seat = (i[:7], i[-3:])
    amount = (0, 127)
    seatN = 0
    aisleN = 0
    row = (0, 7)

    print("-2 = ", seat[0][:-1])
    for j in seat[0][:-1]:
        print(amount, j)
        middle = (amount[1] + amount[0]) // 2
        if j == 'B':
            amount = (middle + 1, amount[1])
        else:
            amount = (amount[0], middle)

    if seat[0][-1] == 'B':
        seatN = amount[1]
    else:
        seatN = amount[0]

    for j in seat[1][:-1]:
        middle = (row[0] + row[1]) // 2
        if j == 'R':
            row = (middle + 1, row[1])
        else:
            row = (row[0], middle)
    if seat[1][-1] == 'R':
        aisleN = row[1]
    else:
        aisleN = row[0]

    print(seat, seatN, aisleN)
    sid = seatN * 8 + aisleN
    if sid > highest:
        highest = sid
    seats.append(sid)



print(highest)
seats.sort()
seat = seats[0]
for i in sorted(seats):
    if i == seat + 2:
        print(i - 1)
    seat = i