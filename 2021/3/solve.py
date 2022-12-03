lines = [line for line in open("resources/resources.txt")]
limes = [line for line in open("resources/resources.txt")]
#lines = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
#limes = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]


def part_one():
  eps = ""
  gam = ""
  for i in range(len(str(lines[0]))):
    print(i)
    zero_c = 0
    one_c = 0
    for line in lines:
      if line[i] == "0":
        zero_c += 1
      else:
        one_c += 1
    print('\n')
    if zero_c < one_c:
      eps += "1"
      gam += "0"
    else:
      eps += "0"
      gam += "1"

  print(eps)
  print(int(int(eps,2)))
  print(gam)
  print( int(int(gam,2)) )
  print( int(int(eps,2)) * int(int(gam,2)) )
  print("\n")
    # print(zero_c, one_c)
  

def part_two(lines,limes):

  for i in range(len(str(lines[0]))):
    zero_c = 0
    one_c = 0
    for line in lines:
      line = str(line)
      if line[i] == "0":
        zero_c += 1
      else:
        one_c += 1
      most = ""
      if zero_c > one_c:
        most = "0"
      else:
        most = "1"
    print(most)
    lines = list(filter(lambda el: el[i] == most, lines))
    if (len(lines) == 1):
      print(lines)
  
  for i in range(len(str(limes[0]))):
    zero_c = 0
    one_c = 0
    for line in limes:
      line = str(line)
      # print(line[i])
      if line[i] == "0":
        zero_c += 1
      else:
        one_c += 1
        
    most = ""
    if zero_c > one_c:
      print("most, 1")
      most = "1"
    else:
      print("most, 0")
      most = "0"
    limes = list(filter(lambda el: el[i] == most, limes))
    if (len(limes) == 1):
    
      print(limes)
      

print(part_one())
print(part_two(lines,limes))
