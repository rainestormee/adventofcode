inp = [[y.split(" ") for y in x.strip().split(" | ")] for x in open("resources/test.txt")]

len_to_possible = {
  2: [1],
  3: [7],
  4: [4],
  5: [2, 3, 5],
  6: [0, 6, 9],
  7: [8]
}

number_to_states = {
  0: [1, 2, 3, 5, 6, 7],
  1: [3, 6],
  2: [1, 3, 4, 5, 7],
  3: [1, 3, 4, 6, 7],
  4: [2, 3, 4, 6],
  5: [1, 2, 4, 6, 7],
  6: [1, 2, 4, 5, 6, 7],
  7: [1, 3, 6],
  8: [1, 2, 3, 4, 5, 6, 7],
  9: [1, 2, 3, 4, 6, 7]
}

n = 0
for x in inp:
  for y in x[1]:
    if (len(len_to_possible[len(y)]) == 1):
      n += 1
print("Part One", n)
big_total = 0
for PAIN in inp:
  known = {}
  data = PAIN[0]
  list.sort(data, key=len)
  for x in data:
    for n in len_to_possible[len(set(x))]:
      if n == 1:
         known[3] = x
         known[6] = x
      if n == 7:
          known[1] = list(set(known[3]) ^ set(x))[0]
      if n == 4:
          known[2] = "".join(set(known[3]) ^ set(x))
          known[4] = known[2]
      if n == 2 or n == 3 or n == 5:
          
          remaining = list(set(known[4]) ^ set(x))
          if (len(remaining) == 3):
         
            six_s = set(remaining) ^ set(known[1])
            for z in six_s:
              if z in known[6]:
                known[6] = z
              else:
                known[7] = z
            letters = ""
            for xi in known:
              letters += known[xi]
            if len(set(letters)) == 6:
              known[5] = list(set(letters) ^ set("abcdefg"))[0]
            
      if n == 6 or n == 0 or n == 9:
        rem = list(set(x) ^ set(known[3]))
        if (len(rem) == 6):
          if len(known[3]) == 2:
            for xi in known[3]:
              if xi in rem:
                known[3] = xi
              else:
                known[6] = xi
                              
  for x in data:
    if len(x) == 5:
      rem = set(known[2]) ^ set(x)
      if (len (rem) == 5):
        for xi in known[2]:
          if xi in rem:
            known[2] = xi
          else:
            known[4] = xi

  known_numbers = {}

  for n in number_to_states:
    no = ""
    for ni in number_to_states[n]:
      no += known[ni]
    no = "".join(sorted(list(no)))
    known_numbers[n] = no

  print(known_numbers)
  tens = 1000
  print(PAIN[1])
  for n in PAIN[1]:
    no = "".join(sorted(list(n)))
    for nnn in known_numbers:
      if (known_numbers[nnn] == no):
        print(tens * nnn)
        big_total += tens * nnn
        tens /= 10
print(big_total)

