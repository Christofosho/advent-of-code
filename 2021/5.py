# Advent of Code: Day 5

# Constants
p1 = x = 0
p2 = y = 1

## Helpers
def helper(L):
  lines = [[
    [int(p1) for p1 in line[0].split(",")],
    [int(p2) for p2 in line[1].split(",")]]
    for line in L
  ]

  highestX = 0
  highestY = 0
  for line in lines:
    if line[p1][x] > highestX:
      highestX = line[p1][x]
    if line[p2][x] > highestX:
      highestX = line[p2][x]
    if line[p1][y] > highestY:
      highestY = line[p1][y]
    if line[p2][y] > highestY:
      highestY = line[p2][y]

  return lines, highestX, highestY

## Part 1
def part1(lines, highestX, highestY):
  grid = [
    [0] * (highestX + 1)
    for _ in range(0, highestY + 1)
  ]
  badNodes = 0
  for line in lines:
    p1x, p2x = line[p1][x], line[p2][x]
    p1y, p2y = line[p1][y], line[p2][y]
    if p1y == p2y: # moving on x-axis, y must be ==
      x1, x2 = (p2x, p1x) if p1x > p2x else (p1x, p2x)
      for currentX in range(x1, x2+1):
        grid[p1y][currentX] += 1
        if grid[p1y][currentX] == 2:
          badNodes += 1

    elif p1x == p2x: # moving on y axis
      y1, y2 = (p2y, p1y) if p1y > p2y else (p1y, p2y)
      for currentY in range(y1, y2+1):
        grid[currentY][p1x] += 1
        if grid[currentY][p1x] == 2:
          badNodes += 1

  return badNodes

## Part 2
def part2(lines, highestX, highestY):
  grid = [
    [0] * (highestX + 1)
    for _ in range(0, highestY + 1)
  ]
  badNodes = 0
  for line in lines:
    p1x, p2x = line[p1][x], line[p2][x]
    p1y, p2y = line[p1][y], line[p2][y]
    if abs(p1x - p2x) == abs(p1y - p2y): # Diagonal
      while p1y != p2y:
        grid[p1y][p1x] += 1
        if grid[p1y][p1x] == 2:
          badNodes += 1
        if p1y < p2y:
          p1y += 1
        else:
          p1y -= 1
        if p1x < p2x:
          p1x += 1
        else:
          p1x -= 1

      grid[p2y][p2x] += 1
      if grid[p2y][p2x] == 2:
        badNodes += 1

    elif p1y == p2y: # moving on x-axis, y must be ==
      x1, x2 = (p2x, p1x) if p1x > p2x else (p1x, p2x)
      for currentX in range(x1, x2+1):
        grid[p1y][currentX] += 1
        if grid[p1y][currentX] == 2:
          badNodes += 1

    elif p1x == p2x: # moving on y axis
      y1, y2 = (p2y, p1y) if p1y > p2y else (p1y, p2y)
      for currentY in range(y1, y2+1):
        grid[currentY][p1x] += 1
        if grid[currentY][p1x] == 2:
          badNodes += 1

  return badNodes

with open("2021/input/5.txt", "r") as F:
  L = [
    x.strip().split(" -> ") for x in F.readlines()
  ]

  lines, highestX, highestY = helper(L)
  assert part1(lines, highestX, highestY) == 7269
  assert part2(lines, highestX, highestY) == 21140
