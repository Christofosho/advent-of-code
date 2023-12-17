import os
from functools import cache
from heapq import heappush, heappop

sample1 = ["2413432311323",
"3215453535623",
"3255245654254",
"3446585845452",
"4546657867536",
"1438598798454",
"4457876987766",
"3637877979653",
"4654967986887",
"4564679986453",
"1224686865563",
"2546548887735",
"4322674655533"
]

X = 0
Y = 1

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

@cache
def move(gridX, gridY, coord, direction, oldDirection):
  y = coord[Y]
  x = coord[X]
  if direction == UP:
    if coord[Y] == 0 or oldDirection == DOWN:
      return None
    y = coord[Y] - 1

  elif direction == RIGHT:
    x = coord[X] + 1
    if x == gridX or oldDirection == LEFT:
      return None

  elif direction == DOWN:
    y = coord[Y] + 1
    if y == gridY or oldDirection == UP:
      return None

  elif direction == LEFT:
    if coord[X] == 0 or oldDirection == RIGHT:
      return None
    x = coord[X] - 1

  return (x, y)

def part1(L):
  grid = [
    list(map(int, list(row.replace("\n", ""))))
    for row in L
  ]
  gridX = len(grid[0])
  gridY = len(grid)

  # cost (default 0, not (0,0)'s cost), X, Y, direction, and times seen direction
  q = [(0, 0, 0, -1, 0)]

  costs = {}

  while q:
    cost, x, y, direction, seen = heappop(q)

    current = (x, y, direction, seen)

    if (current in costs):
      continue

    costs[current] = cost

    for d in (UP, RIGHT, DOWN, LEFT):
      newSeen = 1
      if d == direction:
        if seen > 2:
          continue
        newSeen = seen + 1

      newCoord = move(gridX, gridY, (x, y), d, direction)

      if newCoord:
        newX, newY = newCoord
        heappush(q, (cost + grid[newY][newX], newX, newY, d, newSeen))

  # Find max in cached costs
  filtered = [
    v
    for (k, v) in costs.items()
    if k[X] == (gridX - 1) and k[Y] == (gridY - 1)
  ]

  return min(filtered)

def part2(L):
  grid = [
    list(map(int, list(row.replace("\n", ""))))
    for row in L
  ]
  gridX = len(grid[0])
  gridY = len(grid)

  # cost (default 0, not (0,0)'s cost), X, Y, direction, and times seen direction
  q = [(0, 0, 0, -1, 0)]

  costs = {}

  while q:
    cost, x, y, direction, seen = heappop(q)

    current = (x, y, direction, seen)

    if (current in costs):
      continue

    costs[current] = cost

    for d in (UP, RIGHT, DOWN, LEFT):
      if direction != -1 and d != direction and seen < 4:
        continue

      newSeen = 1
      if d == direction:
        if seen > 9:
          continue
        newSeen = seen + 1

      newCoord = move(gridX, gridY, (x, y), d, direction)

      if newCoord:
        newX, newY = newCoord
        heappush(q, (cost + grid[newY][newX], newX, newY, d, newSeen))

  # Find max in cached costs
  filtered = [
    v
    for (k, v) in costs.items()
    if k[X] == (gridX - 1) and k[Y] == (gridY - 1)
  ]

  return min(filtered)


print("Test 1")
assert part1(sample1) == 102
print("Test 1 passed")

print("Test 2")
assert part2(sample1) == 94
print("Test 2 passed")


path = os.path.join(os.path.dirname(__file__), "../input/17.txt")
with open(path, "r") as f:
  L = list(f)

  print("Begin Part 1:")
  assert part1(L) == 902
  print("assert part1(L) == 902 passed")

  print("Begin Part 2:")
  assert part2(L) == 1073
  print("assert part2(L) == 1073 passed")
