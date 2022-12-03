numbers = [int(line) for line in open("input/day01.txt")]

def part_one():
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            a, b = numbers[i], numbers[j]
            if (a + b == 2020):
                return (a * b)

def part_two():
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            for k in range(j, len(numbers)):
                a, b, c = numbers[i], numbers[j], numbers[k]
                if (a + b + c == 2020):
                    return (a * b * c)

if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())
