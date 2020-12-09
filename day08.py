rulesRaw = [x.split(" ") for x in open("input/day08.txt").read().split("\n")]

def part_one():
    return step_through_instructions(rulesRaw, [True] * len(rulesRaw))[1]

def step_through_instructions(instruction_list, nops):
    ptr, acc = 0, 0
    instructionCount = [0] * len(instruction_list)
    noppedThisLoop = False

    while ptr in range(len(instruction_list)) and instructionCount[ptr] != 1:
        instructionCount[ptr] += 1
        instruction, arg = instruction_list[ptr][0], int(instruction_list[ptr][1])
        if instruction == "nop":
            ptr += 1
        elif instruction == "acc":
            acc += arg
            ptr += 1
        elif instruction == "jmp":
            if not noppedThisLoop and not nops[ptr]:
                nops[ptr] = True
                noppedThisLoop = True
                ptr += 1
            else:
                ptr += arg
        else:
            print("unknown", instruction_list[ptr])
    return ptr, acc, nops

def part_two():
    ptr, acc = 0, 0
    nopped = [False] * len(rulesRaw)
    while ptr in range(len(rulesRaw)):
        ptr, acc, nopped = step_through_instructions(rulesRaw, nopped)
    return acc



if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())
    # brute_instructions(rulesRaw)