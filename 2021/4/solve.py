raw = [line for line in open("resources/alex.txt")]

numbers = [int(n) for n in raw[0].split(',')]
boards = []

board = []
for i in range(2, len(raw)):
  
  if raw[i] == "\n":
    boards.append(board)
    board = []
  else:
    board.append([(int(n), False) for n in list(filter(None, raw[i].split(" ")))])
    
   # board += raw[i]

def check_if_win(board):
  for line in board:
    trues = 0
    for (x, y) in line:
      if y == True:
        trues += 1
    if trues == len(line):
      return True
  
  for i in range(len(board[0])):
    trues = 0
    for j in range(len(board)):
      if board[j][i][1] == True:
        trues += 1
    if trues == len(board):
      return True
      
  return False

def do_number(n, boards):
  for board in boards:
    for line in board:
      for i in range(len(line)):
        if line[i][0] == n:
          line[i] = (n, True)

def do_win_calc(n, board):
  result = 0
  for line in board:
    for (i, b) in line:
      if b == False:
        result += i
  
  return result * n

def printb(board):
  print("===============")
  for line in board:
    for (x, y) in line:
      if x < 10:
        print(" " + str(x), end=' ')
      else:
        print (x, end=' ')
    print('')
   
  print("==============")

part_one = False
for i in numbers:
  do_number(i, boards)
  for b in boards:
    if check_if_win(b):
      if not part_one:
        print("Part One:",do_win_calc(i, b))
        printb(b)
        part_one = True

      if len(boards) == 1:
        print("Part Two:",do_win_calc(i, b))
        exit()
      else:
        boards.remove(b)


print(boards)
