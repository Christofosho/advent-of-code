def makeBoards(boards):
  return [
    [
      row.strip().split()
      for row in boards[board:board+5]
    ]
    for board in range(1, len(boards), 6)
  ]

def calculate(board, val):
  return int(val) * sum(
    int(i)
    for row in board
    for i in row
    if type(i) is str
  )

def part1(L):
  numbers = L[0].split(",")
  boards  = makeBoards(L[1:])

  for number in numbers:
    for board in boards:
      for row in board:
        for i, val in enumerate(row):
          if val == number:
            row[i] = int(val)

            # Check row
            if all(type(v) is int for v in row):
              return calculate(board, val)

            # Check column
            c = [r[i] for r in board]
            if all(type(e) is int for e in c):
              return calculate(board, val)

            break

def part2(L):
  numbers = L[0].split(",")
  boards  = makeBoards(L[1:])
  winningVal = numbers[0]

  for number in numbers:
    newBoards = []
    for board in boards:
      skip = False
      for row in board:
        for i, val in enumerate(row):
          if val == number:
            row[i] = int(val)
            c = [r[i] for r in board]

            # Check row
            if all(type(v) is int for v in row):
              skip = True
              winningVal = val

            # Check column
            elif all(type(e) is int for e in c):
              skip = True
              winningVal = val

            break # no need to finish the row

        if skip:
          break # no need to finish the board

      # We keep this board because it is not winning
      if not skip:
        newBoards.append(board)

    # Our last boards is correct, because we have
    # no more non-winners.. yep.
    if len(newBoards) == 0:
      return calculate(boards[0], int(winningVal))

    boards = newBoards

with open("input4.txt", "r") as F:
  L = [x.strip() for x in F.readlines()]

  assert part1(L) == 33348
  assert part2(L) == 8112
