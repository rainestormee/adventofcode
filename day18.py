input_ = open("./input/day18.txt").read().split("\n")

calculationsMem = {}

def calculate(calcStr, addPrecedence):
    while "(" in calcStr:
        open_, close = findNextInnerBracket(calcStr)
        sliced = calcStr[open_: close + 1]
        calcStr = calcStr.replace(sliced, str(calculate(sliced[1:-1], addPrecedence)))
    calc = calcStr.split(" ")
    while len(calc) != 1:
        if addPrecedence and "+" in calc:
            newCalc = []
            star = calc.index("+")
            res = doOp(int(calc[star - 1]), "+", int(calc[star + 1]))
            if len(calc) > 3:
                for i in range(len(calc)):
                    if i == star - 1 or i == star + 1:
                        continue
                    elif i == star:
                        newCalc.append(res)
                    else:
                        newCalc.append(calc[i])
            else:
                newCalc = [res]
            calc = newCalc
        else:
            first, op, second = int(calc[0]), calc[1], int(calc[2])
            newCalc = [doOp(first, op, second)]
            if len(calc) > 3:
                for e in calc[3:]:
                    newCalc.append(e)
            calc = newCalc
    return calc[0]

def doOp(first, op, second):
    stringed = str(first) + op + str(second)
    revStringed = str(second) + op + str(first)
    if stringed not in calculationsMem:
        if op == "+":
            res = first + second
            calculationsMem[stringed] = res
            calculationsMem[revStringed] = res
        elif op == "-":
            calculationsMem[stringed] = first - second
        elif op == "/":
            calculationsMem[stringed] = first / second
        else:
            res = first * second
            calculationsMem[stringed] = res
            calculationsMem[revStringed] = res
    return calculationsMem[stringed]

def findNextInnerBracket(brackStr):
    indexes = [0, 0]
    if "(" not in brackStr:
        return indexes
    for i in range(len(brackStr)):
        if brackStr[i] == "(":
            indexes[0] = i
        elif brackStr[i] == ")":
            indexes[1] = i
            return indexes

def _sum_(precedence):
    sum_ = 0
    for x in input_:
        sum_ += calculate(x, precedence)
    return sum_

def part_one():
    return _sum_(False)

def part_two():
    return _sum_(True)

if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())
