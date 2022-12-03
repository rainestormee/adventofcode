import re
inputa = [[j.split(":") for j in re.split("[\\n ]", i)] for i in open("input/day04.txt").read().split("\n\n")]

count = 0
validCount = 0

for record in inputa:
    required = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
    has = [False, False, False, False, False, False, False]
    valid = [False, False, False, False, False, False, False]
    for field in record:
        if len(field) == 1:
            # if field[0] in required
             for i in range(len(required)):
              if required[i] == field[0]:
                has[i] = True
             continue
        print(field)
        r = (field[0], field[1])
        if r[0] == "ecl":
            has[0] = True
            if r[1] in (["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
                valid[0] = True
        elif r[0] == "pid":
            has[1] = True
            if len(r[1]) == 9:
                valid[1] = True
        elif r[0] == "hcl":
            has[3] = True
            validChar = True
  
            for c in r[1]:
               print(c) 
               if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "e", "f", "#"]:
                    print("no")
                    validChar = False
            if validChar and len(r[1]) == 7:
                valid[3] = True
        elif r[0] == "eyr":
            has[2] = True
            if int(r[1]) in range(2020, 2030 + 1):
                valid[2] = True
        elif r[0] == "byr":
            has[4] = True
            if int(r[1]) in range(1920, 2002 + 1):
                valid[4] = True
        elif r[0] == "iyr":
            has[5] = True
            if int(r[1]) in range(2010, 2020 + 1):
                valid[5] = True
        elif r[0] == "hgt":
            has[6] = True
            height = r[1].split("cm")
            if "in" in height[0]:
               height = height[0].split("in")
               if int(height[0]) in range(59, 76 + 1):
                   valid[6] = True 
 
            else:
               print("cm") 
               if int(height[0]) in range(150, 193+1):
                   valid[6] = True

            print("=====> ", height)
          
      # for i in range(len(required)):
        #     if required[i] == field[0]:
        #        has[i] = True
    print(has)
    print(valid)           
    if all(has):
        count += 1
        if all(valid):
            validCount += 1
print(count, validCount)
