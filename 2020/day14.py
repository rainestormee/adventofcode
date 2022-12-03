raw_input = open("./input/day14.txt").read().split("\n")
# print(raw_input)

def num_to_array(value):
    return list(format(value, '036b'))

def print_arr(arr):
    print([str(x) for x in arr], end='')
    print('')

def return_mask(mask, number):
    return int(return_maskk(mask, number, False), 2)

def return_maskk(mask, number, xor):
    number = int(number)
    print(mask, number)
    if isinstance(number, int):
        number = num_to_array(number)
    output = ['0'] * 36
    for x in range(len(mask)):
        ma, nu = mask[x], number[x]
        # print(ma, nu)
        if ma == 'X' :
            if not xor:
                output[x] = nu
            else:
                output[x] = 'X'
        else:
            if not xor:
                output[x] = ma
            else:
                if ma == '0':
                    output[x] = nu
                else:
                    output[x] = '1'
                # output[x] = str(int(ma, 2) ^ int(nu, 2))
    return ''.join([str(x) for x in output])


def setup_mask():
    mask = ['X'] * 36
    mask[-2] = 0
    mask[-7] = 1
    return mask

def dict_sum(mem):
    sum = 0
    for x in mem:
        sum += int(mem[x])
    return sum

def part_one():
    mem = {}
    mask = ""
    for input_line in raw_input:
        if input_line.startswith("mask"):
            # print(">> Using new mask")
            mask = input_line.split(" ")[2]
        else:
            # print(input_line)
            add = int(input_line.split(" ")[0].replace("mem[", "").replace("]", "")) # address
            val = input_line.split(" ")[2] # value
            mem[add] = return_mask(mask, int(val))
    return dict_sum(mem)

def get_addresses(mask):
    addresses = []
    if 'X' not in mask:
        return mask
    o = mask.replace('X', '0', 1)
    one = get_addresses(o)
    if isinstance(one, list):
        for x in one:
            addresses.append(x)
    else:
        addresses.append(one)
    t = mask.replace('X', '1', 1)
    two = get_addresses(t)
    if isinstance(two, list):
        for x in two:
            addresses.append(x)
    else:
        addresses.append(two)
    return addresses

def part_two():
    mem = {}
    mask = ""
    for input_line in raw_input:
        if input_line.startswith("mask"):
            # print(">> Using new mask")
            mask = input_line.split(" ")[2]
        else:
            # print(input_line)
            add = int(input_line.split(" ")[0].replace("mem[", "").replace("]", "")) # address
            val = input_line.split(" ")[2] # value
            addr = return_maskk(mask, add, True)
            for loc in get_addresses(addr):
                mem[loc] = val
            # mem[add] = return_mask(mask, int(val))
    return dict_sum(mem)

if __name__ == "__main__":
    # print(part_one())
    # print(get_addresses("00000000000000000000000000000001X0XX"))
    print(part_one())
    print(part_two()) # 1714597612056
