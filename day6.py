groups = [[a.split("\n")] for a in open("./input/day6.txt").read()[:-1].split("\n\n")]

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

print(groups)
print("Total Groups", len(groups))
majorCount = 0
for group in groups: # the first entry
    for answer in group:
        letters = [False] * 26
        count = 0
        for confirm in answer:
            for letter in confirm:
                if not letters[ord(letter) - 97]:
                    letters[ord(letter) - 97] = True
                    count += 1
        majorCount += count
print(majorCount)


majorCount = 0
for group in groups: # the first entry
    for answer in group:
        count = 0
        letters = list(answer[0])
        for confirm in answer:
            print(letters, "/\\", list(confirm), "==", intersection(letters, list(confirm)))
            letters = intersection(letters, list(confirm))
            # print(sorted(confirm.split()))
            #for letter in confirm:
            #    print(letter, end="")
            #print(" ", end="")
        majorCount += len(letters)
print(majorCount)