import os
from functools import cache
from collections import deque

sample1 = [".|...\\....",
"|.-.\\.....",
".....|-...",
"........|.",
"..........",
".........\\",
"..../.\\\\..",
".-.-/..|..",
".|....-|.\\",
"..//.|...."
]

sample1 = [
  row.replace("\\", "D").replace("/", "U").replace("\n", "")
  for row in sample1
]

X = 0
Y = 1

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

@cache
def move(gridX, gridY, coord, direction):
  y = coord[Y]
  x = coord[X]
  if direction == UP:
    if coord[Y] == 0:
      return None
    y = coord[Y] - 1

  elif direction == RIGHT:
    x = coord[X] + 1
    if x == gridX:
      return None

  elif direction == DOWN:
    y = coord[Y] + 1
    if y == gridY:
      return None

  elif direction == LEFT:
    if coord[X] == 0:
      return None
    x = coord[X] - 1

  return (x, y)

@cache
def checkTile(tile, direction):
  if tile == "D":
    if direction == UP:
      return [LEFT]
    elif direction == RIGHT:
      return [DOWN]
    elif direction == DOWN:
      return [RIGHT]
    elif direction == LEFT:
      return [UP]

  elif tile == "U":
    if direction == UP:
      return [RIGHT]
    elif direction == RIGHT:
      return [UP]
    elif direction == DOWN:
      return [LEFT]
    elif direction == LEFT:
      return [DOWN]

  elif tile == "|":
    if direction == UP or direction == DOWN:
      return [direction]
    elif direction == RIGHT or direction == LEFT:
      return [UP, DOWN]

  elif tile == "-":
    if direction == UP or direction == DOWN:
      return [RIGHT, LEFT]
    elif direction == RIGHT or direction == LEFT:
      return [direction]

  return [direction]

def part1(grid, start, direction):
  gridX, gridY = len(grid[0]), len(grid)
  history = set()
  beams = deque([(start, direction)])

  while beams:
    beam = beams.pop()
    if beam in history:
      continue

    history.add(beam)

    nextXY = move(gridX, gridY, *beam)
    if nextXY is not None:
      tile = grid[nextXY[Y]][nextXY[X]]

      nextDirections = checkTile(tile, beam[1])

      for nextDirection in nextDirections:
        beams.appendleft((nextXY, nextDirection))

  final = set([h[0] for h in history])
  return len(final) - 1


def part2(grid):
  best = 0
  gridX = len(grid[0])
  gridY = len(grid)
  for y in range(gridY):
    best = max(part1(grid, (-1, y), RIGHT), best)
    best = max(part1(grid, (gridX, y), LEFT), best)

  for x in range(gridX):
    best = max(part1(grid, (x, -1), DOWN), best)
    best = max(part1(grid, (x, gridY), UP), best)

  return best


print("Test 1")
assert part1(sample1, (-1, 0), RIGHT) == 46
print("Test 1 passed")

# print("Test 2")
# assert part2(sample1) == 145
# print("Test 2 passed")


path = os.path.join(os.path.dirname(__file__), "../input/16.txt")
with open(path, "r") as f:
  L = f.readlines()
  grid = [
    row.replace("\\", "D").replace("/", "U").replace("\n", "")
    for row in L
  ]

  print("Begin Part 1:")
  assert part1(grid, (-1, 0), RIGHT) == 6994
  print("assert part1(L) == 6994 passed")

  print("Begin Part 2:")
  assert part2(grid) == 7488
  print("assert part2(L) == 7488 passed")
