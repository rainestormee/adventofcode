inp = [[y for y in x.split(" ")] for x in open("input.txt").read().split("\n") if x != '']

score = 0
lose = 0
draw = 3
win = 6
themROCK = 'A'
themPAPER = 'B'
themSCISSORS = 'C'
youROCK = 'X'
youPAPER = 'Y'
youSCISSORS = 'Z'

for exa in inp:

    them = exa[0]
    you = exa[1]
    if them == themROCK:
        if you == youROCK:
            score += draw
        elif you == youPAPER:
            score += win
        else:
            score += lose
    elif them == themPAPER:
        if you == youROCK:
            score += lose
        elif you == youPAPER:
            score += draw
        else:
            score += win
    elif them == themSCISSORS:
        if you == youROCK:
            score += win
        elif you == youPAPER:
            score += lose
        else:
            score += draw
    
    if you == youROCK:
        score += 1
    elif you == 'Y':
        score += 2
    else:
        score += 3

score = 0

for exa in inp:
    them = exa[0]
    strat  = exa[1]

    if strat == 'X': # lose, draw, win
        if them == themROCK:
            score += 3
        elif them == themPAPER:
            score += 1
        else:
            score += 2
    elif strat  == 'Y':
        score += draw
        if them == themROCK:
            score += 1
        elif them == themPAPER:
            score += 2
        else:
            score += 3
    else:
        score += win
        if them == themROCK:
            score += 2
        elif them == themPAPER:
            score += 3
        else:
            score += 1



print(score)
