# Advent of Code: Day 9

## Tests
def test():
  L = [
    [2, 2, 2],
    [2, 1, 2],
    [2, 2, 2]
  ]

  return part1(L)

def test2():
  L = [
    [9, 9, 8],
    [7, 8, 9],
    [9, 9, 8]
  ]

  L2 = [
    [[y, 0] for y in x]
    for x in L
  ]
  return part2(L, L2)

## Helpers
def isLow(L, row, i, j, width, height, num):
  return all([
    True if i == 0 or num < L[i-1][j] else False, # Up
    True if j == width or num < row[j+1] else False, # Right
    True if i == height or num < L[i+1][j] else False, # Down
    True if j == 0 or num < row[j-1] else False # Left
  ])

def checkSize(L, row, i, j, width, height):
  num = L[i][j][:]
  L[i][j][1] = 1 # flag as seen
  if num[1] == 1 or num[0] == 9:
    return 0

  size = 1
  if i != 0:
    size += checkSize(L, L[i-1], i-1, j, width, height)

  if j != width:
    size += checkSize(L, row, i, j+1, width, height)

  if i != height:
    size += checkSize(L, L[i+1], i+1, j, width, height)

  if j != 0:
    size += checkSize(L, row, i, j-1, width, height)

  return size

## Part 1
def part1(L):
  width = len(L[0]) - 1
  height = len(L) - 1
  total = 0
  for i, row in enumerate(L):
    for j, num in enumerate(row):
      if isLow(L, row, i, j, width, height, num):
        total += num + 1
  return total

## Part 2
def part2(L, L2):
  width = len(L[0]) - 1
  height = len(L) - 1
  basins = []
  for i, row in enumerate(L):
    j = 0
    for num in row:
      if isLow(L, row, i, j, width, height, num):
        basins.append(checkSize(L2, row, i, j, width, height))
      j += 1
  basins.sort(reverse=True)
  print(basins[0] * basins[1] * basins[2])
  return basins[0] * basins[1] * basins[2]


with open("2021/input/9.txt", "r") as F:
  L = [list(map(int, list(x.rstrip()))) for x in F.readlines()]

  assert test() == 2
  assert part1(L) == 475

  L2 = [
    [[y, 0] for y in x]
    for x in L
  ]
  assert test2() == 2
  assert part2(L, L2) == 1092012