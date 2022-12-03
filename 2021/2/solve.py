numbers = [line for line in open("input/input.txt")]



def part_one():
  position_x = 0
  depth = 0
  for line in numbers:
    (a, b) = line.split(" ") 
    print(a, b)
    b = int(b)
    #print (a)   
    if a == "forward":
      position_x += b
    elif a == "down":
      depth += b
    elif a == "up":
      depth -= b
    print(position_x, depth)
  print(position_x, depth)
  return position_x * depth
    
def part_two():
  depth = 0
  y = 0
  aim = 0
  for line in numbers:
    (a, b) = line.split(" ")
    b = int(b)
    if a == "forward":
      y += b
      depth += (b * aim)
    elif a == "down":
      aim += b
    elif a == "up":
      aim -= b
  return y * depth
    

if __name__ == "__main__":
    print("Part 1:", part_one())
    print("Part 2:", part_two())
