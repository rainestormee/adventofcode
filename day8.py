from time import sleep
rulesRaw = [x.split(" ") for x in open("./input/day8.txt").read().split("\n")]

print(rulesRaw)

def step_through_instructions(instruction_list):
    ptr, acc = 0, 0
    instructionCount = [0] * len(instruction_list)
    while instruction_list[ptr] != 1:
        instructionCount[ptr] += 1
        instruction, arg = instruction_list[ptr][0], int(instruction_list[ptr][1])
        print(acc, rulesRaw[ptr])
        if instruction == "nop":
            ptr += 1
        elif instruction == "acc":
            acc += arg
            ptr += 1
        elif instruction == "jmp":
            ptr += arg
        else:
            print("unknown", instruction_list[ptr])

    return acc

nopped = [False] * len(rulesRaw)

def brute_instructions(instruction_list):
    ptr = 0

    while ptr in range(len(instruction_list)):
        ptr, acc = 0, 0
        instructionCount = [0] * len(instruction_list)
        noppedThisLoop = False

        while ptr in range(len(instruction_list)) and instructionCount[ptr] < 1:
            instructionCount[ptr] += 1
            instruction, arg = rulesRaw[ptr][0], int(rulesRaw[ptr][1])
            # print(instructionCount[ptr], acc, rulesRaw[ptr])
            if instruction == "nop":
                ptr += 1
            elif instruction == "acc":
                acc += arg
                ptr += 1
            elif instruction == "jmp":
                if not noppedThisLoop and not nopped[ptr]:
                    print("nopping")
                    nopped[ptr] = True
                    noppedThisLoop = True
                    ptr += 1
                else:
                    ptr += arg
            else:
                print("unknown", rulesRaw[ptr])
    print(acc)



if __name__ == "__main__":
    brute_instructions(rulesRaw)